"""Expanded source review enforces use firewalls without granting authorization."""

from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from kreyolbench.governance import SourceRecord
from kreyolbench.schemas import CaptionProvenance, MultimodalProvenance
from kreyolbench.source_assessments import (
    SourceContaminationLedger,
    SourceDiversityLedger,
    SourceUseLedger,
)


ROOT = Path(__file__).parents[1]


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_source_use_and_contamination_cover_registry_and_open_leads():
    sources = {
        load(path)["source_id"]
        for path in (ROOT / "configs/sources").glob("*.yaml")
    } - {"sample"}
    discovery = load(ROOT / "configs/governance/source_discovery.yaml")
    leads = {
        lead["lead_id"] for lead in discovery["leads"] if lead["source_id"] is None
    }
    expected = {f"source:{source_id}" for source_id in sources} | {
        f"lead:{lead_id}" for lead_id in leads
    }
    for ledger in [
        SourceUseLedger.model_validate(load(ROOT / "configs/governance/source_use.yaml")),
        SourceContaminationLedger.model_validate(
            load(ROOT / "configs/governance/source_contamination.yaml")
        ),
    ]:
        assert {entry.resource_ref for entry in ledger.entries} == expected


def test_protected_evaluation_resources_are_training_prohibited():
    use = SourceUseLedger.model_validate(load(ROOT / "configs/governance/source_use.yaml"))
    records = {entry.resource_ref: entry for entry in use.entries}
    for source_id in ["flores_plus_hat", "creoleval"]:
        record = records[f"source:{source_id}"]
        assert record.evaluation_eligibility.value == "PROTECTED_REFERENCE"
        assert record.training_eligibility.value == "PROHIBITED"


def test_restricted_and_mirror_resources_cannot_override_parent_rights():
    registry = {
        load(path)["source_id"]: SourceRecord.model_validate(load(path))
        for path in (ROOT / "configs/sources").glob("*.yaml")
    }
    mirror = registry["cmu_haitian_phatjmo"]
    restricted = registry["mission_4636_restricted_sensitive"]
    assert mirror.parent_source_id == "cmu_haitian"
    assert mirror.source_governance.redistribution_status.value != "APPROVED"
    assert restricted.parent_source_id == "haitian_disaster_sms_munro"
    assert restricted.source_governance.collection_status.value == "PROHIBITED"
    assert restricted.source_governance.redistribution_status.value == "PROHIBITED"
    assert not mirror.release_candidate and not restricted.release_candidate


def test_frozen_release_source_requires_immutable_version_and_hash():
    source = load(ROOT / "configs/sources/wikimedia_htwiki_20231101.yaml")
    source["release_candidate"] = True
    source["source_version"] = None
    source["hash"] = None
    with pytest.raises(ValidationError, match="immutable source_version and hash"):
        SourceRecord.model_validate(source)


def test_registered_speech_transitions_and_mission_children_are_explicit():
    discovery = load(ROOT / "configs/governance/source_discovery.yaml")
    leads = {lead["lead_id"]: lead for lead in discovery["leads"]}
    assert leads["voxlingua107_hat"]["source_id"] == "voxlingua107_hat"
    assert leads["northern_haitian"]["source_id"] == "northern_haitian_creole_corpus"
    sources = {load(path)["source_id"]: load(path) for path in (ROOT / "configs/sources").glob("*.yaml")}
    assert sources["haitian_disaster_sms_munro"]["record_type"] == "SOURCE_FAMILY"
    for child in ["mission_4636_open_nonsensitive", "mission_4636_restricted_sensitive"]:
        assert sources[child]["parent_source_id"] == "haitian_disaster_sms_munro"


def test_multimodal_machine_translation_requires_origin_and_model():
    with pytest.raises(ValidationError, match="original_language and translation_model"):
        CaptionProvenance.model_validate(
            {
                "caption_id": "c1",
                "language": "hat",
                "authoring_origin": "MACHINE_TRANSLATED",
                "human_validation_status": "NOT_VALIDATED",
            }
        )


def test_multimodal_media_and_caption_ids_must_resolve_independently():
    payload = {
        "media": {
            "media_id": "m1",
            "original_source": "provider",
            "license_or_terms": "TO_VERIFY",
            "version_or_hash": "sha256:media",
        },
        "caption": {
            "caption_id": "c1",
            "language": "hat",
            "authoring_origin": "MACHINE_TRANSLATED",
            "original_language": "eng",
            "translation_model": "model-id",
            "human_validation_status": "NOT_VALIDATED",
        },
        "linkage": {
            "media_id": "wrong",
            "caption_id": "c1",
            "parent_dataset": "methodology-reference",
            "transformation_history": [],
            "split": "reference",
            "contamination_status": "NOT_ASSESSED",
        },
    }
    with pytest.raises(ValidationError, match="linkage media_id"):
        MultimodalProvenance.model_validate(payload)


def test_native_haitian_multimodal_coverage_remains_an_evidence_gap():
    ledger = SourceDiversityLedger.model_validate(
        load(ROOT / "configs/governance/source_diversity.yaml")
    )
    assert ledger.evidence_gaps == ["NATIVE_HAITIAN_CREOLE_VISION_LANGUAGE_DATA"]
    discovery = load(ROOT / "configs/governance/source_discovery.yaml")
    refs = {lead["lead_id"]: lead for lead in discovery["leads"]}
    assert refs["xm3600"]["disposition"] == "REFERENCE_ONLY"
    assert refs["vicr_translated"]["disposition"] == "UNVERIFIED_LEAD"
