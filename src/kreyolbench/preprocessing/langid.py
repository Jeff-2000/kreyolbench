"""Small lexical language identifier for planning and filtering."""

from __future__ import annotations

import re
from collections import Counter

LEXICONS = {
    "hat": {"mwen", "nou", "yo", "ak", "pou", "nan", "pa", "gen", "lavi", "sante", "lekòl"},
    "fra": {"le", "la", "les", "des", "pour", "dans", "avec", "santé", "école", "publique"},
    "eng": {"the", "and", "for", "with", "health", "school", "appointment", "public"},
    "spa": {"el", "la", "los", "para", "con", "salud", "escuela", "publico"},
}


def classify_sentence(text: str) -> str:
    tokens = re.findall(r"[\wÀ-ÿ']+", text.casefold())
    counts = Counter()
    for token in tokens:
        for lang, lexicon in LEXICONS.items():
            if token in lexicon:
                counts[lang] += 1
    positive = [lang for lang, count in counts.items() if count > 0]
    if not positive:
        return "unknown"
    if len(positive) > 1 and counts.most_common(1)[0][1] < sum(counts.values()):
        return "mixed"
    return counts.most_common(1)[0][0]

