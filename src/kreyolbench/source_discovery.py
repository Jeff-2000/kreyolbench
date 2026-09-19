"""Open-world, metadata-only intake with no implicit dataset authorization."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, ValidationError, model_validator

from kreyolbench.governance import (
    DecisionRecord,
    DomainRecord,
    GovernedArtifact,
    GovernanceAudit,
    MetadataClaim,
    ReviewStatus,
    SourceReviewEvent,
    SourceRecord,
    TaskFamilyRecord,
    TaskInstanceRecord,
    _load_mapping,
    _validate_governed_artifact,
    _validation_message,
)
from kreyolbench.schemas import ContentOrigin


class ReportedSize(BaseModel):
    """An attributed upstream count; never an independently measured corpus size."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    value: float = Field(ge=0, allow_inf_nan=False)
    unit: Literal["ROWS", "DOCUMENTS", "SENTENCES", "HOURS", "IMAGES"]
    configuration: str = Field(min_length=1)
    split: str = Field(min_length=1)
    revision: str = Field(min_length=1)
    verification_state: Literal["UPSTREAM_REPORTED", "USER_REPORTED_UNVERIFIED"]
    evidence: MetadataClaim
    notes: str = Field(min_length=1)


class DiscoveryLead(BaseModel):
    """A source, an unresolved lead, or a reference, independently of release scope."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    lead_id: str = Field(pattern=r"^[a-z][a-z0-9_]*$")
    name: str = Field(min_length=1)
    canonical_url: HttpUrl
    configuration: str = Field(min_length=1)
    revision: str = Field(min_length=1)
    discovery_attribution: list[str] = Field(min_length=1)
    disposition: Literal["REGISTERED_SOURCE", "UNVERIFIED_LEAD", "REFERENCE_ONLY"]
    source_id: str | None
    language_evidence: Literal["DOCUMENTED", "CLAIMED", "UNKNOWN", "NOT_DOCUMENTED"]
    language_claims: list[MetadataClaim]
    roles: list[Literal[
        "BENCHMARK_EVALUATION_REFERENCE", "BENCHMARK_COMPARISON_REFERENCE",
        "GOLD_DATA_CANDIDATE", "CORPUS_CANDIDATE", "PRETRAINING_CANDIDATE",
        "INSTRUCTION_TUNING_CANDIDATE", "CONTAMINATION_REFERENCE",
        "LINGUISTIC_REFERENCE", "SPEECH_RESOURCE", "RESTRICTED_RESEARCH_RESOURCE",
        "DISCOVERY_ONLY", "MIRROR_REFERENCE", "MULTIMODAL_METHODOLOGY_REFERENCE",
        "MACHINE_TRANSLATED_EVALUATION_REFERENCE",
    ]] = Field(min_length=1)
    content_origin: ContentOrigin
    origin_evidence: list[MetadataClaim]
    modalities: list[str] = Field(min_length=1)
    candidate_domain_ids: list[str]
    candidate_task_family_ids: list[str]
    candidate_task_instance_ids: list[str]
    reported_sizes: list[ReportedSize] = Field(default_factory=list)
    evidence_path: str = Field(min_length=1)
    review_status: Literal["SUBMITTED_TO_REVIEW", "BLOCKED"]
    reviewed_on: date
    unresolved_claims: list[str] = Field(min_length=1)
    next_action: str = Field(min_length=1)
    authorization_effect: Literal["NONE"]
    review_history: list[SourceReviewEvent] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_disposition(self) -> "DiscoveryLead":
        if (self.disposition == "REGISTERED_SOURCE") != (self.source_id is not None):
            raise ValueError("only REGISTERED_SOURCE must reference a source_id")
        if self.disposition == "REGISTERED_SOURCE" and self.language_evidence != "DOCUMENTED":
            raise ValueError("source registration requires documented Haitian-language evidence")
        if self.language_evidence == "DOCUMENTED" and not any(
            claim.basis == "DIRECT_FACT" for claim in self.language_claims
        ):
            raise ValueError("DOCUMENTED language coverage requires direct evidence")
        if self.content_origin != ContentOrigin.UNKNOWN and not self.origin_evidence:
            raise ValueError("non-UNKNOWN content origin requires evidence")
        if self.reviewed_on > date.today():
            raise ValueError("discovery review date cannot be in the future")
        for claim in [*self.language_claims, *self.origin_evidence,
                      *(size.evidence for size in self.reported_sizes)]:
            if claim.accessed_on > self.reviewed_on:
                raise ValueError("discovery evidence cannot postdate its review")
        for values in [self.roles, self.modalities, self.candidate_domain_ids,
                       self.candidate_task_family_ids, self.candidate_task_instance_ids]:
            if len(values) != len(set(values)):
                raise ValueError("discovery lists must contain unique values")
        return self


class SourceRelationship(BaseModel):
    """Evidence-backed provenance edges; none transfer rights or approval."""

    model_config = ConfigDict(extra="forbid")

    from_source_id: str
    to_source_id: str
    relation: Literal["SNAPSHOT_OF", "CLAIMED_DERIVATIVE_OF", "HOSTED_WITHIN",
                      "ORIGINATES_FROM", "POSSIBLE_SHARED_UPSTREAM"]
    evidence: MetadataClaim
    authorization_effect: Literal["NONE"]


class DiscoveryIntake(BaseModel):
    """Immutable intake coverage, distinct from subsequent disposition changes."""

    model_config = ConfigDict(extra="forbid")

    intake_id: str
    received_on: date
    supplied_by: str
    lead_ids: list[str] = Field(min_length=1)


class SourceDiscoveryLedger(GovernedArtifact):
    """Extensible source discovery; families and domains remain config-driven."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[2]
    open_world: Literal[True]
    ai_assistance_disclosed: Literal[True]
    authorization_effect: Literal["NONE"]
    intakes: list[DiscoveryIntake] = Field(min_length=1)
    leads: list[DiscoveryLead] = Field(min_length=1)
    relationships: list[SourceRelationship]

    @model_validator(mode="after")
    def validate_inventory(self) -> "SourceDiscoveryLedger":
        if self.status != ReviewStatus.SUBMITTED_TO_REVIEW or self.release_candidate:
            raise ValueError("discovery ledger must remain non-release SUBMITTED_TO_REVIEW")
        ids = [lead.lead_id for lead in self.leads]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate discovery lead ID")
        identities = [(str(lead.canonical_url), lead.configuration, lead.revision)
                      for lead in self.leads]
        if len(identities) != len(set(identities)):
            raise ValueError("duplicate canonical resource/configuration/revision")
        sources = [lead.source_id for lead in self.leads if lead.source_id is not None]
        if len(sources) != len(set(sources)):
            raise ValueError("repeated source registrations must resolve to one discovery lead")
        intake_ids = [intake.intake_id for intake in self.intakes]
        if len(intake_ids) != len(set(intake_ids)):
            raise ValueError("duplicate intake ID")
        covered = set()
        for intake in self.intakes:
            if intake.received_on > date.today():
                raise ValueError("intake date cannot be in the future")
            if len(intake.lead_ids) != len(set(intake.lead_ids)):
                raise ValueError("duplicate intake lead ID")
            covered.update(intake.lead_ids)
        if covered != set(ids):
            raise ValueError("intake coverage must match discovery lead IDs exactly")
        edges = [(edge.from_source_id, edge.to_source_id, edge.relation)
                 for edge in self.relationships]
        if len(edges) != len(set(edges)):
            raise ValueError("duplicate source relationship")
        if any(edge.from_source_id == edge.to_source_id for edge in self.relationships):
            raise ValueError("source relationship cannot reference itself")
        return self


