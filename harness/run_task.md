# Run protocol

## Agent under test

Runs are executed by a single scripted agent policy (the same assistant that
built this repository), not by independent fresh agent instances. Two
consequences, stated up front:

1. The "never seen this codebase" premise holds only approximately. The
   policy below constrains what information the agent may act on, but true
   ignorance cannot be enforced within one session.
2. Within-condition variance comes only from the three exploration variants
   below, not from sampling noise in a model. Variance numbers must be read
   with that in mind.

## Information policy

- `without` condition: the agent may read any file inside `subject/` and run
  commands. It starts with no knowledge of install, test, or lint commands and
  must discover them by reading files or trying commands. Every attempt is
  logged.
- `with-agents-md` condition: identical, except `subject/AGENTS.md` exists and
  is read first.
- In both conditions the agent may not read `harness/verified-facts.md`,
  `AGENTS.md.candidate` at the repo root, other tasks, or any `runs/` output.
  The check script for the current task may be executed but not read.

## Exploration variants (fixed before any run)

- run-1: read pyproject.toml first, then source files, then act.
- run-2: try commands first (test, then lint) before reading any file, then
  read only what the failures point to.
- run-3: locate relevant code by searching file contents for task keywords,
  read only matching files, then act.

In the `with-agents-md` condition, AGENTS.md is read before the variant's
first step.

## Per-run procedure

1. Reset: `git checkout -- subject` and `git clean -fd subject` from the repo
   root (removes any AGENTS.md and stray files; `.venv` is git-ignored and
   survives).
2. Condition setup: for `with-agents-md`, copy `AGENTS.md.candidate` to
   `subject/AGENTS.md`. For `without`, do nothing.
3. Execute the task following the variant policy. Log every action in
   `runs/<task>/<condition>/<run-n>/transcript.md` as a numbered list:
   `[n] READ <path>`, `[n] EDIT <path> <summary>`, or `[n] CMD <command> ->
   exit <code>` with trimmed output. Source excerpts are capped at 15 lines.
4. Verify: run the task's check script. Record its exit code.
5. Save `git diff -- subject` (excluding `subject/AGENTS.md`) to `diff.patch`
   in the run directory.
6. Append one row to `results/results.csv` using the definitions in
   `results/README.md`.
7. Reset again before the next run.

## Order of runs

All 15 `without` runs first (task-01 run-1..3, task-02 run-1..3, ...), then
all 15 `with-agents-md` runs in the same order.
