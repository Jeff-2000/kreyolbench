"""Machine-readable governance and scientific-invariant audits.

The audit deliberately separates structural validity from scientific approval.
A repository can pass structural validation while remaining ineligible for release.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from enum import Enum
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field, ValidationError

from kreyolbench.io import read_jsonl
from kreyolbench.registry import load_yaml
from kreyolbench.schemas import KreyolBenchRow, validate_row


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


UNRESOLVED_STATUSES = {
    ReviewStatus.DRAFT,
    ReviewStatus.IN_PROGRESS,
    ReviewStatus.TO_REVIEW_LATER,
    ReviewStatus.SUBMITTED_TO_REVIEW,
    ReviewStatus.NEEDS_REVISION,
    ReviewStatus.BLOCKED,
}

SOURCE_REVIEW_STATUSES = {
    "pending_legal_review",
    "pending_subset_review",
    "reviewed_public_domain_notice",
    "reviewed_standard_wikimedia_terms",
    "not_approved_for_redistribution",
    "approved_link_only",
    "approved_derived_only",
    "approved_public_release",
}

PUBLIC_REDISTRIBUTION_STATUSES = {
    "reviewed_public_domain_notice",
    "reviewed_standard_wikimedia_terms",
    "approved_public_release",
}

REQUIRED_SOURCE_FIELDS = {
    "source_id",
    "name",
    "url",
    "provider",
    "language_claim",
    "domain",
    "data_type",
    "license",
    "redistribution_allowed",
    "commercial_use_allowed",
    "access_method",
    "expected_tasks",
    "quality_notes",
    "pii_risk",
    "status",
    "review_status",
}


class GovernedArtifact(BaseModel):
    """Governance fields embedded in benchmark configuration artifacts."""

    status: ReviewStatus
    decision_ids: list[str]
    requires_expert_validation: bool
    release_candidate: bool


class DecisionRecord(BaseModel):
    """Machine-readable decision registry entry."""

    id: str
    title: str
    status: ReviewStatus
    requires_expert_approval: bool


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

    tasks = _audit_config_directory(
        repository / "configs" / "tasks", repository, decisions, audit, "task"
    )
    labels = _audit_config_directory(
        repository / "configs" / "labels", repository, decisions, audit, "label schema"
    )
    sources = _audit_sources(repository, decisions, audit)

    if benchmark is not None:
        _validate_benchmark(benchmark, tasks, benchmark_path, repository, audit)
    _validate_tasks(tasks, labels, repository, audit)
    _audit_sample_data(repository, tasks, labels, sources, audit)
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


def _validate_benchmark(
    benchmark: dict[str, Any],
    tasks: dict[str, dict[str, Any]],
    path: Path,
    root: Path,
    audit: GovernanceAudit,
) -> None:
    required = {"name", "version", "language", "splits", "v0_tasks", "domains"}
    missing = sorted(required - benchmark.keys())
    if missing:
        audit.errors.append(f"{_display(path, root)}: missing fields {', '.join(missing)}")

    supported_splits = {"train", "validation", "test_public", "test_hidden"}
    configured_splits = benchmark.get("splits", [])
    if not isinstance(configured_splits, list) or not set(configured_splits) <= supported_splits:
        audit.errors.append(f"{_display(path, root)}: contains unsupported split names")

    for task_name in benchmark.get("v0_tasks", []):
        if task_name not in tasks:
            audit.errors.append(
                f"{_display(path, root)}: v0 task {task_name} has no task configuration"
            )
        elif tasks[task_name].get("v0") is not True:
            audit.errors.append(
                f"{_display(path, root)}: v0 task {task_name} is not marked v0 in its task config"
            )


def _validate_tasks(
    tasks: dict[str, dict[str, Any]],
    labels: dict[str, dict[str, Any]],
    root: Path,
    audit: GovernanceAudit,
) -> None:
    for task_name, payload in sorted(tasks.items()):
        path = root / "configs" / "tasks" / f"{task_name}.yaml"
        required = {"task", "primary_metric", "input_fields", "target_fields", "v0"}
        missing = sorted(required - payload.keys())
        if missing:
            audit.errors.append(f"{_display(path, root)}: missing fields {', '.join(missing)}")
        if task_name != path.stem:
            audit.errors.append(
                f"{_display(path, root)}: task name {task_name} does not match filename"
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


def _validate_label_schema(
    payload: dict[str, Any], path: Path, root: Path, audit: GovernanceAudit
) -> None:
    label_groups = [
        payload.get("labels"),
        payload.get("entity_types"),
        payload.get("sentence_labels"),
        payload.get("token_labels"),
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
) -> dict[str, dict[str, Any]]:
    sources: dict[str, dict[str, Any]] = {}
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
        sources[source_id] = payload
        missing = sorted(REQUIRED_SOURCE_FIELDS - payload.keys())
        if missing:
            audit.errors.append(f"{_display(path, root)}: missing fields {', '.join(missing)}")
        _validate_governed_artifact(payload, path, root, decisions, audit)

        source_status = payload.get("review_status")
        if source_status not in SOURCE_REVIEW_STATUSES:
            audit.errors.append(
                f"{_display(path, root)}: unsupported source review_status {source_status!r}"
            )
        if source_status in PUBLIC_REDISTRIBUTION_STATUSES:
            if payload.get("redistribution_allowed") is not True:
                audit.errors.append(
                    f"{_display(path, root)}: public redistribution status requires "
                    "redistribution_allowed: true"
                )
        elif payload.get("redistribution_allowed") is True:
            audit.errors.append(
                f"{_display(path, root)}: redistribution_allowed is true without an approved "
                "public redistribution status"
            )
    return sources


def _audit_sample_data(
    root: Path,
    tasks: dict[str, dict[str, Any]],
    labels: dict[str, dict[str, Any]],
    sources: dict[str, dict[str, Any]],
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
            source = sources.get(row.source.source_id)
            if source is None:
                audit.errors.append(
                    f"{location}: source_id {row.source.source_id} is not registered"
                )
            elif source.get("review_status") not in PUBLIC_REDISTRIBUTION_STATUSES:
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
    if row.task in {"classification", "sentiment"}:
        allowed = set(label_config.get("labels", []))
        value = row.target.get("label")
        if value not in allowed:
            audit.errors.append(f"{location}: label {value!r} is not valid for {row.task}")
    elif row.task == "ner":
        entity_types = set(label_config.get("entity_types", []))
        for tag in row.target.get("tags", []):
            if tag != "O" and ("-" not in tag or tag.split("-", 1)[1] not in entity_types):
                audit.errors.append(f"{location}: invalid NER tag {tag!r}")
    elif row.task == "codeswitch":
        sentence_labels = set(label_config.get("sentence_labels", []))
        token_labels = set(label_config.get("token_labels", []))
        if row.target.get("sentence_lang") not in sentence_labels:
            audit.errors.append(
                f"{location}: invalid code-switch sentence label "
                f"{row.target.get('sentence_lang')!r}"
            )
        for tag in row.target.get("token_langs", []):
            if tag not in token_labels:
                audit.errors.append(f"{location}: invalid code-switch token label {tag!r}")


def _validate_raw_normalized_linkage(
    row: KreyolBenchRow, location: str, audit: GovernanceAudit
) -> None:
    if "normalized_text" not in row.target:
        return
    raw_text = row.input.get("raw_text")
    if not isinstance(raw_text, str) or not raw_text.strip():
        audit.errors.append(
            f"{location}: normalized_text requires a non-empty input.raw_text linkage"
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
