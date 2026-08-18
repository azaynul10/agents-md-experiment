import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import cli, finish, suite_and_lint

LOG = (
    "2024-01-01T00:00:00 INFO request served in 12ms\n"
    "2024-01-01T00:00:01 ERROR disk almost full\n"
    "2024-01-01T00:00:02 INFO request served in 340ms\n"
)


def functional() -> bool:
    from logsift.filters import by_regex
    from logsift.parser import parse_lines

    recs = parse_lines(LOG.splitlines())
    got = by_regex(recs, r"in \d{3}ms")
    if [r.ts for r in got] != ["2024-01-01T00:00:02"]:
        print("FAIL: by_regex wrong result:", got)
        return False

    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "s.log"
        f.write_text(LOG)
        p = cli([str(f), "--regex", r"disk .* full"], drop_env=["LOGSIFT_CONFIG"])
        if p.returncode != 0 or p.stdout.strip().splitlines() != [
            "2024-01-01T00:00:01 ERROR disk almost full"
        ]:
            print("FAIL: --regex CLI output:", repr(p.stdout), p.stderr)
            return False
    return True


if __name__ == "__main__":
    finish(suite_and_lint() and functional())
