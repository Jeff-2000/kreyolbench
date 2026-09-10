"""Machine-readable governance and scientific-invariant audits.

The audit deliberately separates structural validity from scientific approval.
A repository can pass structural validation while remaining ineligible for release.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from kreyolbench.io import read_jsonl
from kreyolbench.registry import load_yaml
from kreyolbench.schemas import (
    KreyolBenchRow,
    validate_retrieval_document,
    validate_retrieval_qrel,
    validate_retrieval_query,
    validate_row,
)


class ReviewStatus(str, Enum):
    """Allowed lifecycle states for scientific and engineering artifacts."""

    DRAFT = "DRAFT"
    IN_PROGRESS = "IN_PROGRESS"
    TO_REVIEW_LATER = "TO_REVIEW_LATER"
    SUBMITTED_TO_REVIEW = "SUBMITTED_TO_REVIEW"
    EXPERT_VALIDATED = "EXPERT_VALIDATED"
    NEEDS_REVISION = "NEEDS_REVISION"
    BLOCKED = "BLOCKED"
    DEPRECATED = "DEPRECATED"


class ScopeStatus(str, Enum):
    """Planning or release scope, independent of scientific review status."""

    ROADMAP = "ROADMAP"
    DISCOVERY = "DISCOVERY"
    FEASIBILITY_ONLY = "FEASIBILITY_ONLY"
    PILOT_CANDIDATE = "PILOT_CANDIDATE"
    RELEASE_CANDIDATE = "RELEASE_CANDIDATE"
    DEFERRED = "DEFERRED"
    INCLUDED_IN_RELEASE = "INCLUDED_IN_RELEASE"


class ReviewOutcome(str, Enum):
    """Outcome recorded for one human review event."""

    APPROVED = "APPROVED"
    REVISED = "REVISED"
    DEFERRED = "DEFERRED"


class ReviewIndependence(str, Enum):
    """Relationship between a reviewer and the artifact under review."""

    INTERNAL_PROJECT_LEAD = "INTERNAL_PROJECT_LEAD"
    INTERNAL_NON_AUTHOR = "INTERNAL_NON_AUTHOR"
    EXTERNAL_INDEPENDENT = "EXTERNAL_INDEPENDENT"


class ConflictStatus(str, Enum):
    """Conflict disclosure outcome for a scientific review event."""

    NONE_DECLARED = "NONE_DECLARED"
    DISCLOSED_MANAGED = "DISCLOSED_MANAGED"
    DISQUALIFYING = "DISQUALIFYING"


UNRESOLVED_STATUSES = {
    ReviewStatus.DRAFT,
    ReviewStatus.IN_PROGRESS,
    ReviewStatus.TO_REVIEW_LATER,
    ReviewStatus.SUBMITTED_TO_REVIEW,
    ReviewStatus.NEEDS_REVISION,
    ReviewStatus.BLOCKED,
}


class SourceRecordType(str, Enum):
    """Granularity of an entry in the open-world source registry."""

    SOURCE_FAMILY = "SOURCE_FAMILY"
    SOURCE_COLLECTION = "SOURCE_COLLECTION"
    SOURCE_SUBSET = "SOURCE_SUBSET"


class DiscoveryStatus(str, Enum):
    DISCOVERED = "DISCOVERED"
    ENDPOINT_VERIFIED = "ENDPOINT_VERIFIED"
    INACCESSIBLE = "INACCESSIBLE"
    RETIRED = "RETIRED"


class AccessStatus(str, Enum):
    UNKNOWN = "UNKNOWN"
    ACCESSIBLE_FOR_REVIEW = "ACCESSIBLE_FOR_REVIEW"
    RESTRICTED = "RESTRICTED"
    UNAVAILABLE = "UNAVAILABLE"


class LegalReviewStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    CONDITIONAL = "CONDITIONAL"
    REJECTED = "REJECTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class CollectionStatus(str, Enum):
    NOT_REQUESTED = "NOT_REQUESTED"
    PERMISSION_UNKNOWN = "PERMISSION_UNKNOWN"
    APPROVED = "APPROVED"
    PROHIBITED = "PROHIBITED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class PermissionStatus(str, Enum):
    UNKNOWN = "UNKNOWN"
    APPROVED = "APPROVED"
    CONDITIONAL = "CONDITIONAL"
    PROHIBITED = "PROHIBITED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class RedistributionStatus(str, Enum):
    UNKNOWN = "UNKNOWN"
    APPROVED = "APPROVED"
    LINK_ONLY = "LINK_ONLY"
    DERIVED_ONLY = "DERIVED_ONLY"
    CONDITIONAL = "CONDITIONAL"
    PROHIBITED = "PROHIBITED"


class EthicsStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    RESTRICTED = "RESTRICTED"
    REJECTED = "REJECTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class ScientificInclusionStatus(str, Enum):
    PENDING_EXPERT_REVIEW = "PENDING_EXPERT_REVIEW"
    PILOT_ONLY = "PILOT_ONLY"
    APPROVED = "APPROVED"
    EXCLUDED = "EXCLUDED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class EvidenceState(str, Enum):
    """Strength of evidence available for one feasibility dimension."""

    EVIDENCE_AVAILABLE = "EVIDENCE_AVAILABLE"
    PARTIAL = "PARTIAL"
    MISSING = "MISSING"
    BLOCKED = "BLOCKED"


class FeasibilityConclusion(str, Enum):
    """Non-numeric conclusion for a task feasibility assessment."""

    PILOT_FEASIBLE = "PILOT_FEASIBLE"
    CONDITIONAL = "CONDITIONAL"
    BLOCKED = "BLOCKED"


class SourceReviewAction(str, Enum):
    """Permitted metadata-review next actions; none authorize source use."""

    VERIFY_ENDPOINT = "VERIFY_ENDPOINT"
    VERIFY_LICENSE = "VERIFY_LICENSE"
    VERIFY_RELEASE_ARTIFACT = "VERIFY_RELEASE_ARTIFACT"
    REGISTER_CHILD_COLLECTION = "REGISTER_CHILD_COLLECTION"
    REGISTER_CHILD_SUBSET = "REGISTER_CHILD_SUBSET"
    REQUEST_PERMISSION = "REQUEST_PERMISSION"
    SEEK_LEGAL_REVIEW = "SEEK_LEGAL_REVIEW"
    SEEK_ETHICS_REVIEW = "SEEK_ETHICS_REVIEW"
    SEEK_LINGUISTIC_REVIEW = "SEEK_LINGUISTIC_REVIEW"
    SEEK_SCIENTIFIC_REVIEW = "SEEK_SCIENTIFIC_REVIEW"
    RETAIN_DISCOVERY_ONLY = "RETAIN_DISCOVERY_ONLY"
    DEFER = "DEFER"


class GovernedArtifact(BaseModel):
    """Governance fields embedded in benchmark configuration artifacts."""

    status: ReviewStatus
    decision_ids: list[str]
    requires_expert_validation: bool
    release_candidate: bool


class TaskFamilyRecord(BaseModel):
    """One open-world task family and its currently registered task types."""

    model_config = ConfigDict(extra="forbid")

    family_id: str = Field(pattern=r"^[a-z][a-z0-9_]*$")
    name: str = Field(min_length=1)
    scope_status: ScopeStatus
    modalities: list[str] = Field(min_length=1)
    task_type_ids: list[str] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_unique_values(self) -> "TaskFamilyRecord":
        if len(self.modalities) != len(set(self.modalities)):
            raise ValueError("task-family modalities must be unique")
        if len(self.task_type_ids) != len(set(self.task_type_ids)):
            raise ValueError("task-family task_type_ids must be unique")
        return self


class TaskTaxonomyRecord(GovernedArtifact):
    """Machine-readable open-world task-family registry."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[1]
    open_world: Literal[True]
    task_families: list[TaskFamilyRecord] = Field(min_length=1)


