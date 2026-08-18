# agents-md-experiment

A before/after measurement of whether an AGENTS.md file changes coding-agent
behavior on a small repository the agent has not worked on before.

## Layout

- `subject/` - the codebase the agent works on: a Python CLI named logsift
  (source under `src/`, config read from two places, one misleading file name).
- `harness/verified-facts.md` - ground truth. Every fact was established by
  running a command and pasting its output.
- `AGENTS.md.candidate` - the file under test. Every statement carries a tag
  pointing at a fact in verified-facts.md. During `with-agents-md` runs it is
  copied to `subject/AGENTS.md`; during `without` runs it is absent.
- `tasks/task-01.md` through `task-05.md` - five tasks, each with a pass
  condition checked by running a script. Written before any run, frozen since.
- `harness/checks/` - the pass-condition scripts. Frozen with the tasks.
- `harness/run_task.md` - run protocol, information policy, and the known
  limitations of the harness.
- `runs/<task>/<condition>/<run-n>/` - transcript.md and diff.patch per run.
- `results/README.md` - metric definitions, fixed before logging started.
- `results/results.csv` - one row per run, 30 rows.
- `results/summary.md` - per-task pass rates, spread across runs, and the
  metrics on which the conditions were indistinguishable.

## Reproducing

Requirements: Python 3.10+, git, PowerShell (commands in the docs use Windows
path separators; the Python code itself is platform-neutral).

1. `cd subject`
2. `python -m venv .venv`
3. `.\.venv\Scripts\python.exe -m pip install --upgrade pip`
4. `.\.venv\Scripts\python.exe -m pip install -e .[dev]`
5. `.\.venv\Scripts\python.exe -m pytest -q` (expect 10 passed)
6. Follow `harness/run_task.md` for the run matrix.

## Scope

The measured subject is the harness policy described in
`harness/run_task.md`, executed on one small codebase, three runs per cell.
The sample is too small to support general claims; see
`results/summary.md` for what was and was not observed.
