import copy

import pytest

from kreyolbench.io import read_jsonl
from kreyolbench.schemas import (
    validate_retrieval_document,
    validate_retrieval_qrel,
    validate_retrieval_query,
    validate_row,
)


def test_sample_ner_validates():
    row = read_jsonl("data/sample/ner.jsonl")[0]
    validated = validate_row(row)
    assert validated.task == "ner"
    assert validated.input["text"].startswith("MSPP")
    assert validated.target["entities"][0]["label"] == "ORG"


def test_all_sample_rows_validate():
    for path in [
        "data/sample/classification_topic.jsonl",
        "data/sample/sentiment.jsonl",
        "data/sample/ner.jsonl",
        "data/sample/qa.jsonl",
        "data/sample/normalization.jsonl",
        "data/sample/codeswitch.jsonl",
        "data/sample/translation.jsonl",
        "data/sample/summarization.jsonl",
    ]:
        for row in read_jsonl(path):
            assert validate_row(row).id


def test_retrieval_artifacts_validate():
    for row in read_jsonl("data/sample/retrieval/corpus.jsonl"):
        assert validate_retrieval_document(row).doc_id
    for row in read_jsonl("data/sample/retrieval/queries.jsonl"):
        assert validate_retrieval_query(row).query_id
    for row in read_jsonl("data/sample/retrieval/qrels.jsonl"):
        assert validate_retrieval_qrel(row).assessor_id


def test_classification_other_must_be_exclusive():
    row = read_jsonl("data/sample/classification_topic.jsonl")[0]
    invalid = copy.deepcopy(row)
    invalid["target"]["labels"] = ["health", "other"]

    with pytest.raises(ValueError, match="must be exclusive"):
        validate_row(invalid)


def test_ner_allows_nesting_but_rejects_crossing_spans():
    row = read_jsonl("data/sample/ner.jsonl")[0]
    nested = copy.deepcopy(row)
    nested["target"]["entities"] = [
        {"entity_id": "e1", "start_char": 0, "end_char": 11, "text": "MSPP anonse", "label": "ORG"},
        {"entity_id": "e2", "start_char": 0, "end_char": 4, "text": "MSPP", "label": "ORG"},
    ]
    assert validate_row(nested).id

    crossing = copy.deepcopy(row)
    crossing["target"]["entities"] = [
        {"entity_id": "e1", "start_char": 0, "end_char": 11, "text": "MSPP anonse", "label": "ORG"},
        {"entity_id": "e2", "start_char": 5, "end_char": 15, "text": "anonse yon", "label": "EVENT"},
    ]
    with pytest.raises(ValueError, match="must not cross"):
        validate_row(crossing)


def test_ner_rejects_discontinuous_pilot_spans():
    row = read_jsonl("data/sample/ner.jsonl")[0]
    invalid = copy.deepcopy(row)
    invalid["target"]["entities"][0]["segments"] = [[0, 2], [3, 4]]

    with pytest.raises(ValueError, match="contiguous spans only"):
        validate_row(invalid)


def test_document_derived_retrieval_query_cannot_enter_test():
    query = read_jsonl("data/sample/retrieval/queries.jsonl")[0]
    invalid = copy.deepcopy(query)
    invalid["query_origin"] = "DOCUMENT_DERIVED_DIAGNOSTIC"

    with pytest.raises(ValueError, match="cannot enter test splits"):
        validate_retrieval_query(invalid)


def test_codeswitch_borrowing_and_uncertainty_contracts():
    row = read_jsonl("data/sample/codeswitch.jsonl")[0]

    invalid_borrowing = copy.deepcopy(row)
    invalid_borrowing["target"]["annotations"][2].update(
        {"language_id": "eng", "contact_status": "ESTABLISHED_BORROWING"}
    )
    with pytest.raises(ValueError, match="borrowings must use language_id hat"):
        validate_row(invalid_borrowing)

    invalid_unknown = copy.deepcopy(row)
    invalid_unknown["target"]["annotations"][2].update(
        {"language_id": "und", "contact_status": "UNCERTAIN", "uncertainty": "NONE"}
    )
    with pytest.raises(ValueError, match="requires an uncertainty reason"):
        validate_row(invalid_unknown)


def test_codeswitch_tokens_must_match_raw_text_offsets():
    row = read_jsonl("data/sample/codeswitch.jsonl")[0]
    invalid = copy.deepcopy(row)
    invalid["input"]["tokens"][2]["start_char"] = 12

    with pytest.raises(ValueError, match="must match raw-text offsets"):
        validate_row(invalid)


def test_normalization_decisions_and_edit_strata():
    row = read_jsonl("data/sample/normalization.jsonl")[0]

    accept_as_is = copy.deepcopy(row)
    accept_as_is["target"] = {
        "decision": "ACCEPT_AS_IS",
        "references": [accept_as_is["input"]["raw_text"]],
        "edits": [],
    }
    assert validate_row(accept_as_is).id

    abstain = copy.deepcopy(row)
    abstain["target"] = {"decision": "ABSTAIN", "references": [], "edits": []}
    assert validate_row(abstain).id

    wrong_stratum = copy.deepcopy(row)
    wrong_stratum["target"]["edits"][0]["evaluation_stratum"] = "AUXILIARY"
    with pytest.raises(ValueError, match="must use CORE stratum"):
        validate_row(wrong_stratum)


def test_provenance_derivation_steps_must_be_contiguous():
    row = read_jsonl("data/sample/classification_topic.jsonl")[0]
    invalid = copy.deepcopy(row)
    invalid["source"]["derivation_steps"] = [
        {"step_id": "step2", "sequence": 2, "type": "OCR"}
    ]

    with pytest.raises(ValueError, match="contiguous"):
        validate_row(invalid)
