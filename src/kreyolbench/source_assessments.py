"""Cross-source planning, diversity, and contamination governance.

These ledgers are metadata-only planning instruments. They cannot authorize source use.
"""

from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from kreyolbench.governance import (
    DecisionRecord,
    EvidenceState,
    GovernedArtifact,
    GovernanceAudit,
    SourceRecord,
)
from kreyolbench.registry import load_yaml
from kreyolbench.schemas import ContentOrigin


class SourcePriorityTier(str, Enum):
    HIGH_PRIORITY_NEXT_STAGE_REVIEW = "HIGH_PRIORITY_NEXT_STAGE_REVIEW"
    COMPARISON_CONTAMINATION_FUTURE_INFRASTRUCTURE = (
        "COMPARISON_CONTAMINATION_FUTURE_INFRASTRUCTURE"
    )
    DISCOVERY_FUTURE_GOVERNANCE_REQUIRED = "DISCOVERY_FUTURE_GOVERNANCE_REQUIRED"
    PENDING_PROJECT_LEAD_REVIEW = "PENDING_PROJECT_LEAD_REVIEW"
    NOT_IN_PROJECT_LEAD_REVIEW_SCOPE = "NOT_IN_PROJECT_LEAD_REVIEW_SCOPE"


class SourceRole(str, Enum):
    """Scientific use role, independent of authorization and release status."""

    BENCHMARK_EVALUATION_REFERENCE = "BENCHMARK_EVALUATION_REFERENCE"
    BENCHMARK_COMPARISON_REFERENCE = "BENCHMARK_COMPARISON_REFERENCE"
    GOLD_DATA_CANDIDATE = "GOLD_DATA_CANDIDATE"
    CORPUS_CANDIDATE = "CORPUS_CANDIDATE"
    PRETRAINING_CANDIDATE = "PRETRAINING_CANDIDATE"
    INSTRUCTION_TUNING_CANDIDATE = "INSTRUCTION_TUNING_CANDIDATE"
    CONTAMINATION_REFERENCE = "CONTAMINATION_REFERENCE"
    LINGUISTIC_REFERENCE = "LINGUISTIC_REFERENCE"
    SPEECH_RESOURCE = "SPEECH_RESOURCE"
    RESTRICTED_RESEARCH_RESOURCE = "RESTRICTED_RESEARCH_RESOURCE"
    DISCOVERY_ONLY = "DISCOVERY_ONLY"
    MIRROR_REFERENCE = "MIRROR_REFERENCE"
    MULTIMODAL_METHODOLOGY_REFERENCE = "MULTIMODAL_METHODOLOGY_REFERENCE"
    MACHINE_TRANSLATED_EVALUATION_REFERENCE = (
        "MACHINE_TRANSLATED_EVALUATION_REFERENCE"
    )


class TrainingEligibility(str, Enum):
    PROHIBITED = "PROHIBITED"
    REQUIRES_REVIEW = "REQUIRES_REVIEW"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class EvaluationEligibility(str, Enum):
    PROTECTED_REFERENCE = "PROTECTED_REFERENCE"
    REQUIRES_REVIEW = "REQUIRES_REVIEW"
    PROHIBITED = "PROHIBITED"
    REFERENCE_ONLY = "REFERENCE_ONLY"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class SourceUseRecord(BaseModel):
    """Scientific role and use eligibility without granting permission."""

    model_config = ConfigDict(extra="forbid")

    resource_ref: str = Field(pattern=r"^(source|lead):[a-z][a-z0-9_]*$")
    resource_kind: Literal["REGISTERED_SOURCE", "UNVERIFIED_LEAD", "REFERENCE_ONLY"]
    roles: list[SourceRole] = Field(min_length=1)
    training_eligibility: TrainingEligibility
    evaluation_eligibility: EvaluationEligibility
    evidence_path: str = Field(min_length=1)
    rationale: str = Field(min_length=1)
    authorization_effect: Literal["NONE"]

    @model_validator(mode="after")
    def validate_non_authorizing_use(self) -> "SourceUseRecord":
        if len(self.roles) != len(set(self.roles)):
            raise ValueError("source roles must be unique")
        if (
            self.evaluation_eligibility == EvaluationEligibility.PROTECTED_REFERENCE
            and self.training_eligibility != TrainingEligibility.PROHIBITED
        ):
            raise ValueError("protected evaluation resources must prohibit training use")
        if (
            self.resource_kind != "REGISTERED_SOURCE"
            and self.resource_ref.startswith("source:")
        ):
            raise ValueError("nonregistered resources must use lead: references")
        return self


