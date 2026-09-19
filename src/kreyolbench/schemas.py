"""Shared dataset schemas for KreyolBench JSONL rows."""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


# This is the set of row payload adapters implemented by the current package,
# not the global KreyolBench task-family registry.
ImplementedTaskAlias = Literal[
    "classification",
    "sentiment",
    "ner",
    "qa",
    "retrieval",
    "summarization",
    "normalization",
    "translation",
    "codeswitch",
    "orthography_robustness",
]

# Backwards-compatible public alias. Scientific identity comes from the task
# registry's stable task_instance_id rather than this runtime slug.
TaskName = ImplementedTaskAlias

SplitName = Literal["train", "validation", "test_public", "test_hidden"]


class ContentOrigin(str, Enum):
    """Primary origin of an example's linguistic content."""

    HUMAN_ORIGINAL = "HUMAN_ORIGINAL"
    HUMAN_TRANSLATED = "HUMAN_TRANSLATED"
    MACHINE_TRANSLATED = "MACHINE_TRANSLATED"
    LLM_GENERATED = "LLM_GENERATED"
    SYNTHETIC_OTHER = "SYNTHETIC_OTHER"
    ASR_DERIVED = "ASR_DERIVED"
    OCR_DERIVED = "OCR_DERIVED"
    HUMAN_TRANSCRIBED = "HUMAN_TRANSCRIBED"
    MIXED = "MIXED"
    UNKNOWN = "UNKNOWN"


class DerivationType(str, Enum):
    """A transformation applied between a source item and benchmark text."""

    MANUAL_TRANSCRIPTION = "MANUAL_TRANSCRIPTION"
    ASR = "ASR"
    OCR = "OCR"
    NORMALIZATION = "NORMALIZATION"
    HUMAN_TRANSLATION = "HUMAN_TRANSLATION"
    MACHINE_TRANSLATION = "MACHINE_TRANSLATION"
    LLM_GENERATION = "LLM_GENERATION"
    OTHER = "OTHER"


class DerivationStep(BaseModel):
    """One ordered and versionable provenance transformation."""

    model_config = ConfigDict(extra="forbid")

    step_id: str = Field(min_length=1)
    sequence: int = Field(ge=1)
    type: DerivationType
    tool_or_agent: str | None = None
    version: str | None = None
    reviewed_by: str | None = None
    notes: str = ""


class SourceMetadata(BaseModel):
    """Granular example provenance; source-family identifiers are not sufficient."""

    model_config = ConfigDict(extra="forbid")

    source_id: str = Field(min_length=1)
    provenance_unit_id: str = Field(min_length=1)
    source_item_locator: str = Field(min_length=1)
    source_version: str = Field(min_length=1)
    retrieved_at: date
    content_hash: str = Field(pattern=r"^sha256:[0-9a-f]{64}$")
    origin_type: ContentOrigin
    derivation_steps: list[DerivationStep] = Field(default_factory=list)
    url: str | None = None
    license: str = "review_required"
    citation: str | None = None

    @model_validator(mode="after")
    def validate_derivation_order(self) -> "SourceMetadata":
        sequences = [step.sequence for step in self.derivation_steps]
        if sequences != list(range(1, len(sequences) + 1)):
            raise ValueError("derivation step sequences must be contiguous and start at 1")
        if len({step.step_id for step in self.derivation_steps}) != len(self.derivation_steps):
            raise ValueError("derivation step IDs must be unique")
        return self


class MultimodalAuthoringOrigin(str, Enum):
    """How target-language multimodal text was authored or translated."""

    NATIVE_TARGET_LANGUAGE = "NATIVE_TARGET_LANGUAGE"
    HUMAN_TRANSLATED = "HUMAN_TRANSLATED"
    MACHINE_TRANSLATED = "MACHINE_TRANSLATED"
    MACHINE_TRANSLATED_AUTO_FILTERED = "MACHINE_TRANSLATED_AUTO_FILTERED"
    MACHINE_TRANSLATED_HUMAN_VALIDATED = "MACHINE_TRANSLATED_HUMAN_VALIDATED"
    UNKNOWN_OR_MIXED = "UNKNOWN_OR_MIXED"


