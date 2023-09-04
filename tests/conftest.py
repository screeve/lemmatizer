import pytest

from src.lemmatizer.model import Lemmatizer, POSLemmatizer


@pytest.fixture
def lemmatizer() -> Lemmatizer:
    return Lemmatizer()

@pytest.fixture
def pos_lemmatizer() -> POSLemmatizer:
    return POSLemmatizer()
