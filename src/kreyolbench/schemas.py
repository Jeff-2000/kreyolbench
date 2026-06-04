"""Shared dataset schemas for KreyolBench JSONL rows."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator


TaskName = Literal[
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

SplitName = Literal["train", "validation", "test_public", "test_hidden"]


class SourceMetadata(BaseModel):
    source_id: str
    url: str | None = None
    license: str = "review_required"
    retrieved_at: str | None = None
    citation: str | None = None


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
            "classification": _require("input.text", "target.label"),
            "sentiment": _require("input.text", "target.label"),
            "ner": _require("input.tokens", "target.tags"),
            "qa": _require("input.context", "input.question", "target.answers"),
            "retrieval": _require("input.query", "target.relevant_docs"),
            "summarization": _require("input.document", "target.summary"),
            "normalization": _require("input.raw_text", "target.normalized_text"),
            "translation": _require("input.source_text", "input.source_lang", "target.references"),
            "codeswitch": _require("input.tokens", "target.sentence_lang"),
            "orthography_robustness": _require("input.raw_text", "target.variants"),
        }
        validators[self.task](self)
        if self.task in {"ner", "codeswitch"}:
            tokens = self.input.get("tokens", [])
            tags = self.target.get("tags") or self.target.get("token_langs")
            if tags is not None and len(tokens) != len(tags):
                raise ValueError(f"{self.task} tokens and tags must have equal length")
        return self


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

