from .parser import Record


def by_level(records: list[Record], level: str) -> list[Record]:
    lv = level.upper()
    return [r for r in records if r.level == lv]


def by_substring(records: list[Record], needle: str) -> list[Record]:
    return [r for r in records if needle in r.msg]
