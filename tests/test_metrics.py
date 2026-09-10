from kreyolbench.evaluation.metrics import (
    character_span_scores,
    classification_scores,
    multilabel_classification_scores,
    normalization_reference_scores,
    normalization_scores,
    qa_scores,
    retrieval_scores,
    span_f1,
    token_classification_scores,
    token_accuracy,
)


def test_classification_scores():
    scores = classification_scores(["health", "other"], ["health", "health"])
    assert scores["accuracy"] == 0.5
    assert 0.0 <= scores["macro_f1"] <= 1.0


def test_multilabel_classification_scores():
    scores = multilabel_classification_scores(
        [["health", "disaster_response"], ["education"]],
        [["health", "disaster_response"], ["health"]],
    )
    assert scores["subset_accuracy"] == 0.5
    assert 0.0 < scores["macro_f1"] < 1.0


def test_span_f1():
    scores = span_f1([["B-ORG", "O"]], [["B-ORG", "O"]])
    assert scores["span_f1"] == 1.0


def test_character_span_scores_support_nested_entities():
    entities = [
        {"start_char": 0, "end_char": 11, "label": "ORG"},
        {"start_char": 0, "end_char": 4, "label": "ORG"},
    ]
    assert character_span_scores([entities], [entities])["span_f1"] == 1.0


def test_direct_token_classification_does_not_use_bio_spans():
    scores = token_classification_scores(
        [["hat", "hat", "eng", "zxx"]],
        [["hat", "hat", "eng", "zxx"]],
    )
    assert scores["token_accuracy"] == 1.0
    assert scores["macro_f1"] == 1.0


def test_qa_scores():
    scores = qa_scores(["lendi rive vandredi"], [["lendi rive vandredi"]])
    assert scores["exact_match"] == 1.0


def test_retrieval_scores():
    scores = retrieval_scores([["doc1", "doc2"]], [{"doc1": 3, "doc2": 0}], k=2)
    assert scores["mrr_at_2"] == 1.0
    assert scores["recall_at_2"] == 1.0
    assert scores["judged_at_2"] == 1.0
    assert scores["bpref"] == 1.0


def test_retrieval_scores_report_incomplete_judgment_coverage():
    scores = retrieval_scores([["doc1", "unjudged"]], [{"doc1": 3}], k=2)
    assert scores["judged_at_2"] == 0.5
    assert scores["bpref"] == 0.0


def test_normalization_scores():
    assert normalization_scores(["mwen pa"], ["mwen pa"])["exact_match"] == 1.0
    assert token_accuracy([["a"]], [["a"]]) == 1.0


def test_normalization_reference_scores_accept_alternatives():
    scores = normalization_reference_scores(
        ["M pa konnen si l ap vini"],
        [["M pa konnen si l ap vini", "M pa konnen si l'ap vini"]],
    )
    assert scores["exact_match_any_reference"] == 1.0