class MediaProvenance(BaseModel):
    """Rights and identity metadata for one image or other media object."""

    model_config = ConfigDict(extra="forbid")

    media_id: str = Field(min_length=1)
    original_source: str = Field(min_length=1)
    creator_or_rights_holder: str | None = None
    license_or_terms: str = Field(min_length=1)
    source_url: str | None = None
    version_or_hash: str = Field(min_length=1)
    geographic_cultural_provenance: str | None = None


class CaptionProvenance(BaseModel):
    """Independent provenance for text associated with a media object."""

    model_config = ConfigDict(extra="forbid")

    caption_id: str = Field(min_length=1)
    language: str = Field(min_length=1)
    authoring_origin: MultimodalAuthoringOrigin
    original_language: str | None = None
    translator_type: str | None = None
    translation_model: str | None = None
    translation_model_version: str | None = None
    translation_selection_method: str | None = None
    quality_estimation_method: str | None = None
    human_validation_status: str = Field(min_length=1)
    judgment_language: str | None = None
    judgment_provenance: str | None = None

    @model_validator(mode="after")
    def validate_translation_provenance(self) -> "CaptionProvenance":
        machine_origins = {
            MultimodalAuthoringOrigin.MACHINE_TRANSLATED,
            MultimodalAuthoringOrigin.MACHINE_TRANSLATED_AUTO_FILTERED,
            MultimodalAuthoringOrigin.MACHINE_TRANSLATED_HUMAN_VALIDATED,
        }
        if self.authoring_origin in machine_origins:
            if not self.original_language or not self.translation_model:
                raise ValueError(
                    "machine-translated captions require original_language and translation_model"
                )
        if (
            self.authoring_origin
            == MultimodalAuthoringOrigin.MACHINE_TRANSLATED_AUTO_FILTERED
            and not self.translation_selection_method
        ):
            raise ValueError(
                "automatically filtered translations require translation_selection_method"
            )
        return self


class MediaCaptionLinkage(BaseModel):
    """Versioned relationship between independently governed media and text."""

    model_config = ConfigDict(extra="forbid")

    media_id: str = Field(min_length=1)
    caption_id: str = Field(min_length=1)
    parent_dataset: str = Field(min_length=1)
    derived_dataset: str | None = None
    transformation_history: list[DerivationStep] = Field(default_factory=list)
    split: str = Field(min_length=1)
    contamination_status: str = Field(min_length=1)

    @model_validator(mode="after")
    def validate_transformation_order(self) -> "MediaCaptionLinkage":
        sequences = [step.sequence for step in self.transformation_history]
        if sequences != list(range(1, len(sequences) + 1)):
            raise ValueError("multimodal transformation steps must be ordered and contiguous")
        return self


class MultimodalProvenance(BaseModel):
    """Media, caption, and linkage provenance without rights inheritance."""

    model_config = ConfigDict(extra="forbid")

    media: MediaProvenance
    caption: CaptionProvenance
    linkage: MediaCaptionLinkage

    @model_validator(mode="after")
    def validate_linkage_ids(self) -> "MultimodalProvenance":
        if self.linkage.media_id != self.media.media_id:
            raise ValueError("linkage media_id must match media provenance")
        if self.linkage.caption_id != self.caption.caption_id:
            raise ValueError("linkage caption_id must match caption provenance")
        return self


class NormalizationDecision(str, Enum):
    """Adjudication outcome for one normalization example."""

    ERROR_CORRECTION = "ERROR_CORRECTION"
    ACCEPTABLE_VARIANT_NORMALIZATION = "ACCEPTABLE_VARIANT_NORMALIZATION"
    ACCEPT_AS_IS = "ACCEPT_AS_IS"
    ABSTAIN = "ABSTAIN"


