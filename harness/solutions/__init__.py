from pathlib import Path


def replace(path: Path, old: str, new: str):
    text = path.read_text()
    assert old in text, f"pattern not found in {path.name}: {old!r}"
    path.write_text(text.replace(old, new, 1))
