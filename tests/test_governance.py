import json
import shutil
from datetime import date
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from kreyolbench.cli import app
from kreyolbench.governance import (
    AccessStatus,
    CollectionStatus,
    ConflictStatus,
    DecisionRecord,
    DiscoveryStatus,
    EvidenceState,
    EthicsStatus,
    FeasibilityConclusion,
    LegalReviewStatus,
    PermissionStatus,
    RedistributionStatus,
    ReviewIndependence,
    ReviewOutcome,
    ReviewStatus,
    ScopeStatus,
    ScientificInclusionStatus,
    SourceReviewAction,
    SourceRecordType,
    audit_repository,
)


REPOSITORY_ROOT = Path(__file__).parents[1]


def _copy_audit_fixture(tmp_path: Path) -> Path:
    root = tmp_path / "repository"
    shutil.copytree(REPOSITORY_ROOT / "configs", root / "configs")
    shutil.copytree(REPOSITORY_ROOT / "data" / "sample", root / "data" / "sample")
    shutil.copytree(REPOSITORY_ROOT / "reports", root / "reports")
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


@pytest.mark.parametrize("status", list(ScopeStatus))
def test_all_scope_status_values_are_accepted(status: ScopeStatus):
    assert ScopeStatus(status.value) is status


def test_review_status_is_not_a_scope_status():
    with pytest.raises(ValueError):
        ScopeStatus(ReviewStatus.SUBMITTED_TO_REVIEW.value)


@pytest.mark.parametrize(
    "enum_type",
    [
        SourceRecordType,
        DiscoveryStatus,
        AccessStatus,
        LegalReviewStatus,
        CollectionStatus,
        PermissionStatus,
        RedistributionStatus,
        EthicsStatus,
        ScientificInclusionStatus,
        EvidenceState,
        FeasibilityConclusion,
        ReviewOutcome,
        ReviewIndependence,
        ConflictStatus,
        SourceReviewAction,
    ],
)
def test_governance_enum_values_are_strict(enum_type):
    for status in enum_type:
        assert enum_type(status.value) is status
    with pytest.raises(ValueError):
        enum_type("INVALID")


def test_current_repository_is_structurally_valid_but_not_release_eligible():
    audit = audit_repository(REPOSITORY_ROOT)

    assert audit.status == "PASS"
    assert audit.errors == []
    assert not audit.release_eligible
    assert audit.unresolved_decisions == [
        "KB-TASK-CLS-001",
        "KB-TASK-CS-001",
        "KB-TASK-NER-001",
        "KB-TASK-NORM-001",
        "KB-TASK-RET-001",
    ]
    assert "configs/tasks/translation.yaml" in audit.blocked_components


def test_data001_preserves_both_review_events():
    registry = _load_yaml(REPOSITORY_ROOT / "configs" / "governance" / "decisions.yaml")
    data001 = next(item for item in registry["decisions"] if item["id"] == "KB-DATA-001")

    assert [event["outcome"] for event in data001["review_history"]] == [
        ReviewOutcome.REVISED.value,
        ReviewOutcome.APPROVED.value,
    ]
    assert data001["review_history"][-1]["independence"] == (
        ReviewIndependence.INTERNAL_PROJECT_LEAD.value
    )


