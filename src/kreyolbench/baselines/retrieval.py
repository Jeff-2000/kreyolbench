"""Retrieval baselines."""

from __future__ import annotations

import math
from collections import Counter, defaultdict


class BM25Index:
    def __init__(self, documents: dict[str, str], k1: float = 1.5, b: float = 0.75) -> None:
        self.documents = documents
        self.k1 = k1
        self.b = b
        self.tokens = {doc_id: text.casefold().split() for doc_id, text in documents.items()}
        self.doc_lengths = {doc_id: len(tokens) for doc_id, tokens in self.tokens.items()}
        self.avgdl = sum(self.doc_lengths.values()) / len(self.doc_lengths) if self.doc_lengths else 0.0
        self.df: Counter[str] = Counter()
        for tokens in self.tokens.values():
            self.df.update(set(tokens))

    def search(self, query: str, k: int = 10) -> list[str]:
        query_terms = query.casefold().split()
        scores = defaultdict(float)
        total_docs = len(self.documents)
        for term in query_terms:
            df = self.df.get(term, 0)
            if not df:
                continue
            idf = math.log(1 + (total_docs - df + 0.5) / (df + 0.5))
            for doc_id, tokens in self.tokens.items():
                tf = tokens.count(term)
                if not tf:
                    continue
                denom = tf + self.k1 * (1 - self.b + self.b * self.doc_lengths[doc_id] / (self.avgdl or 1))
                scores[doc_id] += idf * tf * (self.k1 + 1) / denom
        return [doc_id for doc_id, _ in sorted(scores.items(), key=lambda item: item[1], reverse=True)[:k]]

