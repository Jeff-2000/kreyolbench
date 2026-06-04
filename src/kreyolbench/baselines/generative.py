"""Generative evaluation prompt templates."""

from __future__ import annotations


PROMPTS = {
    "classification": "Chwazi yon kategori pou tèks sa a: {text}\nKategori:",
    "qa": "Reponn kesyon an an Kreyòl selon kontèks la.\nKontèks: {context}\nKesyon: {question}\nRepons:",
    "normalization": "Ekri fraz sa a nan òtograf Kreyòl estanda san chanje sans li: {raw_text}",
}


def render_prompt(task: str, **kwargs: str) -> str:
    if task not in PROMPTS:
        raise ValueError(f"No prompt template for task {task}")
    return PROMPTS[task].format(**kwargs)

