import json
import shutil
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from kreyolbench.cli import app
from kreyolbench.governance import ReviewStatus, audit_repository


REPOSITORY_ROOT = Path(__file__).parents[1]


def _copy_audit_fixture(tmp_path: Path) -> Path:
    root = tmp_path / "repository"
    shutil.copytree(REPOSITORY_ROOT / "configs", root / "configs")
    shutil.copytree(REPOSITORY_ROOT / "data" / "sample", root / "data" / "sample")
    shutil.copy2(REPOSITORY_ROOT / "DECISIONS.md", root / "DECISIONS.md")
    return root


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _write_yaml(path: Path, payload: dict) -> None:
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def _load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    serialized = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    path.write_text(serialized, encoding="utf-8")


@pytest.mark.parametrize("status", list(ReviewStatus))
def test_all_review_status_values_are_accepted(status: ReviewStatus):
    assert ReviewStatus(status.value) is status


def test_invalid_review_status_is_rejected():
    with pytest.raises(ValueError):
        ReviewStatus("APPROVED")


def test_current_repository_is_structurally_valid_but_not_release_eligible():
    audit = audit_repository(REPOSITORY_ROOT)

    assert audit.status == "PASS"
    assert audit.errors == []
    assert not audit.release_eligible
    assert "KB-EVAL-001" in audit.unresolved_decisions
    assert "configs/tasks/translation.yaml" in audit.blocked_components


def test_audit_output_is_deterministic():
    first = audit_repository(REPOSITORY_ROOT).as_json()
    second = audit_repository(REPOSITORY_ROOT).as_json()
    assert first == second


def test_missing_governance_field_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "benchmark.yaml"
    payload = _load_yaml(path)
    del payload["decision_ids"]
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert audit.status == "FAIL"
    assert any("decision_ids" in error for error in audit.errors)


def test_unknown_decision_reference_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "benchmark.yaml"
    payload = _load_yaml(path)
    payload["decision_ids"].append("KB-UNKNOWN-999")
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("unresolved decision reference KB-UNKNOWN-999" in error for error in audit.errors)


def test_release_candidate_with_unresolved_decision_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "tasks" / "classification.yaml"
    payload = _load_yaml(path)
    payload["release_candidate"] = True
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert audit.status == "FAIL"
    assert any("release candidate is not EXPERT_VALIDATED" in error for error in audit.errors)
    assert any("depends on unresolved decisions" in error for error in audit.errors)


@pytest.mark.parametrize(
    ("review_status", "redistribution_allowed", "should_error"),
    [
        ("approved_public_release", True, False),
        ("approved_link_only", False, False),
        ("pending_legal_review", None, False),
        ("not_approved_for_redistribution", False, False),
        ("pending_legal_review", True, True),
        ("approved_public_release", False, True),
    ],
)
def test_source_redistribution_policy(
    tmp_path: Path,
    review_status: str,
    redistribution_allowed: bool | None,
    should_error: bool,
):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "sources" / "news_candidates.yaml"
    payload = _load_yaml(path)
    payload["review_status"] = review_status
    payload["redistribution_allowed"] = redistribution_allowed
    _write_yaml(path, payload)

    audit = audit_repository(root)
    source_errors = [error for error in audit.errors if "news_candidates.yaml" in error]

    assert bool(source_errors) is should_error


def test_duplicate_example_ids_fail(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "data" / "sample" / "classification_topic.jsonl"
    rows = _load_jsonl(path)
    rows.append(rows[0].copy())
    _write_jsonl(path, rows)

    audit = audit_repository(root)

    assert any("duplicate ID kb_sample_cls_0001" in error for error in audit.errors)


def test_exact_train_test_contamination_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "data" / "sample" / "classification_topic.jsonl"
    rows = _load_jsonl(path)
    train_copy = json.loads(json.dumps(rows[0]))
    train_copy["id"] = "kb_sample_cls_train_copy"
    train_copy["split"] = "train"
    rows.append(train_copy)
    _write_jsonl(path, rows)

    audit = audit_repository(root)

    assert any("exact input-text contamination" in error for error in audit.errors)


def test_normalized_text_requires_raw_linkage(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "data" / "sample" / "normalization.jsonl"
    rows = _load_jsonl(path)
    rows[0]["input"].pop("raw_text")
    _write_jsonl(path, rows)

    audit = audit_repository(root)

    assert any("missing input.raw_text" in error for error in audit.errors)


def test_sample_source_must_resolve(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "data" / "sample" / "qa.jsonl"
    rows = _load_jsonl(path)
    rows[0]["source"]["source_id"] = "missing_source"
    _write_jsonl(path, rows)

    audit = audit_repository(root)

    assert any("source_id missing_source is not registered" in error for error in audit.errors)


def test_invalid_configured_label_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "data" / "sample" / "sentiment.jsonl"
    rows = _load_jsonl(path)
    rows[0]["target"]["label"] = "very_positive"
    _write_jsonl(path, rows)

    audit = audit_repository(root)

    assert any("label 'very_positive' is not valid for sentiment" in error for error in audit.errors)


def test_audit_governance_cli_text_output():
    result = CliRunner().invoke(
        app, ["audit-governance", "--root", str(REPOSITORY_ROOT), "--format", "text"]
    )

    assert result.exit_code == 0
    assert "status: PASS" in result.output
    assert "release_eligible: false" in result.output


def test_audit_governance_cli_json_output():
    result = CliRunner().invoke(
        app, ["audit-governance", "--root", str(REPOSITORY_ROOT), "--format", "json"]
    )

    assert result.exit_code == 0
    payload = json.loads(result.output)
    assert payload["status"] == "PASS"
    assert payload["release_eligible"] is False
    assert payload["errors"] == []


def test_audit_governance_cli_rejects_unknown_format():
    result = CliRunner().invoke(
        app, ["audit-governance", "--root", str(REPOSITORY_ROOT), "--format", "xml"]
    )

    assert result.exit_code != 0
    assert "--format must be 'text' or 'json'" in result.output
