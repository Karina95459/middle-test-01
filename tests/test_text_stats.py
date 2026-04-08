import pytest

from src.text_stats import count_sentences, count_words


@pytest.mark.parametrize(
    "text, expected_words",
    [
        ("Hello world.", 2),
        ("Hello, world!", 2),
        ("One: two; three", 3),
        ("", 0),
        ("Python   is great.", 3),
        ("Hi... Bye!", 2),
    ],
)
def test_count_words(text, expected_words):
    assert count_words(text) == expected_words

@pytest.mark.parametrize(
    "text, expected_sentences",
    [
        ("Hello world.", 1),
        ("Hello! How are you?", 2),
        ("One... Two... Three...", 3),
        ("", 0),
        ("No endings here", 0),
        ("Hi! Bye? Yes.", 3),
    ],
)
def test_count_sentences(text, expected_sentences):
    assert count_sentences(text) == expected_sentences