class DomainRecord(BaseModel):
    """One candidate or roadmap domain; registration grants no data rights."""

    model_config = ConfigDict(extra="forbid")

    domain_id: str = Field(pattern=r"^[a-z][a-z0-9_]*$")
    scope_status: ScopeStatus


class DomainRegistryRecord(GovernedArtifact):
    """Open-world domain registry independent of corpus authorization."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[1]
    open_world: Literal[True]
    domains: list[DomainRecord] = Field(min_length=1)


class TaskInstanceRecord(BaseModel):
    """Common governance contract for a concrete task implementation."""

    model_config = ConfigDict(extra="allow")

    task: str = Field(pattern=r"^[a-z][a-z0-9_]*$")
    task_instance_id: str = Field(pattern=r"^kb_[a-z0-9_]+$")
    task_family_id: str = Field(pattern=r"^[a-z][a-z0-9_]*$")
    task_type_id: str = Field(pattern=r"^[a-z][a-z0-9_]*$")
    task_variant: str = Field(pattern=r"^[a-z][a-z0-9_]*$")
    scope_status: ScopeStatus
    scientific_status: ReviewStatus
    decision_ids: list[str]
    requires_expert_validation: bool


class ReleaseTaskMembership(BaseModel):
    """The explicit relationship between one task instance and one release."""

    model_config = ConfigDict(extra="forbid")

    task_instance_id: str = Field(pattern=r"^kb_[a-z0-9_]+$")
    scope_status: ScopeStatus


class ReleaseRecord(BaseModel):
    """A controlled release scope that does not define the global ecosystem."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[1]
    release_id: str = Field(min_length=1)
    version: str = Field(min_length=1)
    scientific_status: ReviewStatus
    scope_status: ScopeStatus
    decision_ids: list[str]
    requires_expert_validation: bool
    task_memberships: list[ReleaseTaskMembership]
    splits: list[str]
    hidden_test_policy: str


class ReviewRequirements(BaseModel):
    """Qualification evidence required before a decision can be validated."""

    model_config = ConfigDict(extra="forbid")

    required_independence: ReviewIndependence
    minimum_external_approvals: int = Field(ge=1)
    required_expertise_tags: list[str] = Field(default_factory=list)
    require_affiliation: bool = True
    require_conflict_disclosure: bool = True

    @model_validator(mode="after")
    def validate_expertise_tags(self) -> "ReviewRequirements":
        if len(self.required_expertise_tags) != len(set(self.required_expertise_tags)):
            raise ValueError("required expertise tags must be unique")
        if not all(re.fullmatch(r"[A-Z][A-Z0-9_]*", tag) for tag in self.required_expertise_tags):
            raise ValueError("required expertise tags must be uppercase identifiers")
        return self


class ReviewEvent(BaseModel):
    """Append-only evidence for a human decision review."""

    model_config = ConfigDict(extra="forbid")

    outcome: ReviewOutcome
    reviewer: str = Field(min_length=1)
    reviewer_role: str = Field(min_length=1)
    reviewer_affiliation: str | None = None
    expertise_tags: list[str] = Field(default_factory=list)
    conflict_status: ConflictStatus | None = None
    conflict_details: str = ""
    human_attestation: bool = False
    reviewed_on: date
    independence: ReviewIndependence
    evidence_path: str = Field(min_length=1)
    notes: str = ""

    @model_validator(mode="after")
    def validate_external_reviewer_evidence(self) -> "ReviewEvent":
        if len(self.expertise_tags) != len(set(self.expertise_tags)):
            raise ValueError("reviewer expertise tags must be unique")
        if not all(re.fullmatch(r"[A-Z][A-Z0-9_]*", tag) for tag in self.expertise_tags):
            raise ValueError("reviewer expertise tags must be uppercase identifiers")
        if self.independence == ReviewIndependence.EXTERNAL_INDEPENDENT:
            if self.reviewer.strip().casefold() in {
                "anonymous",
                "external reviewer",
                "tbd",
                "unknown",
            }:
                raise ValueError("external reviews require an identifiable reviewer")
            if not self.reviewer_affiliation or not self.reviewer_affiliation.strip():
                raise ValueError("external reviews require reviewer_affiliation")
            if not self.expertise_tags:
                raise ValueError("external reviews require expertise_tags")
            if self.conflict_status is None:
                raise ValueError("external reviews require conflict_status")
            if not self.human_attestation:
                raise ValueError("external reviews require human_attestation")
        if self.conflict_status == ConflictStatus.DISCLOSED_MANAGED:
            if not self.conflict_details.strip():
                raise ValueError("managed conflicts require conflict_details")
        if (
            self.outcome == ReviewOutcome.APPROVED
            and self.conflict_status == ConflictStatus.DISQUALIFYING
        ):
            raise ValueError("a disqualifying conflict cannot support approval")
        return self


class DecisionRecord(BaseModel):
    """Machine-readable decision registry entry with review history."""

    model_config = ConfigDict(extra="forbid")

    id: str
    title: str
    status: ReviewStatus
    requires_expert_approval: bool
    review_requirements: ReviewRequirements | None = None
    review_history: list[ReviewEvent] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_review_state(self) -> "DecisionRecord":
        review_dates = [event.reviewed_on for event in self.review_history]
        if review_dates != sorted(review_dates):
            raise ValueError("review history must be chronological")
        if self.status == ReviewStatus.EXPERT_VALIDATED:
            if not self.requires_expert_approval:
                raise ValueError("EXPERT_VALIDATED decisions must require expert approval")
            if not self.review_history:
                raise ValueError("EXPERT_VALIDATED decisions require review history")
            if self.review_history[-1].outcome != ReviewOutcome.APPROVED:
                raise ValueError("EXPERT_VALIDATED decisions require a latest APPROVED review")
            if self.review_requirements is not None:
                requirements = self.review_requirements
                qualifying = [
                    event
                    for event in self.review_history
                    if event.outcome == ReviewOutcome.APPROVED
                    and event.independence == requirements.required_independence
                    and event.conflict_status != ConflictStatus.DISQUALIFYING
                ]
                if len(qualifying) < requirements.minimum_external_approvals:
                    raise ValueError(
                        "EXPERT_VALIDATED decision lacks the required independent approvals"
                    )
                if requirements.require_affiliation and any(
                    not event.reviewer_affiliation for event in qualifying
                ):
                    raise ValueError(
                        "EXPERT_VALIDATED decision lacks required reviewer affiliations"
                    )
                if requirements.require_conflict_disclosure and any(
                    event.conflict_status is None for event in qualifying
                ):
                    raise ValueError(
                        "EXPERT_VALIDATED decision lacks required conflict disclosures"
                    )
                covered_expertise = {
                    tag for event in qualifying for tag in event.expertise_tags
                }
                missing_expertise = sorted(
                    set(requirements.required_expertise_tags) - covered_expertise
                )
                if missing_expertise:
                    raise ValueError(
                        "EXPERT_VALIDATED decision lacks required expertise: "
                        + ", ".join(missing_expertise)
                    )
        if self.status == ReviewStatus.NEEDS_REVISION:
            if not self.review_history or self.review_history[-1].outcome != ReviewOutcome.REVISED:
                raise ValueError("NEEDS_REVISION decisions require a latest REVISED review")
        return self


