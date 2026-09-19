"""Project-Lead source review remains attributable, multi-axis, and non-authorizing."""

from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from kreyolbench.governance import SourceFeasibilityRecord, SourceRecord, audit_repository
from kreyolbench.source_assessments import (
    SourceContaminationLedger,
    SourceDiversityLedger,
    SourcePriorityLedger,
    SourceUseLedger,
)


ROOT = Path(__file__).parents[1]


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def feasibility():
    return load(ROOT / "configs/governance/source_feasibility.yaml")


def records():
    return {item["source_id"]: item for item in feasibility()["candidate_reviews"]}


def sources():
    return {
        item["source_id"]: SourceRecord.model_validate(item)
        for item in (
            load(path) for path in (ROOT / "configs/sources").glob("*.yaml")
        )
    }


def test_project_lead_review_preserves_initial_scope_and_adds_expanded_scope():
    ledger = feasibility()
    reviewed = {
        source_id
        for source_id, record in records().items()
        if any(event["event_type"] == "PROJECT_LEAD_REVIEW_DECISION" for event in record["review_history"])
    }
    initial = {
        source_id
        for source_id, record in records().items()
        if any(
            event["event_type"] == "PROJECT_LEAD_REVIEW_DECISION"
            and event["evidence_path"] == "reports/SOURCE_FEASIBILITY_REVIEW_PACKET_V0_1.md"
            for event in record["review_history"]
        )
    }
    assert len(initial) == 19
    assert len(reviewed) == 34
    assert set(ledger["pending_project_lead_source_review"]) == {
        "mit_ayiti_resources", "mspp_publications"
    }
    assert ledger["outside_project_lead_review_scope"] == ["aya_collection_haitian"]


def test_human_and_implementation_events_cannot_be_conflated():
    record = records()["cmu_haitian"]
    human = next(e for e in record["review_history"] if e["event_type"] == "PROJECT_LEAD_REVIEW_DECISION")
    implementation = next(e for e in record["review_history"] if e["event_type"] == "IMPLEMENTATION_EVIDENCE_CHECK")
    assert human["actor"] == "Jeff Pierre"
    assert human["human_attestation"] is True
    assert human["independence"] == "INTERNAL_PROJECT_LEAD"
    assert implementation["actor"] == "Codex"
    assert implementation["human_attestation"] is False
    assert implementation["ai_assistance_disclosed"] is True

    invalid = dict(record)
    invalid["review_history"] = [dict(event) for event in record["review_history"]]
    invalid["review_history"][-1]["human_attestation"] = True
    with pytest.raises(ValidationError):
        SourceFeasibilityRecord.model_validate(invalid)


def test_pending_sources_have_no_project_lead_event_or_false_attribution():
    for source_id in ["mit_ayiti_resources", "mspp_publications"]:
        assert records()[source_id]["assessment_axes"]["scientific_feasibility"] == "PENDING_PROJECT_LEAD_REVIEW"
        assert not any(
            event["event_type"] == "PROJECT_LEAD_REVIEW_DECISION"
            for event in records()[source_id]["review_history"]
        )
        report = (ROOT / records()[source_id]["evidence_path"]).read_text(encoding="utf-8")
        assert "Project-Lead Review Event" not in report


def test_feasibility_changes_no_authorization_or_release_gate():
    for source_id, source in sources().items():
        if source_id == "sample":
            continue
        governance = source.source_governance
        assert source.release_candidate is False
        assert governance.collection_status.value != "APPROVED"
        assert governance.derived_use_status.value != "APPROVED"
        assert governance.redistribution_status.value != "APPROVED"
        assert governance.scientific_status.value not in {"PILOT_ONLY", "APPROVED"}
    assert audit_repository(ROOT).release_eligible is False


def test_portal_and_aggregator_evidence_does_not_propagate_rights():
    registry = sources()
    portal = registry["haiti_government_communication_portal"]
    assert portal.source_governance.legal_review_status.value == "PENDING"
    assert portal.source_governance.collection_status.value == "PERMISSION_UNKNOWN"
    for source_id in ["creoleval", "opus", "jhu_kreyol_mt"]:
        source = registry[source_id]
        assert source.source_governance.redistribution_status.value != "APPROVED"
        assert records()[source_id]["external_evidence_required"]


def test_treebank_archive_and_snapshot_hierarchies_remain_distinct():
    registry = sources()
    assert registry["ud_haitian_adolphe"].parent_source_id == "universal_dependencies_haitian"
    assert registry["ud_haitian_autogramm"].parent_source_id == "universal_dependencies_haitian"
    assert registry["radio_haiti_inter_lrec2026"].parent_source_id == "radio_haiti_duke_archive"
    assert registry["wikimedia_htwiki_20231101"].parent_source_id == "wikimedia_htwiki"


def test_planning_ledgers_cover_every_non_synthetic_source():
    expected = set(sources()) - {"sample"}
    ledgers = [
        SourcePriorityLedger.model_validate(load(ROOT / "configs/governance/source_prioritization.yaml")),
        SourceDiversityLedger.model_validate(load(ROOT / "configs/governance/source_diversity.yaml")),
    ]
    for ledger in ledgers:
        assert {entry.source_id for entry in ledger.entries} == expected
        assert ledger.release_candidate is False
    expected_refs = {f"source:{source_id}" for source_id in expected}
    discovery = load(ROOT / "configs/governance/source_discovery.yaml")
    expected_refs |= {
        f"lead:{lead['lead_id']}" for lead in discovery["leads"] if lead["source_id"] is None
    }
    for ledger in [
        SourceContaminationLedger.model_validate(
            load(ROOT / "configs/governance/source_contamination.yaml")
        ),
        SourceUseLedger.model_validate(load(ROOT / "configs/governance/source_use.yaml")),
    ]:
        assert {entry.resource_ref for entry in ledger.entries} == expected_refs
        assert ledger.release_candidate is False


def test_contamination_unknown_is_not_contamination_free():
    ledger = load(ROOT / "configs/governance/source_contamination.yaml")
    statuses = {entry["resource_ref"]: entry["status"] for entry in ledger["entries"]}
    for source_id in [
        "wikimedia_htwiki", "ebible_hat_1985", "opus", "creoleval",
        "jhu_kreyol_mt", "universal_dependencies_haitian",
    ]:
        assert statuses[f"source:{source_id}"] == "ELEVATED_RISK"
    assert "CONTAMINATION_FREE" not in (ROOT / "configs/governance/source_contamination.yaml").read_text()


def test_packet_and_reports_preserve_attribution_and_no_authorization():
    packet = (ROOT / "reports/SOURCE_FEASIBILITY_REVIEW_PACKET_V0_1.md").read_text()
    assert "ACCEPT WITH REQUIRED CORRECTIONS" in packet
    assert "ORIGINAL_CODEX_METADATA_ASSESSMENT" in packet
    assert "PROJECT_LEAD_REVIEW_DECISION" in packet
    assert "IMPLEMENTATION_EVIDENCE_CHECK" in packet
    assert "release_eligible` remains false" in packet
    reviewed_reports = [
        ROOT / record["evidence_path"]
        for record in records().values()
        if any(event["event_type"] == "PROJECT_LEAD_REVIEW_DECISION" for event in record["review_history"])
    ]
    assert len(reviewed_reports) == 34
    assert all(path.is_file() for path in reviewed_reports)
