import importlib
import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import cli, finish, run, suite_and_lint


def functional() -> bool:
    p = cli(["--version"], drop_env=["LOGSIFT_CONFIG"])
    if p.returncode != 0 or p.stdout.strip() != "0.1.0":
        print("FAIL: --version output:", repr(p.stdout), p.stderr)
        return False

    d = run(
        ["git", "diff", "--name-only", "HEAD", "--", "src/logsift/main.py"],
        capture_output=True, text=True,
    )
    if d.stdout.strip():
        print("FAIL: main.py was modified")
        return False

    import logsift

    logsift.__version__ = "9.9.9"
    import logsift.cli as cli_mod

    importlib.reload(cli_mod)
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            cli_mod.main(["--version"])
    except SystemExit:
        pass
    if "9.9.9" not in buf.getvalue():
        print("FAIL: version not sourced from logsift.__version__")
        return False
    return True


if __name__ == "__main__":
    finish(suite_and_lint() and functional())