class SourceGovernanceRecord(BaseModel):
    """Independent legal, ethical, access, and scientific source gates."""

    model_config = ConfigDict(extra="forbid")

    discovery_status: DiscoveryStatus
    access_status: AccessStatus
    legal_review_status: LegalReviewStatus
    collection_status: CollectionStatus
    derived_use_status: PermissionStatus
    redistribution_status: RedistributionStatus
    commercial_use_status: PermissionStatus
    ethics_status: EthicsStatus
    scientific_status: ScientificInclusionStatus
    reviewed_by: str | None = None
    reviewed_on: date | None = None
    evidence_urls: list[str] = Field(default_factory=list)


class SourceRecord(GovernedArtifact):
    """Version 2 source-registry record validated by the governance audit."""

    model_config = ConfigDict(extra="forbid")

    source_schema_version: Literal[2]
    source_id: str
    record_type: SourceRecordType
    parent_source_id: str | None
    name: str
    url: str | None
    provider: str
    publisher_owner: str
    data_type: str
    access_method: str
    license: str
    license_url: str | None
    license_evidence: str
    citation: str
    language_claim: str
    registers: list[str]
    domain: str
    temporal_coverage: str
    geographic_relevance: str
    expected_tasks: list[str]
    accessed_on: date | None
    collection_date: date | None
    hash: str | None
    notes: str
    quality_notes: str
    machine_generated_content_risk: str
    pii_risk: str
    duplication_risk: str
    source_governance: SourceGovernanceRecord


FEASIBILITY_DIMENSIONS = {
    "source_authorization_availability",
    "linguistic_representativeness",
    "annotation_complexity",
    "native_speaker_requirements",
    "schema_readiness",
    "metric_validity",
    "split_contamination_risk",
    "baseline_readiness",
    "compute_requirements",
    "publication_novelty",
    "twelve_month_feasibility",
}


class TaskFeasibilityRecord(BaseModel):
    """Evidence-based, non-numeric task feasibility assessment."""

    model_config = ConfigDict(extra="forbid")

    task_instance_id: str = Field(pattern=r"^kb_[a-z0-9_]+$")
    dimensions: dict[str, EvidenceState]
    overall: FeasibilityConclusion
    source_candidates: list[str]
    blockers: list[str]
    rationale: str

    @model_validator(mode="after")
    def validate_dimensions(self) -> "TaskFeasibilityRecord":
        dimensions = set(self.dimensions)
        if dimensions != FEASIBILITY_DIMENSIONS:
            missing = sorted(FEASIBILITY_DIMENSIONS - dimensions)
            extra = sorted(dimensions - FEASIBILITY_DIMENSIONS)
            raise ValueError(f"feasibility dimensions mismatch; missing={missing}, extra={extra}")
        if self.overall == FeasibilityConclusion.PILOT_FEASIBLE and any(
            state in {EvidenceState.MISSING, EvidenceState.BLOCKED}
            for state in self.dimensions.values()
        ):
            raise ValueError("PILOT_FEASIBLE cannot contain MISSING or BLOCKED evidence")
        return self


class TaskFeasibilityMatrix(GovernedArtifact):
    """Machine-readable feasibility matrix for the v0.1 pilot tasks."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[1]
    tasks: list[TaskFeasibilityRecord]


SOURCE_FEASIBILITY_DIMENSIONS = {
    "endpoint_provider_identity",
    "metadata_accessibility",
    "rights_terms_evidence",
    "language_register_evidence",
    "provenance_versionability",
    "ethics_privacy_assessability",
    "task_scientific_fit",
    "duplication_contamination_assessability",
}


class SourceFeasibilityRecord(BaseModel):
    """Metadata-only evidence about one registered source candidate."""

    model_config = ConfigDict(extra="forbid")

    source_id: str = Field(min_length=1)
    review_status: ReviewStatus
    reviewed_on: date
    prepared_by: str = Field(min_length=1)
    ai_assistance_disclosed: Literal[True]
    evidence_path: str = Field(min_length=1)
    authoritative_evidence_urls: list[str] = Field(default_factory=list)
    dimensions: dict[str, EvidenceState]
    overall: FeasibilityConclusion
    recommended_actions: list[SourceReviewAction] = Field(min_length=1)
    unresolved_claims: list[str] = Field(default_factory=list)
    candidate_task_instance_ids: list[str] = Field(default_factory=list)
    recommended_child_records: list[str] = Field(default_factory=list)
    authorization_effect: Literal["NONE"]

    @model_validator(mode="after")
    def validate_metadata_only_scope(self) -> "SourceFeasibilityRecord":
        dimensions = set(self.dimensions)
        if dimensions != SOURCE_FEASIBILITY_DIMENSIONS:
            missing = sorted(SOURCE_FEASIBILITY_DIMENSIONS - dimensions)
            extra = sorted(dimensions - SOURCE_FEASIBILITY_DIMENSIONS)
            raise ValueError(
                f"source feasibility dimensions mismatch; missing={missing}, extra={extra}"
            )
        if self.review_status not in {
            ReviewStatus.SUBMITTED_TO_REVIEW,
            ReviewStatus.BLOCKED,
        }:
            raise ValueError(
                "metadata source reviews must be SUBMITTED_TO_REVIEW or BLOCKED"
            )
        if self.overall == FeasibilityConclusion.PILOT_FEASIBLE:
            raise ValueError("metadata-only review cannot declare a source PILOT_FEASIBLE")
        if (
            EvidenceState.EVIDENCE_AVAILABLE in self.dimensions.values()
            and not self.authoritative_evidence_urls
        ):
            raise ValueError(
                "EVIDENCE_AVAILABLE requires an authoritative evidence URL"
            )
        for values, label in (
            (self.authoritative_evidence_urls, "authoritative evidence URLs"),
            (self.candidate_task_instance_ids, "candidate task instance IDs"),
            (self.recommended_child_records, "recommended child records"),
        ):
            if len(values) != len(set(values)):
                raise ValueError(f"{label} must be unique")
        return self


class SourceFeasibilityLedger(GovernedArtifact):
    """Complete metadata review ledger for candidate and synthetic sources."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[1]
    candidate_reviews: list[SourceFeasibilityRecord]
    synthetic_control: SourceFeasibilityRecord


class GovernanceAudit(BaseModel):
    """Deterministic output contract for repository governance audits."""

    status: Literal["PASS", "FAIL"]
    errors: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    blocked_components: list[str] = Field(default_factory=list)
    unresolved_decisions: list[str] = Field(default_factory=list)
    release_eligible: bool = False

    def normalized(self) -> "GovernanceAudit":
        """Return a stable, duplicate-free representation for CLI and CI output."""

        for field_name in (
            "errors",
            "warnings",
            "blocked_components",
            "unresolved_decisions",
        ):
            values = sorted(set(getattr(self, field_name)))
            setattr(self, field_name, values)
        self.status = "FAIL" if self.errors else "PASS"
        self.release_eligible = not (
            self.errors or self.blocked_components or self.unresolved_decisions
        )
        return self

    def as_json(self) -> str:
        """Serialize the audit using a stable key and list order."""

        payload = self.normalized().model_dump(mode="json")
        return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)


