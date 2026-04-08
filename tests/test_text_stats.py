import pytest

from src.text_stats import count_words


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