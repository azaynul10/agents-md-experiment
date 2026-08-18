from logsift.parser import Record
from logsift.stats import level_counts, top_messages

RECS = [
    Record("t1", "INFO", "a"),
    Record("t2", "INFO", "a"),
    Record("t3", "ERROR", "b"),
]


def test_level_counts():
    assert level_counts(RECS) == {"INFO": 2, "ERROR": 1}


def test_top_messages():
    assert top_messages(RECS, n=1) == [("a", 2)]