def audit_repository(root: str | Path) -> GovernanceAudit:
    """Audit configuration governance and committed sample-data invariants."""

    repository = Path(root).resolve()
    audit = GovernanceAudit(status="PASS")
    decisions = _load_decisions(repository, audit)

    benchmark_path = repository / "configs" / "benchmark.yaml"
    benchmark = _load_mapping(benchmark_path, repository, audit)
    if benchmark is not None:
        _validate_governed_artifact(
            benchmark, benchmark_path, repository, decisions, audit
        )

    taxonomy = _audit_task_taxonomy(repository, decisions, audit)
    domains = _audit_domain_registry(repository, decisions, audit)

    tasks = _audit_config_directory(
        repository / "configs" / "tasks", repository, decisions, audit, "task"
    )
    labels = _audit_config_directory(
        repository / "configs" / "labels", repository, decisions, audit, "label schema"
    )
    _audit_config_directory(
        repository / "configs" / "orthography",
        repository,
        decisions,
        audit,
        "orthography configuration",
    )
    sources = _audit_sources(repository, decisions, audit)
    task_instances = _validate_tasks(
        tasks, labels, taxonomy, repository, decisions, audit
    )
    releases = _audit_releases(repository, decisions, task_instances, audit)
    pilot_task_ids = {
        membership.task_instance_id
        for release in releases.values()
        if release.release_id == "v0.1"
        for membership in release.task_memberships
        if membership.scope_status == ScopeStatus.PILOT_CANDIDATE
    }
    _audit_task_feasibility(
        repository, decisions, task_instances, pilot_task_ids, sources, audit
    )
    _audit_source_feasibility(
        repository, decisions, task_instances, sources, audit
    )

    if benchmark is not None:
        _validate_benchmark(
            benchmark,
            taxonomy,
            domains,
            releases,
            benchmark_path,
            repository,
            audit,
        )
    _audit_sample_data(repository, tasks, labels, domains, sources, audit)
    _audit_retrieval_sample(repository, domains, sources, audit)
    _validate_decision_document(repository, decisions, audit)

    return audit.normalized()


def _load_mapping(
    path: Path, root: Path, audit: GovernanceAudit
) -> dict[str, Any] | None:
    try:
        return load_yaml(path)
    except (OSError, ValueError) as exc:
        audit.errors.append(f"{_display(path, root)}: {exc}")
        return None


def _load_decisions(root: Path, audit: GovernanceAudit) -> dict[str, DecisionRecord]:
    path = root / "configs" / "governance" / "decisions.yaml"
    payload = _load_mapping(path, root, audit)
    if payload is None:
        return {}
    if payload.get("schema_version") != 4:
        audit.errors.append(
            f"{_display(path, root)}: committed decision registry must use schema_version: 4"
        )
    raw_records = payload.get("decisions")
    if not isinstance(raw_records, list):
        audit.errors.append(f"{_display(path, root)}: decisions must be a list")
        return {}

    decisions: dict[str, DecisionRecord] = {}
    for index, raw in enumerate(raw_records):
        try:
            record = DecisionRecord.model_validate(raw)
        except ValidationError as exc:
            audit.errors.append(
                f"{_display(path, root)}: decisions[{index}] is invalid: "
                f"{_validation_message(exc)}"
            )
            continue
        if record.id in decisions:
            audit.errors.append(f"{_display(path, root)}: duplicate decision ID {record.id}")
            continue
        for event_index, event in enumerate(record.review_history):
            evidence = (root / event.evidence_path).resolve()
            try:
                evidence.relative_to(root)
            except ValueError:
                audit.errors.append(
                    f"{_display(path, root)}: {record.id} review_history[{event_index}] "
                    "evidence_path must remain inside the repository"
                )
                continue
            if not evidence.is_file():
                audit.errors.append(
                    f"{_display(path, root)}: {record.id} review_history[{event_index}] "
                    f"evidence_path does not exist: {event.evidence_path}"
                )
        decisions[record.id] = record
        if record.requires_expert_approval and record.status in UNRESOLVED_STATUSES:
            audit.unresolved_decisions.append(record.id)
    return decisions


def _audit_config_directory(
    directory: Path,
    root: Path,
    decisions: dict[str, DecisionRecord],
    audit: GovernanceAudit,
    kind: str,
) -> dict[str, dict[str, Any]]:
    registry: dict[str, dict[str, Any]] = {}
    for path in sorted(directory.glob("*.yaml")):
        payload = _load_mapping(path, root, audit)
        if payload is None:
            continue
        key_name = "task" if kind == "task" else None
        key = str(payload.get(key_name) if key_name else path.stem)
        if key in registry:
            audit.errors.append(f"{_display(path, root)}: duplicate {kind} key {key}")
            continue
        registry[key] = payload
        if kind != "task":
            _validate_governed_artifact(payload, path, root, decisions, audit)
        if kind == "label schema":
            _validate_label_schema(payload, path, root, audit)
    return registry


def _validate_governed_artifact(
    payload: dict[str, Any],
    path: Path,
    root: Path,
    decisions: dict[str, DecisionRecord],
    audit: GovernanceAudit,
) -> None:
    try:
        governed = GovernedArtifact.model_validate(payload)
    except ValidationError as exc:
        audit.errors.append(
            f"{_display(path, root)}: invalid governance fields: {_validation_message(exc)}"
        )
        return

    unresolved_refs: list[str] = []
    for decision_id in governed.decision_ids:
        decision = decisions.get(decision_id)
        if decision is None:
            audit.errors.append(
                f"{_display(path, root)}: unresolved decision reference {decision_id}"
            )
        elif decision.status != ReviewStatus.EXPERT_VALIDATED:
            unresolved_refs.append(decision_id)

    if governed.status == ReviewStatus.BLOCKED:
        audit.blocked_components.append(_display(path, root))
    elif governed.requires_expert_validation and governed.status != ReviewStatus.EXPERT_VALIDATED:
        audit.blocked_components.append(_display(path, root))

    if governed.release_candidate:
        if governed.status != ReviewStatus.EXPERT_VALIDATED:
            audit.errors.append(
                f"{_display(path, root)}: release candidate is not EXPERT_VALIDATED"
            )
        if unresolved_refs:
            joined = ", ".join(sorted(unresolved_refs))
            audit.errors.append(
                f"{_display(path, root)}: release candidate depends on unresolved decisions: {joined}"
            )


def _audit_task_taxonomy(
    root: Path,
    decisions: dict[str, DecisionRecord],
    audit: GovernanceAudit,
) -> dict[str, TaskFamilyRecord]:
    path = root / "configs" / "task_taxonomy.yaml"
    payload = _load_mapping(path, root, audit)
    if payload is None:
        return {}
    try:
        taxonomy = TaskTaxonomyRecord.model_validate(payload)
    except ValidationError as exc:
        audit.errors.append(
            f"{_display(path, root)}: invalid task taxonomy: {_validation_message(exc)}"
        )
        return {}
    _validate_governed_artifact(payload, path, root, decisions, audit)
    families: dict[str, TaskFamilyRecord] = {}
    for family in taxonomy.task_families:
        if family.family_id in families:
            audit.errors.append(
                f"{_display(path, root)}: duplicate task family {family.family_id}"
            )
        families[family.family_id] = family
    return families


def _audit_domain_registry(
    root: Path,
    decisions: dict[str, DecisionRecord],
    audit: GovernanceAudit,
) -> dict[str, DomainRecord]:
    path = root / "configs" / "domains.yaml"
    payload = _load_mapping(path, root, audit)
    if payload is None:
        return {}
    try:
        registry = DomainRegistryRecord.model_validate(payload)
    except ValidationError as exc:
        audit.errors.append(
            f"{_display(path, root)}: invalid domain registry: {_validation_message(exc)}"
        )
        return {}
    _validate_governed_artifact(payload, path, root, decisions, audit)
    domains: dict[str, DomainRecord] = {}
    for domain in registry.domains:
        if domain.domain_id in domains:
            audit.errors.append(
                f"{_display(path, root)}: duplicate domain {domain.domain_id}"
            )
        domains[domain.domain_id] = domain
    return domains


