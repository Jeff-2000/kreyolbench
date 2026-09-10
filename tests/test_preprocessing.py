from kreyolbench.preprocessing.dedupe import normalized_hash, token_jaccard
from kreyolbench.preprocessing.langid import classify_sentence
from kreyolbench.preprocessing.orthography import normalize_orthography
from kreyolbench.preprocessing.pii import detect_pii, redact_pii
from kreyolbench.preprocessing.sentence import split_sentences
from kreyolbench.preprocessing.unicode import likely_mojibake, normalize_unicode


def test_unicode_cleanup():
    assert normalize_unicode("Mwen\u200b di \u201cwi\u201d") == 'Mwen di "wi"'
    assert likely_mojibake("Ã©cole")


def test_sentence_split_keeps_abbreviation():
    assert split_sentences("Dr. Jan vini. Li pale.") == ["Dr. Jan vini.", "Li pale."]


def test_orthography_preserves_raw():
    result = normalize_orthography("M pa konnen si lap vini")
    assert result.raw_text == "M pa konnen si lap vini"
    assert "l ap" in result.normalized_text
    assert result.normalized_text.startswith("M pa konnen")


def test_default_normalizer_does_not_expand_lexical_variants():
    result = normalize_orthography("m pa konn")

    assert result.normalized_text == "m pa konn"


def test_langid_and_pii():
    assert classify_sentence("Nou bezwen appointment pou sèvis la.") == "mixed"
    assert detect_pii("Ekri test@example.org oswa rele 509 1234 5678") == ["email", "phone"]
    assert "[EMAIL]" in redact_pii("test@example.org")


def test_dedupe_helpers():
    assert normalized_hash("Bonjou!") == normalized_hash("bonjou")
    assert token_jaccard("lave men", "lave men ak savon") > 0.4
