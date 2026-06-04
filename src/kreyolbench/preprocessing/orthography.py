"""Orthographic normalization utilities."""

from __future__ import annotations

import re
from dataclasses import dataclass


DEFAULT_VARIANTS = {
    r"\bm pa\b": "mwen pa",
    r"\bpa p\b": "p ap",
    r"\bp'ap\b": "p ap",
    r"\blap\b": "l ap",
    r"\bécole\b": "lekòl",
}


@dataclass(frozen=True)
class NormalizationResult:
    raw_text: str
    normalized_text: str
    edits: list[dict[str, str]]
    confidence: float


def normalize_orthography(text: str, variants: dict[str, str] | None = None) -> NormalizationResult:
    variants = variants or DEFAULT_VARIANTS
    normalized = text
    edits: list[dict[str, str]] = []
    for pattern, replacement in variants.items():
        updated = re.sub(pattern, replacement, normalized, flags=re.IGNORECASE)
        if updated != normalized:
            edits.append({"pattern": pattern, "replacement": replacement})
            normalized = updated
    confidence = 1.0 if not edits else 0.75
    return NormalizationResult(text, normalized, edits, confidence)

