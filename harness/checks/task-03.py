import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import cli, finish, suite_and_lint

LOG = (
    "t1 INFO a\n"
    "t2 ERROR b\n"
    "t3 WARNING c\n"
    "t4 INFO d\n"
)


def functional() -> bool:
    from logsift.filters import by_level
    from logsift.parser import parse_lines

    recs = parse_lines(LOG.splitlines())
    if len(by_level(recs, "info")) != 2:
        print("FAIL: single level broken")
        return False
    got = by_level(recs, "info,error")
    if sorted(r.ts for r in got) != ["t1", "t2", "t4"]:
        print("FAIL: comma list wrong:", [r.ts for r in got])
        return False

    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "s.log"
        f.write_text(LOG)
        p = cli([str(f), "--level", "Info,eRRor"], drop_env=["LOGSIFT_CONFIG"])
        lines = p.stdout.strip().splitlines()
        if p.returncode != 0 or len(lines) != 3:
            print("FAIL: CLI comma list:", lines, p.stderr)
            return False
    return True


if __name__ == "__main__":
    finish(suite_and_lint() and functional())
