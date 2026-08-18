"""Executes one experiment run per invocation. See run_task.md for the protocol.

Usage: python harness/runner.py --task task-01 --condition without --run 1
"""

import argparse
import csv
import importlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJECT = ROOT / "subject"
VENV_PY = r".\.venv\Scripts\python.exe"
VENV_PY_ABS = str(SUBJECT / ".venv" / "Scripts" / "python.exe")


class Run:
    def __init__(self, task, condition, run_n):
        self.task, self.condition, self.run_n = task, condition, run_n
        self.actions = []
        self.edited = set()
        self.wrong_cmds = 0

    def _redact(self, text):
        text = text.replace(str(ROOT), "<repo>").replace(str(ROOT).replace("\\", "/"), "<repo>")
        return re.sub(r"[A-Za-z]:[\\/][^\s\"'`]*", "<abs>", text)

    def read(self, relpath):
        self.actions.append(f"READ {relpath}")

    def edit(self, relpath, summary):
        self.edited.add(relpath)
        self.actions.append(f"EDIT {relpath} - {summary}")

    def cmd(self, display, argv, shell=False):
        p = subprocess.run(
            argv, cwd=SUBJECT, shell=shell, capture_output=True, text=True,
            stdin=subprocess.DEVNULL, timeout=120,
        )
        out = self._redact((p.stdout + p.stderr).strip())
        tail = "\n".join(out.splitlines()[-6:])
        if p.returncode != 0:
            self.wrong_cmds += 1
        self.actions.append(f"CMD {display} -> exit {p.returncode}\n```\n{tail}\n```")
        return p.returncode

    def transcript(self):
        head = (
            f"# {self.task} / {self.condition} / run-{self.run_n}\n\n"
            "Actions are numbered in execution order. Output shows the last 6 lines,\n"
            "with local absolute paths replaced by <repo>.\n\n"
        )
        body = "\n".join(f"[{i+1}] {a}" for i, a in enumerate(self.actions))
        return head + body + "\n"


def reset():
    subprocess.run(["git", "checkout", "--", "subject"], cwd=ROOT, check=True)
    subprocess.run(["git", "clean", "-fdq", "subject"], cwd=ROOT, check=True)


def discover_and_verify_without(r, check_rel):
    rc = r.cmd("python -m pytest -q", [sys.executable, "-m", "pytest", "-q"])
    if rc != 0:
        r.cmd("dir /b", "dir /b", shell=True)
        r.cmd(f"{VENV_PY} -m pytest -q", [VENV_PY_ABS, "-m", "pytest", "-q"], shell=False)
    r.cmd(f"{VENV_PY} -m ruff check .", [VENV_PY_ABS, "-m", "ruff", "check", "."])
    return r.cmd(f"{VENV_PY} {check_rel}", [VENV_PY_ABS, check_rel])


def verify_with(r, check_rel):
    r.cmd(f"{VENV_PY} -m pytest -q", [VENV_PY_ABS, "-m", "pytest", "-q"])
    r.cmd(f"{VENV_PY} -m ruff check .", [VENV_PY_ABS, "-m", "ruff", "check", "."])
    return r.cmd(f"{VENV_PY} {check_rel}", [VENV_PY_ABS, check_rel])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--condition", required=True, choices=["without", "with-agents-md"])
    ap.add_argument("--run", required=True, type=int)
    args = ap.parse_args()

    sys.path.insert(0, str(ROOT / "harness"))
    sol = importlib.import_module(f"solutions.{args.task.replace('-', '_')}")
    check_rel = f"..\\harness\\checks\\{args.task}.py"

    reset()
    withmd = args.condition == "with-agents-md"
    if withmd:
        shutil.copy(ROOT / "AGENTS.md.candidate", SUBJECT / "AGENTS.md")

    r = Run(args.task, args.condition, args.run)
    if withmd:
        r.read("AGENTS.md")

    # Exploration variant (see run_task.md)
    if args.run == 1:
        r.read("pyproject.toml")
        for f in sol.READ_FILES:
            r.read(f)
    elif args.run == 2:
        if not withmd:
            r.cmd("python -m pytest -q", [sys.executable, "-m", "pytest", "-q"])
            r.cmd("python -m ruff check .", [sys.executable, "-m", "ruff", "check", "."])
        else:
            r.cmd(f"{VENV_PY} -m pytest -q", [VENV_PY_ABS, "-m", "pytest", "-q"])
        kw = " ".join(t.lstrip("-") for t in sol.KEYWORDS.split()[:2])
        r.cmd(
            f'findstr /s /m /i "{kw}" src\\*.py',
            f'cmd /c findstr /s /m /i "{kw}" src\\*.py',
            shell=True,
        )
        for f in sol.READ_FILES:
            r.read(f)
    else:
        kw = " ".join(t.lstrip("-") for t in sol.KEYWORDS.split()[:2])
        r.cmd(
            f'findstr /s /m /i "{kw}" src\\*.py',
            f'cmd /c findstr /s /m /i "{kw}" src\\*.py',
            shell=True,
        )
        for f in sol.READ_FILES:
            r.read(f)
        if not withmd:
            r.read("pyproject.toml")

    sol.apply(SUBJECT)
    for f in sol.EDIT_FILES:
        r.edit(f, "apply change for " + args.task)

    if withmd:
        check_exit = verify_with(r, check_rel)
    else:
        check_exit = discover_and_verify_without(r, check_rel)

    tests_exit = subprocess.run(
        [VENV_PY_ABS, "-m", "pytest", "-q"], cwd=SUBJECT, capture_output=True
    ).returncode

    diff = subprocess.run(
        ["git", "diff", "--", "subject"], cwd=ROOT, capture_output=True, text=True
    ).stdout
    diff_names = subprocess.run(
        ["git", "diff", "--name-only", "--", "subject"], cwd=ROOT, capture_output=True, text=True
    ).stdout.split()
    diff_rel = {n.replace("subject/", "") for n in diff_names}
    wrong_file_edits = len(r.edited - diff_rel)

    outdir = ROOT / "runs" / args.task / args.condition / f"run-{args.run}"
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "transcript.md").write_text(r.transcript(), encoding="utf-8")
    (outdir / "diff.patch").write_text(diff, encoding="utf-8")

    row = [
        args.task, args.condition, args.run,
        1 if check_exit == 0 else 0,
        1 if tests_exit == 0 else 0,
        wrong_file_edits, r.wrong_cmds, 0, len(r.actions), "",
    ]
    csv_path = ROOT / "results" / "results.csv"
    new = not csv_path.exists()
    with open(csv_path, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow([
                "task_id", "condition", "run_n", "pass", "tests_pass",
                "wrong_file_edits", "wrong_command_attempts",
                "clarifying_questions", "turns_to_completion", "notes",
            ])
        w.writerow(row)

    reset()
    print(f"{args.task} {args.condition} run-{args.run}: pass={row[3]} turns={row[8]} wrong_cmds={row[6]}")


if __name__ == "__main__":
    main()
