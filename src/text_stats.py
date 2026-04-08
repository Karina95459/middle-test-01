import re
from pathlib import Path


def read_text_file(file_path: str) -> str:
    path = Path(file_path)

    if path.suffix.lower() != ".txt":
        raise ValueError("The file must have a .txt extension.")

    return path.read_text(encoding="utf-8")


def count_sentences(text: str) -> int:
    matches = re.findall(r"\.\.\.|[.!?]", text)
    return len(matches)

def count_words(text: str) -> int:
    cleaned_text = re.sub(r"\.\.\.|[.!?]", " ", text)
    parts = re.split(r"[,\s:;]+", cleaned_text)
    words = [part for part in parts if part]
    return len(words)

def get_text_statistics(file_path: str) -> dict:
    text = read_text_file(file_path)
    return {
        "words": count_words(text),
        "sentences": count_sentences(text),
    }

if __name__ == "__main__":
    input_path = input("Enter path to .txt file: ").strip()

    try:
        stats = get_text_statistics(input_path)
        print(f"Words: {stats['words']}")
        print(f"Sentences: {stats['sentences']}")
    except Exception as error:
        print(f"Error: {error}")