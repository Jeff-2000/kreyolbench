from kreyolbench.io import read_jsonl
from kreyolbench.schemas import validate_row


def test_sample_ner_validates():
    row = read_jsonl("data/sample/ner.jsonl")[0]
    validated = validate_row(row)
    assert validated.task == "ner"
    assert validated.input["tokens"][0] == "MSPP"


def test_all_sample_rows_validate():
    for path in [
        "data/sample/classification_topic.jsonl",
        "data/sample/sentiment.jsonl",
        "data/sample/ner.jsonl",
        "data/sample/qa.jsonl",
        "data/sample/retrieval.jsonl",
        "data/sample/normalization.jsonl",
        "data/sample/codeswitch.jsonl",
        "data/sample/translation.jsonl",
        "data/sample/summarization.jsonl",
    ]:
        for row in read_jsonl(path):
            assert validate_row(row).id

