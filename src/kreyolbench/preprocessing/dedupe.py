"""Exact and lightweight near-duplicate helpers."""

from __future__ import annotations

import re

from kreyolbench.io import sha256_text


def normalized_for_dedupe(text: str) -> str:
    text = text.casefold()
    text = re.sub(r"\W+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def exact_hash(text: str) -> str:
    return sha256_text(text)


def normalized_hash(text: str) -> str:
    return sha256_text(normalized_for_dedupe(text))


def token_jaccard(a: str, b: str) -> float:
    a_tokens = set(normalized_for_dedupe(a).split())
    b_tokens = set(normalized_for_dedupe(b).split())
    if not a_tokens and not b_tokens:
        return 1.0
    if not a_tokens or not b_tokens:
        return 0.0
    return len(a_tokens & b_tokens) / len(a_tokens | b_tokens)

