from logsift.filters import by_level, by_substring
from logsift.parser import Record

RECS = [
    Record("t1", "INFO", "server started"),
    Record("t2", "ERROR", "disk full"),
    Record("t3", "INFO", "request served"),
]


def test_by_level_case_insensitive():
    assert len(by_level(RECS, "info")) == 2


def test_by_substring():
    assert [r.ts for r in by_substring(RECS, "disk")] == ["t2"]
