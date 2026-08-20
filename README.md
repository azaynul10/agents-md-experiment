# agents-md-experiment

A small harness that tries to measure whether an AGENTS.md file changes coding
agent behaviour on an unfamiliar repository, and a write-up of why this
attempt could not answer that.

**It found nothing.** Pass rate was 15/15 in both arms. The turn-count gap
(1.7) is smaller than the spread within one arm (2), so: no separation.

**The reason is the executor.** Runs were driven by a scripted policy, not a
language model, so the results describe that script. One metric that does
separate the arms is confounded by construction. Full list:
`harness/LIMITATIONS.md`. Prior, stronger studies: `RELATED-WORK.md`.

**Run it:** `cd subject`, `python -m venv .venv`,
`.\.venv\Scripts\python.exe -m pip install -e .[dev]`, then
`python harness\runner.py --task task-01 --condition without --run 1`.
Verify the numbers with `python results/recompute.py`.

## What the null looks like

Every one of the 30 runs, by turns taken. The two arms overlap:

```
turns per run          7    8    9   10   11   12
                       |    |    |    |    |    |
without  (8-12)             *===================*
with     (7-10)        *==============*
                            |<overlap>|

mean gap between the two arms ................. 1.7 turns
spread across the 3 runs of one task, in
`without` alone ............................... 2 turns  <- exceeds the gap
```

Re-running the same task three times inside one arm moves the turn count more
than switching arms does, so there is no separation to report. Pass rate was
15/15 in both arms, so that metric did not separate them either.

Both figures come from `python results/recompute.py`, which regenerates every
number in this repo from `results/results.csv`.

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
- `harness/runner.py` - the scripted executor. This, not a language model, is
  what produced every run.
- `harness/run_task.md` - run protocol and information policy.
- `harness/LIMITATIONS.md` - **canonical limitations list, L1 to L11.**
  Everything else links here rather than restating it.
- `RELATED-WORK.md` - four public evaluations of context files, all stronger
  designs than this one, and where this repo stands relative to each.
- `runs/<task>/<condition>/<run-n>/` - transcript.md and diff.patch per run.
- `results/README.md` - metric definitions, fixed before logging started.
- `results/results.csv` - one row per run, 30 rows.
- `results/recompute.py` - recomputes every number quoted in this repo from
  the CSV and asserts the dataset shape. Prose defers to its output.
- `results/summary.md` - what the experiment cannot tell you, then what was
  measured, then the no-separation result and the confounded metric.

## Reproducing

Requirements: Python 3.10+, git, PowerShell (commands in the docs use Windows
path separators; the Python code itself is platform-neutral).

1. `cd subject`
2. `python -m venv .venv`
3. `.\.venv\Scripts\python.exe -m pip install --upgrade pip`
4. `.\.venv\Scripts\python.exe -m pip install -e .[dev]`
5. `.\.venv\Scripts\python.exe -m pytest -q` (expect 10 passed)
6. Follow `harness/run_task.md` for the run matrix.
7. `python results/recompute.py` from the repo root to verify every quoted
   number against `results/results.csv`.

## Scope

What was measured is the scripted policy in `harness/runner.py`, on one small
synthetic codebase, three runs per cell. Before citing any number from this
repo, read `harness/LIMITATIONS.md`.

This is an independent experiment. It is not affiliated with, endorsed by, or
reviewed by any foundation or vendor.
