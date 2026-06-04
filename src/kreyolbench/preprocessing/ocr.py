"""Conservative OCR cleanup helpers."""

from __future__ import annotations

CONFUSIONS = {
    "l<": "k",
    "rn": "m",
    "0": "o",
}


def suggest_ocr_corrections(text: str) -> list[dict[str, str]]:
    suggestions = []
    for observed, replacement in CONFUSIONS.items():
        if observed in text:
            suggestions.append({"observed": observed, "suggested": replacement})
    return suggestions