def test_validated_decision_requires_latest_approved_review(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "governance" / "decisions.yaml"
    payload = _load_yaml(path)
    decision = next(item for item in payload["decisions"] if item["id"] == "KB-DATA-001")
    decision["review_history"][-1]["outcome"] = "REVISED"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("latest APPROVED review" in error for error in audit.errors)


def test_review_evidence_path_must_exist(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "governance" / "decisions.yaml"
    payload = _load_yaml(path)
    decision = next(item for item in payload["decisions"] if item["id"] == "KB-DATA-001")
    decision["review_history"][-1]["evidence_path"] = "reports/missing.md"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("evidence_path does not exist" in error for error in audit.errors)


def _externally_gated_decision(review_history: list[dict], status: str = "EXPERT_VALIDATED"):
    return {
        "id": "KB-TASK-TEST-001",
        "title": "Test task",
        "status": status,
        "requires_expert_approval": True,
        "review_requirements": {
            "required_independence": "EXTERNAL_INDEPENDENT",
            "minimum_external_approvals": 1,
            "required_expertise_tags": ["HAITIAN_CREOLE_LINGUISTICS", "TASK_METHODS"],
            "require_affiliation": True,
            "require_conflict_disclosure": True,
        },
        "review_history": review_history,
    }


def _external_approval(**overrides) -> dict:
    event = {
        "outcome": "APPROVED",
        "reviewer": "Marie Example",
        "reviewer_role": "Associate Professor",
        "reviewer_affiliation": "Example University",
        "expertise_tags": ["HAITIAN_CREOLE_LINGUISTICS", "TASK_METHODS"],
        "conflict_status": "NONE_DECLARED",
        "conflict_details": "",
        "human_attestation": True,
        "reviewed_on": "2026-09-10",
        "independence": "EXTERNAL_INDEPENDENT",
        "evidence_path": "reports/reviews/example.md",
        "notes": "Synthetic test record.",
    }
    event.update(overrides)
    return event


def test_internal_approval_cannot_satisfy_external_review_requirement():
    event = _external_approval(
        reviewer="Jeff Pierre",
        reviewer_affiliation=None,
        expertise_tags=[],
        conflict_status=None,
        independence="INTERNAL_PROJECT_LEAD",
    )
    with pytest.raises(ValueError, match="required independent approvals"):
        DecisionRecord.model_validate(_externally_gated_decision([event]))


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("reviewer_affiliation", None, "reviewer_affiliation"),
        ("expertise_tags", [], "expertise_tags"),
        ("conflict_status", None, "conflict_status"),
        ("human_attestation", False, "human_attestation"),
    ],
)
def test_external_approval_requires_complete_reviewer_evidence(field, value, message):
    with pytest.raises(ValueError, match=message):
        DecisionRecord.model_validate(
            _externally_gated_decision([_external_approval(**{field: value})])
        )


def test_disqualifying_conflict_cannot_support_approval():
    with pytest.raises(ValueError, match="disqualifying conflict"):
        DecisionRecord.model_validate(
            _externally_gated_decision(
                [_external_approval(conflict_status="DISQUALIFYING")]
            )
        )


def test_one_dual_qualified_external_reviewer_can_satisfy_requirements():
    decision = DecisionRecord.model_validate(
        _externally_gated_decision([_external_approval()])
    )
    assert decision.status is ReviewStatus.EXPERT_VALIDATED


def test_multiple_external_reviewers_can_collectively_cover_expertise():
    first = _external_approval(
        reviewer="Linguistics Reviewer",
        expertise_tags=["HAITIAN_CREOLE_LINGUISTICS"],
    )
    second = _external_approval(
        reviewer="Methods Reviewer",
        expertise_tags=["TASK_METHODS"],
    )
    decision = DecisionRecord.model_validate(
        _externally_gated_decision([first, second])
    )
    assert decision.status is ReviewStatus.EXPERT_VALIDATED


def test_task_revision_event_is_preserved_after_resubmission():
    registry = _load_yaml(REPOSITORY_ROOT / "configs" / "governance" / "decisions.yaml")
    tasks = [item for item in registry["decisions"] if item["id"].startswith("KB-TASK-")]

    assert len(tasks) == 5
    for task in tasks:
        assert task["status"] == ReviewStatus.SUBMITTED_TO_REVIEW.value
        assert task["review_history"][-1]["outcome"] == ReviewOutcome.REVISED.value
        assert task["review_history"][-1]["independence"] == (
            ReviewIndependence.INTERNAL_PROJECT_LEAD.value
        )


def test_v0_scope_matches_expert_decision():
    release = _load_yaml(REPOSITORY_ROOT / "configs" / "releases" / "v0_1.yaml")
    memberships = {
        item["task_instance_id"]: item["scope_status"]
        for item in release["task_memberships"]
    }

    assert {
        task_id
        for task_id, scope_status in memberships.items()
        if scope_status == ScopeStatus.PILOT_CANDIDATE.value
    } == {
        "kb_cls_topic_multilabel_v0_1",
        "kb_ie_ner_charspan_v0_1",
        "kb_ret_hybrid_query_v0_1",
        "kb_norm_orthography_v0_1",
        "kb_lc_token_language_id_v0_1",
    }
    assert memberships["kb_qa_extractive_v0_1_feasibility"] == "FEASIBILITY_ONLY"
    assert memberships["kb_mt_text_v0_1_deferred"] == "DEFERRED"
    assert "kb_cls_sentiment_roadmap" not in memberships
    assert "kb_gen_summarization_roadmap" not in memberships
    assert ScopeStatus.INCLUDED_IN_RELEASE.value not in memberships.values()


