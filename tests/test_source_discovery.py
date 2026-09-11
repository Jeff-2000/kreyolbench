"""Discovery is evidence-backed intake, never an authorization shortcut."""

import copy
import shutil
from datetime import date, timedelta
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from kreyolbench.governance import (
    MetadataClaim,
    SourceFeasibilityRecord,
    SourceRecord,
    audit_repository,
)
from kreyolbench.source_discovery import DiscoveryLead, ReportedSize, SourceDiscoveryLedger


ROOT = Path(__file__).parents[1]
LEDGER_PATH = Path("configs/governance/source_discovery.yaml")
SUPPLIED_LEADS = {
    "jsbeaudry_stem", "wikipedia_20231101_ht", "flores_plus_hat", "xp3x_hat",
    "aya_haitian", "finepdfs_hat", "mc4_ht", "kreyol_mt", "creoleval",
    "mit_haiti_parallel", "cmu_original", "cmu_hf_mirror", "babel_haitian",
    "voxlingua107_hat", "northern_haitian", "ud_autogramm", "ud_adolphe",
    "munro_sms", "apics_survey49", "apics_structure49", "xm3600", "vicr_translated",
}


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def discovery():
    return load(ROOT / LEDGER_PATH)


def lead(identifier="wikipedia_20231101_ht"):
    return next(item for item in discovery()["leads"] if item["lead_id"] == identifier)


def copy_fixture(tmp_path):
    for name in ["configs", "reports"]:
        shutil.copytree(ROOT / name, tmp_path / name)
    shutil.copytree(ROOT / "data/sample", tmp_path / "data/sample")
    shutil.copy2(ROOT / "DECISIONS.md", tmp_path / "DECISIONS.md")
    return tmp_path


def test_every_supplied_lead_is_retained_without_defining_a_fixed_universe():
    model = SourceDiscoveryLedger.model_validate(discovery())
    assert SUPPLIED_LEADS <= {item.lead_id for item in model.leads}
    assert {item.disposition for item in model.leads} == {
        "REGISTERED_SOURCE", "UNVERIFIED_LEAD", "REFERENCE_ONLY"
    }


def test_original_source_permissions_are_unchanged():
    snapshot = load(ROOT / "reports/source_reviews/history/source_authorization_initial_20260910.yaml")
    current = {record["source_id"]: record for record in (
        load(path) for path in (ROOT / "configs/sources").glob("*.yaml")
    )}
    for source_id, original in snapshot["sources"].items():
        normalized = SourceRecord.model_validate(current[source_id]).model_dump(mode="json")
        assert {key: normalized[key] for key in original} == original
    for source_id in current.keys() - snapshot["sources"].keys():
        record = current[source_id]
        assert not record["release_candidate"]
        assert record["source_governance"]["collection_status"] == "NOT_REQUESTED"
        assert record["source_governance"]["redistribution_status"] == "UNKNOWN"
        assert record["source_governance"]["scientific_status"] == "PENDING_EXPERT_REVIEW"


def test_original_review_is_preserved_and_active_coverage_is_dynamic():
    historical = load(ROOT / "reports/source_reviews/history/source_feasibility_initial_20260910.yaml")
    current = load(ROOT / "configs/governance/source_feasibility.yaml")
    assert historical["schema_version"] == 1
    assert len(historical["candidate_reviews"]) == 21  # Historical snapshot only.
    assert current["schema_version"] == 2
    assert {r["source_id"] for r in historical["candidate_reviews"]} <= {
        r["source_id"] for r in current["candidate_reviews"]
    }


@pytest.mark.parametrize("mutation", ["duplicate_id", "duplicate_identity", "missing_intake",
                                     "extra_intake", "invalid_disposition", "approval"])
def test_discovery_inventory_rejects_inconsistent_records(mutation):
    payload = discovery()
    if mutation == "duplicate_id":
        payload["leads"].append(copy.deepcopy(payload["leads"][0]))
    elif mutation == "duplicate_identity":
        duplicate = copy.deepcopy(payload["leads"][0])
        duplicate["lead_id"] = "different_name_same_resource"
        payload["leads"].append(duplicate)
        payload["intakes"][0]["lead_ids"].append(duplicate["lead_id"])
    elif mutation == "missing_intake":
        payload["intakes"][0]["lead_ids"].pop()
    elif mutation == "extra_intake":
        payload["intakes"][0]["lead_ids"].append("lost_resource")
    elif mutation == "invalid_disposition":
        payload["leads"][0]["disposition"] = "APPROVED"
    else:
        payload["authorization_effect"] = "APPROVED"
    with pytest.raises(ValidationError):
        SourceDiscoveryLedger.model_validate(payload)


@pytest.mark.parametrize("field,value", [
    ("language_evidence", "CLAIMED"), ("language_claims", []),
    ("source_id", None), ("disposition", "REFERENCE_ONLY"),
    ("content_origin", "HUMAN_ORIGINAL"),
])
def test_registration_requires_language_evidence_and_origin_is_not_inferred(field, value):
    payload = lead()
    payload[field] = value
    with pytest.raises(ValidationError):
        DiscoveryLead.model_validate(payload)