def _validate_benchmark(
    benchmark: dict[str, Any],
    taxonomy: dict[str, TaskFamilyRecord],
    domains: dict[str, DomainRecord],
    releases: dict[str, ReleaseRecord],
    path: Path,
    root: Path,
    audit: GovernanceAudit,
) -> None:
    required = {
        "name",
        "program_id",
        "ecosystem_id",
        "language",
        "task_taxonomy",
        "domain_registry",
        "release_registry",
        "current_pilot_release",
    }
    missing = sorted(required - benchmark.keys())
    if missing:
        audit.errors.append(f"{_display(path, root)}: missing fields {', '.join(missing)}")
    deprecated = sorted({"version", "splits", "v0_tasks", "domains"} & benchmark.keys())
    if deprecated:
        audit.errors.append(
            f"{_display(path, root)}: release-specific fields must not define the ecosystem: "
            f"{', '.join(deprecated)}"
        )
    expected_paths = {
        "task_taxonomy": "configs/task_taxonomy.yaml",
        "domain_registry": "configs/domains.yaml",
        "release_registry": "configs/releases",
    }
    for field, expected in expected_paths.items():
        if benchmark.get(field) != expected:
            audit.errors.append(
                f"{_display(path, root)}: {field} must reference {expected}"
            )
    if not taxonomy:
        audit.errors.append(f"{_display(path, root)}: task taxonomy is empty or invalid")
    if not domains:
        audit.errors.append(f"{_display(path, root)}: domain registry is empty or invalid")
    current_release = benchmark.get("current_pilot_release")
    if current_release not in releases:
        audit.errors.append(
            f"{_display(path, root)}: current_pilot_release {current_release!r} is not registered"
        )


def _validate_tasks(
    tasks: dict[str, dict[str, Any]],
    labels: dict[str, dict[str, Any]],
    taxonomy: dict[str, TaskFamilyRecord],
    root: Path,
    decisions: dict[str, DecisionRecord],
    audit: GovernanceAudit,
) -> dict[str, TaskInstanceRecord]:
    instances: dict[str, TaskInstanceRecord] = {}
    for task_name, payload in sorted(tasks.items()):
        path = root / "configs" / "tasks" / f"{task_name}.yaml"
        try:
            instance = TaskInstanceRecord.model_validate(payload)
        except ValidationError as exc:
            audit.errors.append(
                f"{_display(path, root)}: invalid task instance: {_validation_message(exc)}"
            )
            continue
        if instance.task_instance_id in instances:
            audit.errors.append(
                f"{_display(path, root)}: duplicate task_instance_id "
                f"{instance.task_instance_id}"
            )
        instances[instance.task_instance_id] = instance
        if task_name != path.stem:
            audit.errors.append(
                f"{_display(path, root)}: task name {task_name} does not match filename"
            )
        deprecated = sorted(
            {"status", "scope_tier", "v0", "release_candidate"} & payload.keys()
        )
        if deprecated:
            audit.errors.append(
                f"{_display(path, root)}: deprecated task scope fields: "
                f"{', '.join(deprecated)}"
            )
        family = taxonomy.get(instance.task_family_id)
        if family is None:
            audit.errors.append(
                f"{_display(path, root)}: unknown task_family_id {instance.task_family_id}"
            )
        elif instance.task_type_id not in family.task_type_ids:
            audit.errors.append(
                f"{_display(path, root)}: task_type_id {instance.task_type_id} is not "
                f"registered under {instance.task_family_id}"
            )
        _validate_scientific_artifact(
            instance.scientific_status,
            instance.scope_status,
            instance.decision_ids,
            instance.requires_expert_validation,
            path,
            root,
            decisions,
            audit,
        )

        required = {"primary_metric"}
        if payload.get("data_contract") == "separate_corpus_queries_qrels_v1":
            required.update({"artifact_files", "query_origins", "unjudged_policy"})
        else:
            required.update({"input_fields", "target_fields"})
        missing = sorted(required - payload.keys())
        if missing:
            audit.errors.append(f"{_display(path, root)}: missing fields {', '.join(missing)}")
        expected_contracts = {
            "classification": (["text"], ["labels"]),
            "ner": (["text"], ["entities"]),
            "normalization": (["raw_text"], ["decision", "references", "edits"]),
            "codeswitch": (
                ["raw_text", "tokens", "tokenization_version"],
                ["annotations"],
            ),
        }
        if task_name in expected_contracts:
            expected_input, expected_target = expected_contracts[task_name]
            if payload.get("input_fields") != expected_input:
                audit.errors.append(
                    f"{_display(path, root)}: {task_name} input_fields must be {expected_input}"
                )
            if payload.get("target_fields") != expected_target:
                audit.errors.append(
                    f"{_display(path, root)}: {task_name} target_fields must be {expected_target}"
                )
        if task_name == "retrieval" and payload.get("data_contract") != (
            "separate_corpus_queries_qrels_v1"
        ):
            audit.errors.append(
                f"{_display(path, root)}: retrieval must use separate corpus/query/qrel artifacts"
            )
        label_path = payload.get("labels_config")
        if label_path:
            configured_path = root / str(label_path)
            if not configured_path.is_file():
                audit.errors.append(
                    f"{_display(path, root)}: labels_config does not exist: {label_path}"
                )
            elif configured_path.stem not in labels:
                audit.errors.append(
                    f"{_display(path, root)}: labels_config is outside the audited label registry"
                )
    return instances


def _validate_scientific_artifact(
    scientific_status: ReviewStatus,
    scope_status: ScopeStatus,
    decision_ids: list[str],
    requires_expert_validation: bool,
    path: Path,
    root: Path,
    decisions: dict[str, DecisionRecord],
    audit: GovernanceAudit,
) -> None:
    unresolved: list[str] = []
    for decision_id in decision_ids:
        decision = decisions.get(decision_id)
        if decision is None:
            audit.errors.append(
                f"{_display(path, root)}: unresolved decision reference {decision_id}"
            )
        elif decision.status != ReviewStatus.EXPERT_VALIDATED:
            unresolved.append(decision_id)
    if scientific_status == ReviewStatus.BLOCKED or (
        requires_expert_validation and scientific_status != ReviewStatus.EXPERT_VALIDATED
    ):
        audit.blocked_components.append(_display(path, root))
    if scope_status in {ScopeStatus.RELEASE_CANDIDATE, ScopeStatus.INCLUDED_IN_RELEASE}:
        if scientific_status != ReviewStatus.EXPERT_VALIDATED:
            audit.errors.append(
                f"{_display(path, root)}: {scope_status.value} requires EXPERT_VALIDATED"
            )
        if unresolved:
            audit.errors.append(
                f"{_display(path, root)}: {scope_status.value} depends on unresolved "
                f"decisions: {', '.join(sorted(unresolved))}"
            )