def test_task_scientific_status_cannot_be_used_as_scope_status(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "tasks" / "qa.yaml"
    payload = _load_yaml(path)
    payload["scope_status"] = "SUBMITTED_TO_REVIEW"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("invalid task instance" in error for error in audit.errors)


def test_feasibility_matrix_covers_all_v0_tasks():
    matrix = _load_yaml(
        REPOSITORY_ROOT / "configs" / "governance" / "task_feasibility.yaml"
    )

    assert {record["task_instance_id"] for record in matrix["tasks"]} == {
        "kb_cls_topic_multilabel_v0_1",
        "kb_ie_ner_charspan_v0_1",
        "kb_ret_hybrid_query_v0_1",
        "kb_norm_orthography_v0_1",
        "kb_lc_token_language_id_v0_1",
    }
    assert {record["overall"] for record in matrix["tasks"]} == {"CONDITIONAL"}


def test_pilot_feasible_rejects_missing_evidence(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "governance" / "task_feasibility.yaml"
    payload = _load_yaml(path)
    payload["tasks"][0]["overall"] = "PILOT_FEASIBLE"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("PILOT_FEASIBLE cannot contain" in error for error in audit.errors)


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
    payload["scope_status"] = "RELEASE_CANDIDATE"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert audit.status == "FAIL"
    assert any("RELEASE_CANDIDATE requires EXPERT_VALIDATED" in error for error in audit.errors)
    assert any("RELEASE_CANDIDATE depends on unresolved decisions" in error for error in audit.errors)


def test_task_instance_ids_are_stable_and_unique():
    expected = {
        "classification": "kb_cls_topic_multilabel_v0_1",
        "ner": "kb_ie_ner_charspan_v0_1",
        "retrieval": "kb_ret_hybrid_query_v0_1",
        "normalization": "kb_norm_orthography_v0_1",
        "codeswitch": "kb_lc_token_language_id_v0_1",
        "qa": "kb_qa_extractive_v0_1_feasibility",
        "translation": "kb_mt_text_v0_1_deferred",
        "sentiment": "kb_cls_sentiment_roadmap",
        "summarization": "kb_gen_summarization_roadmap",
    }
    actual = {
        path.stem: _load_yaml(path)["task_instance_id"]
        for path in (REPOSITORY_ROOT / "configs" / "tasks").glob("*.yaml")
    }

    assert actual == expected
    assert len(actual.values()) == len(set(actual.values()))


def test_duplicate_task_instance_id_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    classification = _load_yaml(root / "configs" / "tasks" / "classification.yaml")
    path = root / "configs" / "tasks" / "sentiment.yaml"
    sentiment = _load_yaml(path)
    sentiment["task_instance_id"] = classification["task_instance_id"]
    _write_yaml(path, sentiment)

    audit = audit_repository(root)

    assert any("duplicate task_instance_id" in error for error in audit.errors)


def test_unknown_task_family_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "tasks" / "classification.yaml"
    payload = _load_yaml(path)
    payload["task_family_id"] = "unknown_family"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("unknown task_family_id unknown_family" in error for error in audit.errors)


def test_task_type_must_resolve_within_family(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "tasks" / "classification.yaml"
    payload = _load_yaml(path)
    payload["task_type_id"] = "unregistered_classification_type"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any(
        "task_type_id unregistered_classification_type is not registered" in error
        for error in audit.errors
    )


def test_unregistered_sample_domain_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "data" / "sample" / "classification_topic.jsonl"
    rows = _load_jsonl(path)
    rows[0]["domain"] = "unregistered_domain"
    _write_jsonl(path, rows)

    audit = audit_repository(root)

    assert any("domain unregistered_domain is not registered" in error for error in audit.errors)


def test_future_task_family_registration_does_not_require_core_code_change(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "task_taxonomy.yaml"
    payload = _load_yaml(path)
    payload["task_families"].append(
        {
            "family_id": "future_research_family",
            "name": "Future research family",
            "scope_status": "ROADMAP",
            "modalities": ["future_modality"],
            "task_type_ids": ["future_task_type"],
        }
    )
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert audit.status == "PASS"
    assert not [error for error in audit.errors if "future_research_family" in error]


def test_roadmap_task_cannot_be_added_to_release(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "releases" / "v0_1.yaml"
    payload = _load_yaml(path)
    payload["task_memberships"].append(
        {
            "task_instance_id": "kb_cls_sentiment_roadmap",
            "scope_status": "ROADMAP",
        }
    )
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("roadmap or discovery tasks do not belong" in error for error in audit.errors)


def test_unknown_release_task_instance_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "releases" / "v0_1.yaml"
    payload = _load_yaml(path)
    payload["task_memberships"].append(
        {"task_instance_id": "kb_unknown_task", "scope_status": "PILOT_CANDIDATE"}
    )
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("unknown task_instance_id kb_unknown_task" in error for error in audit.errors)


def test_release_membership_scope_must_match_task_instance(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "releases" / "v0_1.yaml"
    payload = _load_yaml(path)
    payload["task_memberships"][0]["scope_status"] = "FEASIBILITY_ONLY"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("membership scope" in error for error in audit.errors)


def test_scope002_is_synchronized_and_review_packet_tracks_task_decisions():
    registry = _load_yaml(REPOSITORY_ROOT / "configs" / "governance" / "decisions.yaml")
    scope002 = next(item for item in registry["decisions"] if item["id"] == "KB-SCOPE-002")
    decisions_doc = (REPOSITORY_ROOT / "DECISIONS.md").read_text(encoding="utf-8")
    packet = (REPOSITORY_ROOT / "reports" / "TASK_SPEC_REVIEW_PACKET_V0_1.md").read_text(
        encoding="utf-8"
    )

    assert scope002["status"] == "EXPERT_VALIDATED"
    assert scope002["review_history"][-1] == {
        "outcome": "APPROVED",
        "reviewer": "Jeff Pierre",
        "reviewer_role": "Project Lead and Scientific Reviewer",
        "reviewed_on": date(2026, 9, 9),
        "independence": "INTERNAL_PROJECT_LEAD",
        "evidence_path": "reports/TASK_SPEC_REVIEW_PACKET_V0_1.md",
        "notes": "Project-scope policy approval only; no task, source, dataset, metric, or release authorization.",
    }
    assert "## KB-SCOPE-002" in decisions_doc
    for decision_id in {
        "KB-TASK-CLS-001",
        "KB-TASK-NER-001",
        "KB-TASK-RET-001",
        "KB-TASK-NORM-001",
        "KB-TASK-CS-001",
    }:
        assert f"## {decision_id}" in packet


@pytest.mark.parametrize(
    ("legal_status", "ethics_status", "redistribution_status", "should_error"),
    [
        ("APPROVED", "APPROVED", "APPROVED", False),
        ("PENDING", "APPROVED", "APPROVED", True),
        ("APPROVED", "PENDING", "APPROVED", True),
        ("CONDITIONAL", "PENDING", "CONDITIONAL", False),
        ("REJECTED", "APPROVED", "APPROVED", True),
    ],
)
def test_source_redistribution_policy_v2(
    tmp_path: Path,
    legal_status: str,
    ethics_status: str,
    redistribution_status: str,
    should_error: bool,
):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "sources" / "sample.yaml"
    payload = _load_yaml(path)
    payload["source_governance"]["legal_review_status"] = legal_status
    payload["source_governance"]["ethics_status"] = ethics_status
    payload["source_governance"]["redistribution_status"] = redistribution_status
    _write_yaml(path, payload)

    audit = audit_repository(root)
    source_errors = [error for error in audit.errors if "sample.yaml" in error]

    assert bool(source_errors) is should_error


def test_metadata_review_rejects_collection_authorization_elevation(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "sources" / "mspp.yaml"
    payload = _load_yaml(path)
    payload["source_governance"]["collection_status"] = "APPROVED"
    payload["source_governance"]["redistribution_status"] = "UNKNOWN"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any(
        "metadata-only review cannot accompany an authorized source state" in error
        and "mspp_publications" in error
        for error in audit.errors
    )


def test_source_feasibility_covers_all_candidates_and_sample_control():
    ledger = _load_yaml(
        REPOSITORY_ROOT / "configs" / "governance" / "source_feasibility.yaml"
    )
    source_ids = {
        _load_yaml(path)["source_id"]
        for path in (REPOSITORY_ROOT / "configs" / "sources").glob("*.yaml")
    }
    candidate_ids = {item["source_id"] for item in ledger["candidate_reviews"]}

    assert len(candidate_ids) == len(ledger["candidate_reviews"])
    assert candidate_ids == source_ids - {"sample"}
    assert ledger["synthetic_control"]["source_id"] == "sample"
    assert ledger["synthetic_control"]["authorization_effect"] == "NONE"


def test_missing_source_feasibility_record_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "governance" / "source_feasibility.yaml"
    payload = _load_yaml(path)
    payload["candidate_reviews"].pop()
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("source review coverage mismatch" in error for error in audit.errors)


def test_source_feasibility_evidence_path_must_exist(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "governance" / "source_feasibility.yaml"
    payload = _load_yaml(path)
    payload["candidate_reviews"][0]["evidence_path"] = (
        "reports/source_reviews/missing.md"
    )
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("evidence_path does not exist" in error for error in audit.errors)


def test_source_feasibility_task_reference_must_resolve(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "governance" / "source_feasibility.yaml"
    payload = _load_yaml(path)
    payload["candidate_reviews"][0]["candidate_task_instance_ids"] = [
        "kb_unknown_task"
    ]
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("references unknown task instances" in error for error in audit.errors)


def test_source_feasibility_available_evidence_requires_url(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "governance" / "source_feasibility.yaml"
    payload = _load_yaml(path)
    payload["candidate_reviews"][0]["authoritative_evidence_urls"] = []
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any(
        "EVIDENCE_AVAILABLE requires an authoritative evidence URL" in error
        for error in audit.errors
    )


def test_source_metadata_review_cannot_declare_pilot_feasible(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "governance" / "source_feasibility.yaml"
    payload = _load_yaml(path)
    payload["candidate_reviews"][0]["overall"] = "PILOT_FEASIBLE"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any(
        "cannot declare a source PILOT_FEASIBLE" in error for error in audit.errors
    )


def test_source_family_cannot_be_recommended_for_permission(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "governance" / "source_feasibility.yaml"
    payload = _load_yaml(path)
    family = next(
        item
        for item in payload["candidate_reviews"]
        if item["source_id"] == "aka_official"
    )
    family["recommended_actions"] = ["REQUEST_PERMISSION"]
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any(
        "SOURCE_FAMILY aka_official cannot be recommended directly" in error
        for error in audit.errors
    )


def test_synthetic_control_may_be_reusable_but_stays_scientifically_excluded():
    audit = audit_repository(REPOSITORY_ROOT)

    assert not [
        error for error in audit.errors if "authorized source state for sample" in error
    ]


def test_synthetic_control_cannot_become_scientific_evidence(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "sources" / "sample.yaml"
    payload = _load_yaml(path)
    payload["source_governance"]["scientific_status"] = "PILOT_ONLY"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any(
        "synthetic sample must remain scientifically excluded" in error
        for error in audit.errors
    )


def test_source_family_cannot_receive_blanket_approval(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "sources" / "news_candidates.yaml"
    payload = _load_yaml(path)
    payload["source_governance"]["collection_status"] = "APPROVED"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("SOURCE_FAMILY cannot have collection_status APPROVED" in error for error in audit.errors)


def test_committed_legacy_source_schema_is_rejected(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "sources" / "news_candidates.yaml"
    payload = _load_yaml(path)
    payload.pop("source_schema_version")
    payload["review_status"] = "pending_legal_review"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("committed source configs must use source_schema_version: 2" in error for error in audit.errors)


def test_missing_source_parent_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "configs" / "sources" / "radio_haiti_corpus.yaml"
    payload = _load_yaml(path)
    payload["parent_source_id"] = "missing_parent"
    _write_yaml(path, payload)

    audit = audit_repository(root)

    assert any("parent_source_id missing_parent is not registered" in error for error in audit.errors)


def test_source_hierarchy_cycle_fails(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    parent_path = root / "configs" / "sources" / "radio_haiti_archive.yaml"
    parent = _load_yaml(parent_path)
    parent["parent_source_id"] = "radio_haiti_inter_lrec2026"
    _write_yaml(parent_path, parent)

    audit = audit_repository(root)

    assert any("source hierarchy cycle" in error for error in audit.errors)


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


def test_sample_rows_cannot_reference_source_family(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "data" / "sample" / "qa.jsonl"
    rows = _load_jsonl(path)
    rows[0]["source"]["source_id"] = "aka_official"
    _write_jsonl(path, rows)

    audit = audit_repository(root)

    assert any("discovery-only SOURCE_FAMILY" in error for error in audit.errors)


def test_retrieval_qrel_must_reference_existing_document(tmp_path: Path):
    root = _copy_audit_fixture(tmp_path)
    path = root / "data" / "sample" / "retrieval" / "qrels.jsonl"
    rows = _load_jsonl(path)
    rows[0]["doc_id"] = "missing_document"
    _write_jsonl(path, rows)

    audit = audit_repository(root)

    assert any("qrel doc_id missing_document is missing" in error for error in audit.errors)


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
