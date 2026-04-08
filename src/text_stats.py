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