def _audit_releases(
    root: Path,
    decisions: dict[str, DecisionRecord],
    task_instances: dict[str, TaskInstanceRecord],
    audit: GovernanceAudit,
) -> dict[str, ReleaseRecord]:
    releases: dict[str, ReleaseRecord] = {}
    directory = root / "configs" / "releases"
    supported_splits = {"train", "validation", "test_public", "test_hidden"}
    for path in sorted(directory.glob("*.yaml")):
        payload = _load_mapping(path, root, audit)
        if payload is None:
            continue
        try:
            release = ReleaseRecord.model_validate(payload)
        except ValidationError as exc:
            audit.errors.append(
                f"{_display(path, root)}: invalid release record: {_validation_message(exc)}"
            )
            continue
        if release.release_id in releases:
            audit.errors.append(
                f"{_display(path, root)}: duplicate release_id {release.release_id}"
            )
        releases[release.release_id] = release
        _validate_scientific_artifact(
            release.scientific_status,
            release.scope_status,
            release.decision_ids,
            release.requires_expert_validation,
            path,
            root,
            decisions,
            audit,
        )
        if len(release.splits) != len(set(release.splits)) or not set(
            release.splits
        ) <= supported_splits:
            audit.errors.append(f"{_display(path, root)}: contains unsupported split names")
        membership_ids = [item.task_instance_id for item in release.task_memberships]
        if len(membership_ids) != len(set(membership_ids)):
            audit.errors.append(f"{_display(path, root)}: duplicate task membership")
        for membership in release.task_memberships:
            instance = task_instances.get(membership.task_instance_id)
            if instance is None:
                audit.errors.append(
                    f"{_display(path, root)}: unknown task_instance_id "
                    f"{membership.task_instance_id}"
                )
                continue
            if membership.scope_status in {ScopeStatus.ROADMAP, ScopeStatus.DISCOVERY}:
                audit.errors.append(
                    f"{_display(path, root)}: roadmap or discovery tasks do not belong "
                    "in a release record"
                )
            if membership.scope_status != instance.scope_status:
                audit.errors.append(
                    f"{_display(path, root)}: membership scope for "
                    f"{membership.task_instance_id} does not match its task config"
                )
            if membership.scope_status == ScopeStatus.INCLUDED_IN_RELEASE:
                if release.scope_status != ScopeStatus.INCLUDED_IN_RELEASE:
                    audit.errors.append(
                        f"{_display(path, root)}: included task requires an included release"
                    )
                if instance.scientific_status != ReviewStatus.EXPERT_VALIDATED:
                    audit.errors.append(
                        f"{_display(path, root)}: included task "
                        f"{membership.task_instance_id} is not EXPERT_VALIDATED"
                    )
    return releases


def _audit_task_feasibility(
    root: Path,
    decisions: dict[str, DecisionRecord],
    task_instances: dict[str, TaskInstanceRecord],
    pilot_task_ids: set[str],
    sources: dict[str, SourceRecord],
    audit: GovernanceAudit,
) -> None:
    path = root / "configs" / "governance" / "task_feasibility.yaml"
    payload = _load_mapping(path, root, audit)
    if payload is None:
        return
    try:
        matrix = TaskFeasibilityMatrix.model_validate(payload)
    except ValidationError as exc:
        audit.errors.append(
            f"{_display(path, root)}: invalid task feasibility matrix: "
            f"{_validation_message(exc)}"
        )
        return
    _validate_governed_artifact(payload, path, root, decisions, audit)

    assessed_tasks: set[str] = set()
    for record in matrix.tasks:
        if record.task_instance_id in assessed_tasks:
            audit.errors.append(
                f"{_display(path, root)}: duplicate feasibility record for "
                f"{record.task_instance_id}"
            )
        assessed_tasks.add(record.task_instance_id)
        if record.task_instance_id not in task_instances:
            audit.errors.append(
                f"{_display(path, root)}: unknown task instance in feasibility matrix: "
                f"{record.task_instance_id}"
            )
        for source_id in record.source_candidates:
            if source_id not in sources:
                audit.errors.append(
                    f"{_display(path, root)}: {record.task_instance_id} references "
                    f"unknown source {source_id}"
                )

    if assessed_tasks != pilot_task_ids:
        audit.errors.append(
            f"{_display(path, root)}: feasibility tasks do not match v0.1 pilot; "
            f"expected={sorted(pilot_task_ids)}, actual={sorted(assessed_tasks)}"
        )


def _audit_source_feasibility(
    root: Path,
    decisions: dict[str, DecisionRecord],
    task_instances: dict[str, TaskInstanceRecord],
    sources: dict[str, SourceRecord],
    audit: GovernanceAudit,
) -> None:
    path = root / "configs" / "governance" / "source_feasibility.yaml"
    payload = _load_mapping(path, root, audit)
    if payload is None:
        return
    try:
        ledger = SourceFeasibilityLedger.model_validate(payload)
    except ValidationError as exc:
        audit.errors.append(
            f"{_display(path, root)}: invalid source feasibility ledger: "
            f"{_validation_message(exc)}"
        )
        return
    _validate_governed_artifact(payload, path, root, decisions, audit)

    candidate_ids = [record.source_id for record in ledger.candidate_reviews]
    if len(candidate_ids) != len(set(candidate_ids)):
        audit.errors.append(f"{_display(path, root)}: duplicate candidate source review")

    expected_candidates = set(sources) - {"sample"}
    if set(candidate_ids) != expected_candidates:
        audit.errors.append(
            f"{_display(path, root)}: source review coverage mismatch; "
            f"expected={sorted(expected_candidates)}, actual={sorted(set(candidate_ids))}"
        )
    if ledger.synthetic_control.source_id != "sample":
        audit.errors.append(
            f"{_display(path, root)}: synthetic_control must reference source_id sample"
        )

    for record in [*ledger.candidate_reviews, ledger.synthetic_control]:
        source = sources.get(record.source_id)
        if source is None:
            audit.errors.append(
                f"{_display(path, root)}: unknown reviewed source {record.source_id}"
            )
            continue
        evidence = (root / record.evidence_path).resolve()
        try:
            evidence.relative_to(root)
        except ValueError:
            audit.errors.append(
                f"{_display(path, root)}: {record.source_id} evidence_path "
                "must remain inside the repository"
            )
        else:
            if not evidence.is_file():
                audit.errors.append(
                    f"{_display(path, root)}: {record.source_id} evidence_path "
                    f"does not exist: {record.evidence_path}"
                )
        unknown_tasks = sorted(
            set(record.candidate_task_instance_ids) - set(task_instances)
        )
        if unknown_tasks:
            audit.errors.append(
                f"{_display(path, root)}: {record.source_id} references unknown "
                f"task instances: {unknown_tasks}"
            )
        if source.record_type == SourceRecordType.SOURCE_FAMILY:
            prohibited_actions = {
                SourceReviewAction.REQUEST_PERMISSION,
            }
            if prohibited_actions.intersection(record.recommended_actions):
                audit.errors.append(
                    f"{_display(path, root)}: SOURCE_FAMILY {record.source_id} "
                    "cannot be recommended directly for permission or collection"
                )

        governance = source.source_governance
        if record.source_id == "sample":
            if (
                source.release_candidate
                or governance.scientific_status
                != ScientificInclusionStatus.EXCLUDED
            ):
                audit.errors.append(
                    f"{_display(path, root)}: synthetic sample must remain "
                    "scientifically excluded and non-releaseable"
                )
            continue
        if (
            source.release_candidate
            or source.status == ReviewStatus.EXPERT_VALIDATED
            or governance.collection_status == CollectionStatus.APPROVED
            or governance.derived_use_status == PermissionStatus.APPROVED
            or governance.redistribution_status == RedistributionStatus.APPROVED
            or governance.scientific_status
            in {
                ScientificInclusionStatus.PILOT_ONLY,
                ScientificInclusionStatus.APPROVED,
            }
        ):
            audit.errors.append(
                f"{_display(path, root)}: metadata-only review cannot accompany "
                f"an authorized source state for {record.source_id}"
            )


def _validate_label_schema(
    payload: dict[str, Any], path: Path, root: Path, audit: GovernanceAudit
) -> None:
    label_groups = [
        payload.get("labels"),
        payload.get("entity_types"),
        payload.get("sentence_labels"),
        payload.get("token_labels"),
        payload.get("language_ids"),
        payload.get("token_types"),
    ]
    groups = [group for group in label_groups if group is not None]
    if not groups:
        audit.errors.append(f"{_display(path, root)}: no label collection found")
        return
    for group in groups:
        if not isinstance(group, list) or not all(isinstance(item, str) for item in group):
            audit.errors.append(f"{_display(path, root)}: labels must be a list of strings")
        elif len(group) != len(set(group)):
            audit.errors.append(f"{_display(path, root)}: duplicate labels detected")


