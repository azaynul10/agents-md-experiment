import re
from dataclasses import dataclass

LINE_RE = re.compile(r"^(?P<ts>\S+) (?P<level>[A-Z]+) (?P<msg>.*)$")


@dataclass
class Record:
    ts: str
    level: str
    msg: str


def parse_line(line: str) -> Record | None:
    m = LINE_RE.match(line.strip())
    if not m:
        return None
    return Record(m.group("ts"), m.group("level"), m.group("msg"))


def parse_lines(lines) -> list[Record]:
    out = []
    for ln in lines:
        rec = parse_line(ln)
        if rec is not None:
            out.append(rec)
    return out