def test_reference_and_unverified_resources_are_not_registered_corpora():
    for identifier in ["xm3600", "vicr_translated", "northern_haitian", "apics_survey49",
                       "apics_structure49", "voxlingua107_hat", "jsbeaudry_stem"]:
        assert lead(identifier)["source_id"] is None
    assert lead("aya_haitian")["content_origin"] == "MACHINE_TRANSLATION"


def test_snapshots_mirrors_and_treebanks_are_distinct():
    assert lead("ud_autogramm")["source_id"] != lead("ud_adolphe")["source_id"]
    sources = {r["source_id"]: r for r in (
        load(path) for path in (ROOT / "configs/sources").glob("*.yaml")
    )}
    assert sources[lead()["source_id"]]["parent_source_id"] == "wikimedia_htwiki"
    assert sources[lead("cmu_hf_mirror")["source_id"]]["parent_source_id"] == "cmu_haitian"
    assert sources[lead("cmu_hf_mirror")["source_id"]]["license"] == "TO_VERIFY"


@pytest.mark.parametrize("field,value", [("unit", "EXAMPLES_OR_HOURS"), ("value", -1),
                                         ("split", ""), ("revision", ""),
                                         ("verification_state", "INDEPENDENTLY_VERIFIED")])
def test_reported_sizes_require_units_context_and_honest_verification(field, value):
    payload = lead()["reported_sizes"][0]
    payload[field] = value
    with pytest.raises(ValidationError):
        ReportedSize.model_validate(payload)


@pytest.mark.parametrize("mutation", ["missing_claim", "inference_only", "invalid_url",
                                     "future_date", "postdated_review", "unknown_dimension"])
def test_available_evidence_requires_a_direct_dated_claim(mutation):
    record = load(ROOT / "configs/governance/source_feasibility.yaml")["candidate_reviews"][0]
    dimension = "endpoint_provider_identity"
    claim = record["dimension_evidence"][dimension][0]
    if mutation == "missing_claim":
        record["dimension_evidence"].pop(dimension)
    elif mutation == "inference_only":
        claim["basis"] = "INFERENCE"
    elif mutation == "invalid_url":
        claim["url"] = "file:///private/secret"
    elif mutation == "future_date":
        claim["accessed_on"] = date.today() + timedelta(days=1)
    elif mutation == "postdated_review":
        record["reviewed_on"] = date(2026, 9, 9)
    else:
        record["dimension_evidence"]["invented_dimension"] = [claim]
    with pytest.raises(ValidationError):
        SourceFeasibilityRecord.model_validate(record)


@pytest.mark.parametrize("field,value", [
    ("source_id", "missing_source"), ("candidate_task_family_ids", ["missing_family"]),
    ("candidate_domain_ids", ["missing_domain"]),
    ("candidate_task_instance_ids", ["missing_task"]),
    ("evidence_path", "../outside.md"),
])
def test_discovery_audit_rejects_unresolved_references(tmp_path, field, value):
    root = copy_fixture(tmp_path)
    payload = discovery()
    payload["leads"][1][field] = value
    (root / LEDGER_PATH).write_text(yaml.safe_dump(payload), encoding="utf-8")
    assert audit_repository(root).errors


def test_relationship_references_resolve_without_transferring_approval(tmp_path):
    root = copy_fixture(tmp_path)
    payload = discovery()
    payload["relationships"][0]["to_source_id"] = "unknown_upstream"
    (root / LEDGER_PATH).write_text(yaml.safe_dump(payload), encoding="utf-8")
    assert any("relationship: unknown source_id" in e for e in audit_repository(root).errors)


def test_future_reference_can_be_registered_without_changing_python_enums():
    payload = discovery()
    future = copy.deepcopy(lead("xm3600"))
    future.update(lead_id="future_reference", canonical_url="https://example.org/new-reference")
    payload["leads"].append(future)
    payload["intakes"].append({"intake_id": "future_intake", "received_on": "2026-09-10",
                               "supplied_by": "Test fixture", "lead_ids": [future["lead_id"]]})
    assert SourceDiscoveryLedger.model_validate(payload).open_world


def test_expansion_preserves_unresolved_tasks_and_nonrelease_state():
    audit = audit_repository(ROOT)
    assert audit.errors == []
    assert audit.warnings == []
    assert audit.release_eligible is False
    assert audit.unresolved_decisions == ["KB-TASK-CLS-001", "KB-TASK-CS-001", "KB-TASK-NER-001",
                                          "KB-TASK-NORM-001", "KB-TASK-RET-001"]
    assert audit.as_json() == audit_repository(ROOT).as_json()


def test_blank_evidence_and_future_dates_are_rejected():
    payload = lead()["language_claims"][0]
    payload["claim"] = "   "
    with pytest.raises(ValidationError):
        MetadataClaim.model_validate(payload)
