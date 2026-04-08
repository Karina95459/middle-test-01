import pytest

from src.text_stats import count_sentences, count_words,get_text_statistics, read_text_file


@pytest.fixture
def invalid_extension_file(tmp_path):
    file_path = tmp_path / "sample.doc"
    file_path.write_text("Some content", encoding="utf-8")
    return file_path


@pytest.fixture
def sample_text_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello, world! How are you? I am fine...", encoding="utf-8")
    return file_path


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


def test_read_text_file_success(sample_text_file):
    content = read_text_file(str(sample_text_file))
    assert content == "Hello, world! How are you? I am fine..."


def test_read_text_file_invalid_extension(invalid_extension_file):
    with pytest.raises(ValueError, match="The file must have a .txt extension."):
        read_text_file(str(invalid_extension_file))

def test_get_text_statistics(sample_text_file):
    stats = get_text_statistics(str(sample_text_file))
    assert stats == {
        "words": 8,
        "sentences": 3,
    }