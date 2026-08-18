import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import cli, finish, suite_and_lint

LOG = (
    "t1 DEBUG a\n"
    "t2 INFO b\n"
    "t3 TRACE odd\n"
    "t4 WARNING c\n"
    "t5 ERROR d\n"
)


def lines(p):
    return p.stdout.strip().splitlines() if p.stdout.strip() else []


def functional() -> bool:
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        f = td / "s.log"
        f.write_text(LOG)

        (td / "logsift.toml").write_text('min_level = "WARNING"\n')
        p = cli(["s.log"], cwd=td, drop_env=["LOGSIFT_CONFIG"])
        got = [ln.split()[0] for ln in lines(p)]
        if got != ["t3", "t4", "t5"]:
            print("FAIL: local min_level=WARNING gave:", got, p.stderr)
            return False

        envf = td / "env.toml"
        envf.write_text('min_level = "DEBUG"\n')
        p = cli(["s.log"], cwd=td, extra_env={"LOGSIFT_CONFIG": str(envf)})
        if len(lines(p)) != 5:
            print("FAIL: env override to DEBUG gave:", lines(p))
            return False

        (td / "logsift.toml").write_text('min_level = "ERROR"\n')
        p = cli(["s.log", "--level", "info"], cwd=td, drop_env=["LOGSIFT_CONFIG"])
        got = [ln.split()[0] for ln in lines(p)]
        if got != ["t2"]:
            print("FAIL: --level precedence gave:", got)
            return False
    return True


if __name__ == "__main__":
    finish(suite_and_lint() and functional())