def _audit_sources(
    root: Path,
    decisions: dict[str, DecisionRecord],
    audit: GovernanceAudit,
) -> dict[str, SourceRecord]:
    sources: dict[str, SourceRecord] = {}
    source_paths: dict[str, Path] = {}
    directory = root / "configs" / "sources"
    for path in sorted(directory.glob("*.yaml")):
        payload = _load_mapping(path, root, audit)
        if payload is None:
            continue
        source_id = str(payload.get("source_id", ""))
        if not source_id:
            audit.errors.append(f"{_display(path, root)}: missing source_id")
            continue
        if source_id in sources:
            audit.errors.append(f"{_display(path, root)}: duplicate source_id {source_id}")
            continue

        if payload.get("source_schema_version") != 2:
            audit.errors.append(
                f"{_display(path, root)}: committed source configs must use "
                "source_schema_version: 2; legacy review_status fields are deprecated"
            )
            continue
        try:
            source = SourceRecord.model_validate(payload)
        except ValidationError as exc:
            audit.errors.append(
                f"{_display(path, root)}: invalid source record: {_validation_message(exc)}"
            )
            continue

        sources[source_id] = source
        source_paths[source_id] = path
        _validate_governed_artifact(payload, path, root, decisions, audit)
        _validate_source_permissions(source, path, root, audit)

    _validate_source_hierarchy(sources, source_paths, root, audit)
    return sources


def _validate_source_permissions(
    source: SourceRecord, path: Path, root: Path, audit: GovernanceAudit
) -> None:
    governance = source.source_governance
    location = _display(path, root)

    if source.record_type == SourceRecordType.SOURCE_FAMILY:
        prohibited_family_states = {
            "collection_status": governance.collection_status == CollectionStatus.APPROVED,
            "derived_use_status": governance.derived_use_status == PermissionStatus.APPROVED,
            "redistribution_status": (
                governance.redistribution_status == RedistributionStatus.APPROVED
            ),
            "scientific_status": (
                governance.scientific_status == ScientificInclusionStatus.APPROVED
            ),
        }
        for field_name, invalid in prohibited_family_states.items():
            if invalid:
                audit.errors.append(
                    f"{location}: SOURCE_FAMILY cannot have {field_name} APPROVED; "
                    "register a collection or subset"
                )

    if governance.legal_review_status == LegalReviewStatus.REJECTED:
        if governance.collection_status == CollectionStatus.APPROVED:
            audit.errors.append(f"{location}: rejected legal review cannot approve collection")
        if governance.derived_use_status == PermissionStatus.APPROVED:
            audit.errors.append(f"{location}: rejected legal review cannot approve derived use")
        if governance.redistribution_status == RedistributionStatus.APPROVED:
            audit.errors.append(f"{location}: rejected legal review cannot approve redistribution")

    if governance.redistribution_status == RedistributionStatus.APPROVED:
        if source.record_type == SourceRecordType.SOURCE_FAMILY:
            audit.errors.append(f"{location}: source families cannot be approved for redistribution")
        if governance.legal_review_status not in {
            LegalReviewStatus.APPROVED,
            LegalReviewStatus.NOT_APPLICABLE,
        }:
            audit.errors.append(
                f"{location}: redistribution APPROVED requires legal review APPROVED "
                "or NOT_APPLICABLE"
            )
        if governance.ethics_status not in {
            EthicsStatus.APPROVED,
            EthicsStatus.NOT_APPLICABLE,
        }:
            audit.errors.append(
                f"{location}: redistribution APPROVED requires ethics APPROVED "
                "or NOT_APPLICABLE"
            )
        if not source.license_evidence.strip() or not governance.evidence_urls:
            audit.errors.append(
                f"{location}: redistribution APPROVED requires license evidence and an evidence URL"
            )

    if governance.scientific_status == ScientificInclusionStatus.APPROVED:
        if source.status != ReviewStatus.EXPERT_VALIDATED:
            audit.errors.append(
                f"{location}: scientific inclusion APPROVED requires project status EXPERT_VALIDATED"
            )

    if source.release_candidate:
        required_release_states = {
            "redistribution_status": (
                governance.redistribution_status == RedistributionStatus.APPROVED
            ),
            "scientific_status": (
                governance.scientific_status == ScientificInclusionStatus.APPROVED
            ),
            "legal_review_status": governance.legal_review_status
            in {LegalReviewStatus.APPROVED, LegalReviewStatus.NOT_APPLICABLE},
            "ethics_status": governance.ethics_status
            in {EthicsStatus.APPROVED, EthicsStatus.NOT_APPLICABLE},
        }
        for field_name, valid in required_release_states.items():
            if not valid:
                audit.errors.append(
                    f"{location}: release candidate lacks an approved {field_name} gate"
                )


def _validate_source_hierarchy(
    sources: dict[str, SourceRecord],
    source_paths: dict[str, Path],
    root: Path,
    audit: GovernanceAudit,
) -> None:
    for source_id, source in sorted(sources.items()):
        location = _display(source_paths[source_id], root)
        parent_id = source.parent_source_id
        if source.record_type == SourceRecordType.SOURCE_FAMILY and parent_id is not None:
            audit.errors.append(f"{location}: SOURCE_FAMILY must not have parent_source_id")
        if source.record_type == SourceRecordType.SOURCE_SUBSET and parent_id is None:
            audit.errors.append(f"{location}: SOURCE_SUBSET requires parent_source_id")
        if parent_id is not None and parent_id not in sources:
            audit.errors.append(f"{location}: parent_source_id {parent_id} is not registered")
        elif parent_id is not None and sources[parent_id].record_type == SourceRecordType.SOURCE_SUBSET:
            audit.errors.append(f"{location}: SOURCE_SUBSET cannot be a parent source")

    for source_id in sorted(sources):
        visited: set[str] = set()
        current: str | None = source_id
        while current is not None and current in sources:
            if current in visited:
                audit.errors.append(
                    f"configs/sources: source hierarchy cycle detected from {source_id}"
                )
                break
            visited.add(current)
            current = sources[current].parent_source_id


def _audit_sample_data(
    root: Path,
    tasks: dict[str, dict[str, Any]],
    labels: dict[str, dict[str, Any]],
    domains: dict[str, DomainRecord],
    sources: dict[str, SourceRecord],
    audit: GovernanceAudit,
) -> None:
    seen_ids: dict[str, str] = {}
    text_splits: dict[str, set[str]] = defaultdict(set)
    for path in sorted((root / "data" / "sample").glob("*.jsonl")):
        display_path = _display(path, root)
        try:
            raw_rows = read_jsonl(path)
        except (OSError, ValueError) as exc:
            audit.errors.append(f"{display_path}: {exc}")
            continue
        for index, raw in enumerate(raw_rows, start=1):
            location = f"{display_path}:{index}"
            try:
                row = validate_row(raw)
            except (ValidationError, ValueError) as exc:
                audit.errors.append(f"{location}: invalid row: {exc}")
                continue
            if row.id in seen_ids:
                audit.errors.append(
                    f"{location}: duplicate ID {row.id}; first seen at {seen_ids[row.id]}"
                )
            else:
                seen_ids[row.id] = location
            if row.task not in tasks:
                audit.errors.append(f"{location}: no task configuration for {row.task}")
            if row.domain not in domains:
                audit.errors.append(f"{location}: domain {row.domain} is not registered")
            source = sources.get(row.source.source_id)
            if source is None:
                audit.errors.append(
                    f"{location}: source_id {row.source.source_id} is not registered"
                )
            elif source.record_type == SourceRecordType.SOURCE_FAMILY:
                audit.errors.append(
                    f"{location}: source_id {row.source.source_id} is a discovery-only "
                    "SOURCE_FAMILY"
                )
            elif (
                source.source_governance.redistribution_status
                != RedistributionStatus.APPROVED
            ):
                audit.errors.append(
                    f"{location}: sample data uses source {row.source.source_id} without "
                    "approved public redistribution"
                )
            _validate_row_labels(row, tasks, labels, location, audit)
            _validate_raw_normalized_linkage(row, location, audit)
            canonical_text = _canonical_input_text(row)
            if canonical_text:
                text_splits[canonical_text].add(row.split)

    for text, splits in sorted(text_splits.items()):
        if "train" in splits and ({"test_public", "test_hidden"} & splits):
            audit.errors.append(
                "data/sample: exact input-text contamination between train and test splits: "
                f"{text[:80]!r}"
            )