class SourceUseLedger(GovernedArtifact):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[1]
    entries: list[SourceUseRecord]


PRIORITY_DIMENSIONS = {
    "native_haitian_creole_value",
    "linguistic_authenticity",
    "domain_diversity",
    "register_diversity",
    "temporal_diversity",
    "geographic_diaspora_diversity",
    "spoken_language_value",
    "code_switching_value",
    "orthographic_value",
    "task_relevance",
    "provenance_quality",
    "rights_clarity",
    "ethics_burden",
    "contamination_assessability",
    "long_term_infrastructure_value",
}


class SourcePriorityRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_id: str
    tier: SourcePriorityTier
    dimensions: dict[str, EvidenceState]
    rationale: str = Field(min_length=1)
    authorization_effect: Literal["NONE"]

    @model_validator(mode="after")
    def validate_dimensions(self) -> "SourcePriorityRecord":
        if set(self.dimensions) != PRIORITY_DIMENSIONS:
            raise ValueError("source-priority dimensions must match the governed inventory")
        return self


class SourcePriorityLedger(GovernedArtifact):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[1]
    entries: list[SourcePriorityRecord]


class SourceDiversityRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_id: str
    domains: list[str] = Field(min_length=1)
    registers: list[str] = Field(min_length=1)
    origins: list[ContentOrigin] = Field(min_length=1)
    modalities: list[
        Literal["TEXT", "SPEECH_AUDIO", "IMAGE_TEXT", "DOCUMENT_OCR", "MULTIMODAL", "OTHER"]
    ] = Field(min_length=1)
    temporal_periods: list[str] = Field(min_length=1)
    geographies: list[Literal["HAITI", "DIASPORA", "HAITI_AND_DIASPORA", "UNKNOWN"]]
    multimodal_origin: Literal[
        "NATIVE_HAITIAN_MULTIMODAL",
        "TRANSLATED_TO_HAITIAN_MULTIMODAL",
        "MULTILINGUAL_HAITIAN_UNVERIFIED",
        "METHODOLOGY_REFERENCE_ONLY",
        "NOT_MULTIMODAL",
        "UNKNOWN",
    ]
    evidence_state: EvidenceState
    limitations: list[str] = Field(min_length=1)
    authorization_effect: Literal["NONE"]

    @model_validator(mode="after")
    def validate_unique_values(self) -> "SourceDiversityRecord":
        for values in (
            self.domains,
            self.registers,
            self.origins,
            self.modalities,
            self.temporal_periods,
            self.geographies,
        ):
            if len(values) != len(set(values)):
                raise ValueError("source-diversity values must be unique")
        return self


class SourceDiversityLedger(GovernedArtifact):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[2]
    entries: list[SourceDiversityRecord]
    evidence_gaps: list[Literal["NATIVE_HAITIAN_CREOLE_VISION_LANGUAGE_DATA"]]


class ContaminationState(str, Enum):
    ELEVATED_RISK = "ELEVATED_RISK"
    KNOWN_OVERLAP = "KNOWN_OVERLAP"
    CONTAMINATION_NOT_ESTABLISHED = "CONTAMINATION_NOT_ESTABLISHED"
    NOT_ASSESSED = "NOT_ASSESSED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class SourceContaminationRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    resource_ref: str = Field(pattern=r"^(source|lead):[a-z][a-z0-9_]*$")
    resource_kind: Literal["REGISTERED_SOURCE", "UNVERIFIED_LEAD", "REFERENCE_ONLY"]
    subset: str = Field(min_length=1)
    revision: str = Field(min_length=1)
    protected_splits: list[str]
    parent_resource_refs: list[str]
    derived_resource_refs: list[str]
    possible_overlap_refs: list[str]
    training_status: TrainingEligibility
    status: ContaminationState
    evidence_state: EvidenceState
    rationale: list[str] = Field(min_length=1)
    required_provenance: list[str] = Field(min_length=1)
    authorization_effect: Literal["NONE"]

    @model_validator(mode="after")
    def prohibit_unsupported_clean_claims(self) -> "SourceContaminationRecord":
        if "CONTAMINATION_FREE" in " ".join(self.rationale).upper():
            raise ValueError("CONTAMINATION_FREE is not an allowed unsupported claim")
        linked = [
            *self.parent_resource_refs,
            *self.derived_resource_refs,
            *self.possible_overlap_refs,
        ]
        if self.resource_ref in linked:
            raise ValueError("a resource cannot reference itself as contamination lineage")
        for values in (
            self.protected_splits,
            self.parent_resource_refs,
            self.derived_resource_refs,
            self.possible_overlap_refs,
        ):
            if len(values) != len(set(values)):
                raise ValueError("contamination lists must contain unique values")
        if self.protected_splits and self.training_status != TrainingEligibility.PROHIBITED:
            raise ValueError("protected splits must prohibit training use")
        return self


