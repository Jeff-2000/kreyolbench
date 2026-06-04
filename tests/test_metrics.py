from kreyolbench.evaluation.metrics import (
    classification_scores,
    normalization_scores,
    qa_scores,
    retrieval_scores,
    span_f1,
    token_accuracy,
)


def test_classification_scores():
    scores = classification_scores(["health", "other"], ["health", "health"])
    assert scores["accuracy"] == 0.5
    assert 0.0 <= scores["macro_f1"] <= 1.0


def test_span_f1():
    scores = span_f1([["B-ORG", "O"]], [["B-ORG", "O"]])
    assert scores["span_f1"] == 1.0


def test_qa_scores():
    scores = qa_scores(["lendi rive vandredi"], [["lendi rive vandredi"]])
    assert scores["exact_match"] == 1.0


def test_retrieval_scores():
    scores = retrieval_scores([["doc1", "doc2"]], [{"doc1": 3, "doc2": 0}], k=2)
    assert scores["mrr_at_2"] == 1.0
    assert scores["recall_at_2"] == 1.0


def test_normalization_scores():
    assert normalization_scores(["mwen pa"], ["mwen pa"])["exact_match"] == 1.0
    assert token_accuracy([["a"]], [["a"]]) == 1.0