class CodeSwitchContactStatus(str, Enum):
    """Language-contact analysis kept separate from token language identity."""

    NONE = "NONE"
    ACTIVE_SWITCH = "ACTIVE_SWITCH"
    ESTABLISHED_BORROWING = "ESTABLISHED_BORROWING"
    MIXED_INTRATOKEN = "MIXED_INTRATOKEN"
    SHARED_AMBIGUOUS = "SHARED_AMBIGUOUS"
    UNCERTAIN = "UNCERTAIN"


class CodeSwitchUncertainty(str, Enum):
    """Reason an annotation cannot be treated as unambiguous."""

    NONE = "NONE"
    AMBIGUOUS_FORM = "AMBIGUOUS_FORM"
    INSUFFICIENT_CONTEXT = "INSUFFICIENT_CONTEXT"
    TOKENIZATION_UNCERTAIN = "TOKENIZATION_UNCERTAIN"


class CodeSwitchToken(BaseModel):
    """One versioned token aligned to immutable raw text."""

    model_config = ConfigDict(extra="forbid")

    token_id: str = Field(min_length=1)
    text: str = Field(min_length=1)
    start_char: int = Field(ge=0)
    end_char: int = Field(gt=0)

    @model_validator(mode="after")
    def validate_offsets(self) -> "CodeSwitchToken":
        if self.end_char <= self.start_char:
            raise ValueError("code-switch token end_char must exceed start_char")
        return self


class CodeSwitchAnnotation(BaseModel):
    """Factorized token annotation for language identity and contact status."""

    model_config = ConfigDict(extra="forbid")

    token_id: str = Field(min_length=1)
    language_id: str = Field(pattern=r"^(?:[a-z]{3}|mul|und|zxx)$")
    token_type: Literal[
        "WORD", "NAMED_ENTITY", "NUMBER", "PUNCTUATION", "SYMBOL", "URL", "EMOJI"
    ]
    contact_status: CodeSwitchContactStatus
    uncertainty: CodeSwitchUncertainty = CodeSwitchUncertainty.NONE

    @model_validator(mode="after")
    def validate_contact_semantics(self) -> "CodeSwitchAnnotation":
        if (
            self.contact_status == CodeSwitchContactStatus.ESTABLISHED_BORROWING
            and self.language_id != "hat"
        ):
            raise ValueError("established Haitian Creole borrowings must use language_id hat")
        if (
            self.contact_status == CodeSwitchContactStatus.MIXED_INTRATOKEN
            and self.language_id != "mul"
        ):
            raise ValueError("mixed intra-token forms must use language_id mul")
        if self.contact_status == CodeSwitchContactStatus.UNCERTAIN:
            if self.uncertainty == CodeSwitchUncertainty.NONE:
                raise ValueError("uncertain contact status requires an uncertainty reason")
        if self.language_id == "und" and self.uncertainty == CodeSwitchUncertainty.NONE:
            raise ValueError("language_id und requires an uncertainty reason")
        return self


class KreyolBenchRow(BaseModel):
    id: str
    task: TaskName
    language: str = "hat"
    split: SplitName
    domain: str
    source: SourceMetadata
    input: dict[str, Any] = Field(default_factory=dict)
    target: dict[str, Any] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_task_payload(self) -> "KreyolBenchRow":
        validators = {
            "classification": _require("input.text", "target.labels"),
            "sentiment": _require("input.text", "target.label"),
            "ner": _require("input.text", "target.entities"),
            "qa": _require("input.context", "input.question", "target.answers"),
            "retrieval": _require("input.query", "target.relevant_docs"),
            "summarization": _require("input.document", "target.summary"),
            "normalization": _require(
                "input.raw_text", "target.decision", "target.references", "target.edits"
            ),
            "translation": _require("input.source_text", "input.source_lang", "target.references"),
            "codeswitch": _require(
                "input.raw_text",
                "input.tokens",
                "input.tokenization_version",
                "target.annotations",
            ),
            "orthography_robustness": _require("input.raw_text", "target.variants"),
        }
        validators[self.task](self)
        if self.task == "classification":
            labels = self.target.get("labels")
            if not isinstance(labels, list) or not labels or not all(
                isinstance(label, str) for label in labels
            ):
                raise ValueError("classification target.labels must be a non-empty string list")
            if len(labels) != len(set(labels)):
                raise ValueError("classification target.labels must not contain duplicates")
            if "other" in labels and len(labels) > 1:
                raise ValueError("classification label 'other' must be exclusive")
        if self.task == "ner":
            _validate_ner_entities(self)
        if self.task == "codeswitch":
            _validate_codeswitch(self)
        if self.task == "normalization":
            _validate_normalization(self)
        return self


