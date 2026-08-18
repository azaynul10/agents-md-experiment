import os
import subprocess
import sys


def run(cmd, **kw):
    print("+", " ".join(str(c) for c in cmd))
    return subprocess.run(cmd, **kw)


def suite_and_lint() -> bool:
    if run([sys.executable, "-m", "pytest", "-q"]).returncode != 0:
        print("FAIL: pytest not exit 0")
        return False
    if run([sys.executable, "-m", "ruff", "check", "."]).returncode != 0:
        print("FAIL: ruff not exit 0")
        return False
    return True


def cli(args, cwd=None, extra_env=None, drop_env=()):
    env = dict(os.environ)
    for k in drop_env:
        env.pop(k, None)
    if extra_env:
        env.update(extra_env)
    return run(
        [sys.executable, "-m", "logsift.cli", *args],
        cwd=cwd, env=env, capture_output=True, text=True,
    )


def finish(ok: bool):
    print("PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
