"""Classical baseline helpers."""

from __future__ import annotations

from typing import Any


def train_tfidf_logreg(texts: list[str], labels: list[str]) -> Any:
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression
        from sklearn.pipeline import Pipeline
    except Exception as exc:
        raise RuntimeError("classical baselines require scikit-learn") from exc
    model = Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
            ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )
    return model.fit(texts, labels)


def majority_label(labels: list[str]) -> str:
    if not labels:
        raise ValueError("labels cannot be empty")
    return max(sorted(set(labels)), key=labels.count)

