"""HTML and PDF extraction helpers."""

from __future__ import annotations

import re
from pathlib import Path


def extract_html_text(html: str) -> str:
    try:
        import trafilatura

        extracted = trafilatura.extract(html)
        if extracted:
            return clean_whitespace(extracted)
    except Exception:
        pass
    text = re.sub(r"<script\b[^<]*(?:(?!</script>)<[^<]*)*</script>", " ", html, flags=re.I)
    text = re.sub(r"<style\b[^<]*(?:(?!</style>)<[^<]*)*</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return clean_whitespace(text)


def extract_pdf_text(path: str | Path) -> str:
    try:
        import fitz
    except Exception as exc:
        raise RuntimeError("PDF extraction requires pymupdf") from exc
    parts = []
    with fitz.open(path) as doc:
        for page in doc:
            parts.append(page.get_text("text"))
    return clean_whitespace("\n".join(parts))


def clean_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

