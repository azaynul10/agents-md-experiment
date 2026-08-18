from collections import Counter

from .parser import Record


def level_counts(records: list[Record]) -> dict[str, int]:
    return dict(Counter(r.level for r in records))


def top_messages(records: list[Record], n: int = 3) -> list[tuple[str, int]]:
    return Counter(r.msg for r in records).most_common(n)