class RetrievalQueryOrigin(str, Enum):
    """Declared construction route for a retrieval query."""

    CONSENTED_USER_NEED = "CONSENTED_USER_NEED"
    STAKEHOLDER_ELICITED = "STAKEHOLDER_ELICITED"
    DOMAIN_EXPERT_RECONSTRUCTED = "DOMAIN_EXPERT_RECONSTRUCTED"
    EXPERT_AUTHORED_FROM_BRIEF = "EXPERT_AUTHORED_FROM_BRIEF"
    DOCUMENT_DERIVED_DIAGNOSTIC = "DOCUMENT_DERIVED_DIAGNOSTIC"


class RetrievalDocument(BaseModel):
    """One document in a canonical retrieval corpus."""

    model_config = ConfigDict(extra="forbid")

    doc_id: str
    text: str
    language: str = "hat"
    domain: str
    temporal_snapshot_id: str = Field(min_length=1)
    published_on: date | None = None
    source: SourceMetadata
    metadata: dict[str, Any] = Field(default_factory=dict)


class RetrievalQuery(BaseModel):
    """One query with explicit construction provenance."""

    model_config = ConfigDict(extra="forbid")

    query_id: str
    text: str
    language: str = "hat"
    domain: str
    split: SplitName
    query_family_id: str = Field(min_length=1)
    query_origin: RetrievalQueryOrigin
    provenance_note: str
    metadata: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def exclude_document_derived_test_queries(self) -> "RetrievalQuery":
        if (
            self.query_origin == RetrievalQueryOrigin.DOCUMENT_DERIVED_DIAGNOSTIC
            and self.split in {"test_public", "test_hidden"}
        ):
            raise ValueError("document-derived diagnostic queries cannot enter test splits")
        return self


class RetrievalQrel(BaseModel):
    """A graded relevance judgment; absence means unjudged, not irrelevant."""

    model_config = ConfigDict(extra="forbid")

    query_id: str
    doc_id: str
    judgment_status: Literal["JUDGED"]
    relevance: int = Field(ge=0, le=3)
    assessor_id: str
    adjudicated: bool = False


def _validate_ner_entities(row: KreyolBenchRow) -> None:
    text = row.input.get("text")
    entities = row.target.get("entities")
    if not isinstance(text, str) or not isinstance(entities, list):
        raise ValueError("NER requires text and an entity list")
    spans: list[tuple[int, int]] = []
    for entity in entities:
        if not isinstance(entity, dict):
            raise ValueError("NER entities must be objects")
        start = entity.get("start_char")
        end = entity.get("end_char")
        label = entity.get("label")
        if not isinstance(start, int) or not isinstance(end, int) or not isinstance(label, str):
            raise ValueError("NER entities require integer offsets and a string label")
        if start < 0 or end <= start or end > len(text):
            raise ValueError("NER entity offsets are outside input.text")
        if entity.get("text") is not None and entity["text"] != text[start:end]:
            raise ValueError("NER entity text does not match its character offsets")
        if entity.get("segments") is not None:
            raise ValueError("v0.1 NER scoring supports contiguous spans only")
        spans.append((start, end))
    if len(spans) != len(set(spans)):
        raise ValueError("NER entity spans must be unique")
    for index, (start_a, end_a) in enumerate(spans):
        for start_b, end_b in spans[index + 1 :]:
            crossing = (start_a < start_b < end_a < end_b) or (
                start_b < start_a < end_b < end_a
            )
            if crossing:
                raise ValueError("NER entity spans may be nested but must not cross")


