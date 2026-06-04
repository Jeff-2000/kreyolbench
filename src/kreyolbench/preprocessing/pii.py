"""PII detection and redaction helpers."""

from __future__ import annotations

import re

EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b")
PHONE_RE = re.compile(r"(?:\+?509[\s.-]?)?\b\d{4}[\s.-]?\d{4}\b")
ID_RE = re.compile(r"\b(?:NIF|CIN|ID)[:\s-]*[A-Za-z0-9-]{4,}\b", re.I)


def detect_pii(text: str) -> list[str]:
    labels = []
    if EMAIL_RE.search(text):
        labels.append("email")
    if PHONE_RE.search(text):
        labels.append("phone")
    if ID_RE.search(text):
        labels.append("id")
    return labels


def redact_pii(text: str) -> str:
    text = EMAIL_RE.sub("[EMAIL]", text)
    text = PHONE_RE.sub("[PHONE]", text)
    return ID_RE.sub("[ID]", text)