class SourceContaminationLedger(GovernedArtifact):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[2]
    entries: list[SourceContaminationRecord]


def _load_model(path: Path, model: type[BaseModel], root: Path, audit: GovernanceAudit):
    try:
        payload = load_yaml(path)
        return model.model_validate(payload)
    except (OSError, ValueError, ValidationError) as exc:
        audit.errors.append(f"{path.relative_to(root)}: {exc}")
        return None


def _validate_coverage(entries, expected: set[str], label: str, audit: GovernanceAudit) -> None:
    ids = [
        entry.source_id if hasattr(entry, "source_id") else entry.resource_ref
        for entry in entries
    ]
    if len(ids) != len(set(ids)):
        audit.errors.append(f"{label}: duplicate source ID")
    if set(ids) != expected:
        audit.errors.append(
            f"{label}: coverage mismatch; expected={sorted(expected)}, actual={sorted(set(ids))}"
        )


def audit_source_assessments(
    root: Path,
    sources: dict[str, SourceRecord],
    decisions: dict[str, DecisionRecord],
    audit: GovernanceAudit,
) -> None:
    """Validate non-authoritative planning ledgers and cross-source references."""

    expected = set(sources) - {"sample"}
    discovery_payload = load_yaml(root / "configs/governance/source_discovery.yaml")
    nonregistered_leads = {
        lead["lead_id"]: lead["disposition"]
        for lead in discovery_payload.get("leads", [])
        if lead.get("source_id") is None
    }
    expected_resource_refs = {f"source:{source_id}" for source_id in expected} | {
        f"lead:{lead_id}" for lead_id in nonregistered_leads
    }
    priority = _load_model(
        root / "configs/governance/source_prioritization.yaml",
        SourcePriorityLedger,
        root,
        audit,
    )
    diversity = _load_model(
        root / "configs/governance/source_diversity.yaml",
        SourceDiversityLedger,
        root,
        audit,
    )
    contamination = _load_model(
        root / "configs/governance/source_contamination.yaml",
        SourceContaminationLedger,
        root,
        audit,
    )
    source_use = _load_model(
        root / "configs/governance/source_use.yaml",
        SourceUseLedger,
        root,
        audit,
    )
    if priority:
        _validate_coverage(priority.entries, expected, "source prioritization", audit)
    if diversity:
        _validate_coverage(diversity.entries, expected, "source diversity", audit)
    if contamination:
        _validate_coverage(
            contamination.entries,
            expected_resource_refs,
            "source contamination",
            audit,
        )
        known_refs = expected_resource_refs
        for entry in contamination.entries:
            linked = {
                *entry.parent_resource_refs,
                *entry.derived_resource_refs,
                *entry.possible_overlap_refs,
            }
            unknown = linked - known_refs
            if unknown:
                audit.errors.append(
                    f"source contamination {entry.resource_ref}: unknown references {sorted(unknown)}"
                )
    if source_use:
        _validate_coverage(source_use.entries, expected_resource_refs, "source use", audit)
        for entry in source_use.entries:
            expected_kind = (
                "REGISTERED_SOURCE"
                if entry.resource_ref.startswith("source:")
                else nonregistered_leads[entry.resource_ref.removeprefix("lead:")]
            )
            if entry.resource_kind != expected_kind:
                audit.errors.append(
                    f"source use {entry.resource_ref}: expected resource kind {expected_kind}"
                )
            evidence = root / entry.evidence_path
            if not evidence.is_file() or root.resolve() not in evidence.resolve().parents:
                audit.errors.append(
                    f"source use {entry.resource_ref}: invalid evidence path {entry.evidence_path}"
                )
    for label, ledger in (
        ("source prioritization", priority),
        ("source diversity", diversity),
        ("source contamination", contamination),
        ("source use", source_use),
    ):
        if ledger is None:
            continue
        if ledger.release_candidate or ledger.status.value != "SUBMITTED_TO_REVIEW":
            audit.errors.append(f"{label}: planning ledger must remain non-release SUBMITTED_TO_REVIEW")
        missing = sorted(set(ledger.decision_ids) - set(decisions))
        if missing:
            audit.errors.append(f"{label}: unknown decision references {missing}")