def _validate_codeswitch(row: KreyolBenchRow) -> None:
    raw_text = row.input.get("raw_text")
    tokenization_version = row.input.get("tokenization_version")
    raw_tokens = row.input.get("tokens")
    raw_annotations = row.target.get("annotations")
    if not isinstance(raw_text, str) or not raw_text:
        raise ValueError("codeswitch input.raw_text must be non-empty")
    if not isinstance(tokenization_version, str) or not tokenization_version.strip():
        raise ValueError("codeswitch input.tokenization_version must be non-empty")
    if not isinstance(raw_tokens, list) or not isinstance(raw_annotations, list):
        raise ValueError("codeswitch tokens and annotations must be lists")
    tokens = [CodeSwitchToken.model_validate(item) for item in raw_tokens]
    annotations = [CodeSwitchAnnotation.model_validate(item) for item in raw_annotations]
    if len(tokens) != len(annotations):
        raise ValueError("codeswitch tokens and annotations must align")
    token_ids = [token.token_id for token in tokens]
    if len(token_ids) != len(set(token_ids)):
        raise ValueError("codeswitch token IDs must be unique")
    if [item.token_id for item in annotations] != token_ids:
        raise ValueError("codeswitch annotations must align with token IDs in order")
    previous_end = 0
    for token in tokens:
        if token.start_char < previous_end:
            raise ValueError("codeswitch token spans must not overlap")
        if token.end_char > len(raw_text) or raw_text[token.start_char : token.end_char] != token.text:
            raise ValueError("codeswitch token text must match raw-text offsets")
        previous_end = token.end_char


def _validate_normalization(row: KreyolBenchRow) -> None:
    raw_text = row.input.get("raw_text")
    references = row.target.get("references")
    edits = row.target.get("edits")
    decision = NormalizationDecision(row.target.get("decision"))
    if not isinstance(references, list) or not all(
        isinstance(reference, str) and reference.strip() for reference in references
    ):
        raise ValueError("normalization target.references must contain strings")
    if not isinstance(edits, list):
        raise ValueError("normalization target.edits must be a list")
    if decision == NormalizationDecision.ABSTAIN:
        if references or edits:
            raise ValueError("ABSTAIN normalization rows cannot contain references or edits")
        return
    if not references:
        raise ValueError("normalization target.references must be non-empty")
    if decision == NormalizationDecision.ACCEPT_AS_IS:
        if references != [raw_text] or edits:
            raise ValueError("ACCEPT_AS_IS requires the raw text as its sole reference and no edits")
        return
    if not edits:
        raise ValueError("normalization corrections require typed edits")
    allowed_types = {
        "spacing",
        "apostrophe",
        "spelling_convention",
        "accent",
        "capitalization",
        "punctuation",
    }
    for edit in edits:
        if not isinstance(edit, dict) or edit.get("type") not in allowed_types:
            raise ValueError("normalization edits require an allowed type")
        if not isinstance(edit.get("rule_id"), str) or not edit["rule_id"].strip():
            raise ValueError("normalization edits require rule_id")
        expected_stratum = (
            "AUXILIARY"
            if edit["type"] in {"capitalization", "punctuation"}
            else "CORE"
        )
        if edit.get("evaluation_stratum") != expected_stratum:
            raise ValueError(
                f"normalization edit {edit['type']} must use {expected_stratum} stratum"
            )


def _require(*paths: str):
    def validator(row: KreyolBenchRow) -> None:
        for path in paths:
            root, key = path.split(".", 1)
            payload = row.input if root == "input" else row.target
            if key not in payload:
                raise ValueError(f"{row.task} row {row.id} missing {path}")

    return validator


def validate_row(data: dict[str, Any]) -> KreyolBenchRow:
    return KreyolBenchRow.model_validate(data)


def validate_retrieval_document(data: dict[str, Any]) -> RetrievalDocument:
    return RetrievalDocument.model_validate(data)


def validate_retrieval_query(data: dict[str, Any]) -> RetrievalQuery:
    return RetrievalQuery.model_validate(data)


def validate_retrieval_qrel(data: dict[str, Any]) -> RetrievalQrel:
    return RetrievalQrel.model_validate(data)
