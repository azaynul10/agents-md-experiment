from logsift.parser import parse_line, parse_lines


def test_parse_line_valid():
    rec = parse_line("2024-01-01T00:00:00 INFO started")
    assert rec is not None
    assert rec.level == "INFO"
    assert rec.msg == "started"


def test_parse_line_invalid():
    assert parse_line("not a log line at all") is None


def test_parse_lines_skips_invalid():
    lines = ["2024-01-01T00:00:00 ERROR boom", "garbage", "2024-01-01T00:00:01 INFO ok"]
    recs = parse_lines(lines)
    assert len(recs) == 2
