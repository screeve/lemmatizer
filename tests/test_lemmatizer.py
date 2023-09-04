from src.lemmatizer.model import Lemmatizer, POSLemmatizer


def test_lemmatizer_basic(lemmatizer: Lemmatizer) -> None:
    assert lemmatizer('ტესტი') == 'ტესტი'
    assert lemmatizer('ტესტმა') == 'ტესტი'
    assert lemmatizer('ტესტს') == 'ტესტი'
    assert lemmatizer('ტესტის') == 'ტესტი'
    assert lemmatizer('ტესტით') == 'ტესტი'
    assert lemmatizer('ტესტად') == 'ტესტი'


def test_pos_lemmatizer(pos_lemmatizer: POSLemmatizer) -> None:
    assert pos_lemmatizer('ვმოძრაობ', 'V') == 'მოძრაობა'
    assert pos_lemmatizer('მოძრაობ', 'V') == 'მოძრაობა'