def audit_source_discovery(
    root: Path,
    sources: dict[str, SourceRecord],
    taxonomy: dict[str, TaskFamilyRecord],
    domains: dict[str, DomainRecord],
    tasks: dict[str, TaskInstanceRecord],
    decisions: dict[str, DecisionRecord],
    audit: GovernanceAudit,
) -> None:
    """Audit references without network calls or source-status mutation."""
    path = root / "configs/governance/source_discovery.yaml"
    payload = _load_mapping(path, root, audit)
    if payload is None:
        return
    try:
        ledger = SourceDiscoveryLedger.model_validate(payload)
    except ValidationError as exc:
        audit.errors.append(f"configs/governance/source_discovery.yaml: {_validation_message(exc)}")
        return
    _validate_governed_artifact(payload, path, root, decisions, audit)
    for lead in ledger.leads:
        if lead.source_id is not None and lead.source_id not in sources:
            audit.errors.append(f"discovery {lead.lead_id}: unknown source_id {lead.source_id}")
        for values, registry, label in [
            (lead.candidate_task_family_ids, taxonomy, "task family"),
            (lead.candidate_task_instance_ids, tasks, "task instance"),
            (lead.candidate_domain_ids, domains, "domain"),
        ]:
            for value in sorted(set(values) - set(registry)):
                audit.errors.append(f"discovery {lead.lead_id}: unknown {label} {value}")
        evidence_path = (root / lead.evidence_path).resolve()
        if not evidence_path.is_relative_to(root) or not evidence_path.is_file():
            audit.errors.append(f"discovery {lead.lead_id}: evidence_path must exist inside repository")
        if lead.disposition == "UNVERIFIED_LEAD":
            audit.blocked_components.append(f"discovery: {lead.lead_id} remains unverified")
    for edge in ledger.relationships:
        for source_id in [edge.from_source_id, edge.to_source_id]:
            if source_id not in sources:
                audit.errors.append(f"discovery relationship: unknown source_id {source_id}")
