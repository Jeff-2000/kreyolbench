"""Kreyol-aware sentence segmentation."""

from __future__ import annotations

import re

ABBREVIATIONS = {"Dr.", "Mesye.", "M.", "Mme.", "St.", "No."}


def split_sentences(text: str) -> list[str]:
    protected = text
    replacements: dict[str, str] = {}
    for index, abbr in enumerate(ABBREVIATIONS):
        token = f"__ABBR_{index}__"
        replacements[token] = abbr
        protected = protected.replace(abbr, token)
    parts = re.split(r"(?<=[.!?])\s+", protected.strip())
    sentences = []
    for part in parts:
        for token, abbr in replacements.items():
            part = part.replace(token, abbr)
        if part.strip():
            sentences.append(part.strip())
    return sentences