def _validate_row_labels(
    row: KreyolBenchRow,
    tasks: dict[str, dict[str, Any]],
    labels: dict[str, dict[str, Any]],
    location: str,
    audit: GovernanceAudit,
) -> None:
    task_config = tasks.get(row.task)
    if not task_config or not task_config.get("labels_config"):
        return
    label_key = Path(str(task_config["labels_config"])).stem
    label_config = labels.get(label_key, {})
    if row.task == "classification":
        allowed = set(label_config.get("labels", []))
        values = row.target.get("labels", [])
        for value in values:
            if value not in allowed:
                audit.errors.append(
                    f"{location}: label {value!r} is not valid for classification"
                )
    elif row.task == "sentiment":
        allowed = set(label_config.get("labels", []))
        value = row.target.get("label")
        if value not in allowed:
            audit.errors.append(f"{location}: label {value!r} is not valid for {row.task}")
    elif row.task == "ner":
        entity_types = set(label_config.get("entity_types", []))
        for entity in row.target.get("entities", []):
            label = entity.get("label")
            if label not in entity_types:
                audit.errors.append(f"{location}: invalid NER entity label {label!r}")
    elif row.task == "codeswitch":
        configured_languages = set(label_config.get("language_ids", []))
        allow_other_iso = label_config.get("allow_registered_iso639_3", False)
        annotations = row.target.get("annotations", [])
        for annotation in annotations:
            language_id = annotation.get("language_id")
            is_iso_like = isinstance(language_id, str) and bool(
                re.fullmatch(r"[a-z]{3}", language_id)
            )
            if language_id not in configured_languages and not (allow_other_iso and is_iso_like):
                audit.errors.append(
                    f"{location}: invalid code-switch language ID {language_id!r}"
                )
        token_types = set(label_config.get("token_types", []))
        for annotation in annotations:
            token_type = annotation.get("token_type")
            if token_type not in token_types:
                audit.errors.append(
                    f"{location}: invalid code-switch token type {token_type!r}"
                )
        contact_statuses = set(label_config.get("contact_statuses", []))
        for annotation in annotations:
            contact_status = annotation.get("contact_status")
            if contact_status not in contact_statuses:
                audit.errors.append(
                    f"{location}: invalid code-switch contact status {contact_status!r}"
                )


def _validate_raw_normalized_linkage(
    row: KreyolBenchRow, location: str, audit: GovernanceAudit
) -> None:
    if row.task != "normalization":
        return
    raw_text = row.input.get("raw_text")
    if not isinstance(raw_text, str) or not raw_text.strip():
        audit.errors.append(
            f"{location}: normalization references require a non-empty input.raw_text linkage"
        )


def _canonical_input_text(row: KreyolBenchRow) -> str:
    text_fields: list[str] = []
    for key in sorted(row.input):
        value = row.input[key]
        if isinstance(value, str):
            text_fields.append(value)
        elif isinstance(value, list) and all(isinstance(item, str) for item in value):
            text_fields.append(" ".join(value))
    return re.sub(r"\s+", " ", " ".join(text_fields)).strip().casefold()


def _audit_retrieval_sample(
    root: Path,
    domains: dict[str, DomainRecord],
    sources: dict[str, SourceRecord],
    audit: GovernanceAudit,
) -> None:
    directory = root / "data" / "sample" / "retrieval"
    artifact_paths = {
        "corpus": directory / "corpus.jsonl",
        "queries": directory / "queries.jsonl",
        "qrels": directory / "qrels.jsonl",
    }
    if not directory.is_dir():
        audit.errors.append("data/sample/retrieval: canonical retrieval fixture is missing")
        return

    documents: dict[str, str] = {}
    queries: dict[str, str] = {}
    qrel_pairs: set[tuple[str, str, str]] = set()
    for kind, path in artifact_paths.items():
        display_path = _display(path, root)
        try:
            rows = read_jsonl(path)
        except (OSError, ValueError) as exc:
            audit.errors.append(f"{display_path}: {exc}")
            continue
        for index, raw in enumerate(rows, start=1):
            location = f"{display_path}:{index}"
            try:
                if kind == "corpus":
                    document = validate_retrieval_document(raw)
                    if document.domain not in domains:
                        audit.errors.append(
                            f"{location}: domain {document.domain} is not registered"
                        )
                    if document.doc_id in documents:
                        audit.errors.append(f"{location}: duplicate doc_id {document.doc_id}")
                    documents[document.doc_id] = location
                    source = sources.get(document.source.source_id)
                    if source is None:
                        audit.errors.append(
                            f"{location}: source_id {document.source.source_id} is not registered"
                        )
                    elif source.record_type == SourceRecordType.SOURCE_FAMILY:
                        audit.errors.append(
                            f"{location}: retrieval document cannot reference SOURCE_FAMILY"
                        )
                    elif (
                        source.source_governance.redistribution_status
                        != RedistributionStatus.APPROVED
                    ):
                        audit.errors.append(
                            f"{location}: retrieval sample uses source "
                            f"{document.source.source_id} without approved public redistribution"
                        )
                elif kind == "queries":
                    query = validate_retrieval_query(raw)
                    if query.domain not in domains:
                        audit.errors.append(
                            f"{location}: domain {query.domain} is not registered"
                        )
                    if query.query_id in queries:
                        audit.errors.append(f"{location}: duplicate query_id {query.query_id}")
                    queries[query.query_id] = location
                else:
                    qrel = validate_retrieval_qrel(raw)
                    pair = (qrel.query_id, qrel.doc_id, qrel.assessor_id)
                    if pair in qrel_pairs:
                        audit.errors.append(
                            f"{location}: duplicate qrel for query, document, and assessor"
                        )
                    qrel_pairs.add(pair)
            except (ValidationError, ValueError) as exc:
                audit.errors.append(f"{location}: invalid retrieval {kind} row: {exc}")

    for query_id, doc_id, _ in sorted(qrel_pairs):
        if query_id not in queries:
            audit.errors.append(f"data/sample/retrieval: qrel query_id {query_id} is missing")
        if doc_id not in documents:
            audit.errors.append(f"data/sample/retrieval: qrel doc_id {doc_id} is missing")


def _validate_decision_document(
    root: Path, decisions: dict[str, DecisionRecord], audit: GovernanceAudit
) -> None:
    path = root / "DECISIONS.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        audit.errors.append(f"{_display(path, root)}: {exc}")
        return
    for decision in decisions.values():
        heading = f"## {decision.id}"
        if heading not in text:
            audit.errors.append(
                f"{_display(path, root)}: missing narrative record for {decision.id}"
            )
            continue
        section = text.split(heading, 1)[1].split("\n## ", 1)[0]
        if f"Status: {decision.status.value}" not in section:
            audit.errors.append(
                f"{_display(path, root)}: status mismatch for {decision.id}; "
                f"machine-readable status is {decision.status.value}"
            )


def _display(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def _validation_message(exc: ValidationError) -> str:
    messages = []
    for error in exc.errors(include_url=False):
        location = ".".join(str(item) for item in error["loc"])
        messages.append(f"{location}: {error['msg']}")
    return "; ".join(messages)
