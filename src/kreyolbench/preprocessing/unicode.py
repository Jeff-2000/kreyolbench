"""Unicode normalization and text hygiene."""

from __future__ import annotations

import re
import unicodedata

SMART_QUOTES = {
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u00ab": '"',
    "\u00bb": '"',
}
ZERO_WIDTH_RE = re.compile("[\u200b\u200c\u200d\ufeff]")


def normalize_unicode(text: str) -> str:
    for source, replacement in SMART_QUOTES.items():
        text = text.replace(source, replacement)
    text = ZERO_WIDTH_RE.sub("", text)
    return unicodedata.normalize("NFC", text)


def likely_mojibake(text: str) -> bool:
    markers = ("Ã", "Â", "â€™", "â€œ", "�")
    return any(marker in text for marker in markers)

