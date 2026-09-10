import json
from pathlib import Path


ROOT = Path(__file__).parents[1]


def _label_config(name: str) -> str:
    path = ROOT / "annotation" / "label_studio" / f"{name}.json"
    return json.loads(path.read_text(encoding="utf-8"))["label_config"]


def test_classification_template_is_multilabel():
    config = _label_config("classification")
    assert 'name="labels"' in config
    assert 'choice="multiple"' in config
    assert 'name="uncertainty"' in config
    assert 'name="other_justification"' in config


def test_ner_template_contains_complete_candidate_taxonomy():
    config = _label_config("ner")
    for label in ("MONEY", "PERCENT", "PRODUCT", "LAW_POLICY"):
        assert f'value="{label}"' in config


def test_codeswitch_template_factorizes_language_contact_annotations():
    config = _label_config("codeswitch")
    assert 'name="language_id"' in config
    assert 'name="token_type"' in config
    assert 'name="contact_status"' in config
    assert 'name="uncertainty"' in config
    assert 'value="ESTABLISHED_BORROWING"' in config
    assert "sentence_lang" not in config


def test_normalization_template_uses_orthography_only_edit_types():
    config = _label_config("normalization")
    assert 'name="decision"' in config
    assert 'name="references"' in config
    assert 'name="core_edit_type"' in config
    assert 'name="auxiliary_edit_type"' in config
    assert 'name="rule_ids"' in config
    assert 'value="spacing"' in config
    assert "split_merge" not in config
