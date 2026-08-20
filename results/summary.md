# Results summary

Regenerate every number below with `python results/recompute.py`.

## What this experiment cannot tell you

Read this before any number on this page.

**It cannot tell you whether AGENTS.md helps a coding agent.** The runs were
executed by a scripted policy (`harness/runner.py`), not by a language model.
The script replays a predetermined sequence of reads, edits and commands from
a per-task solution module. What the tables below describe is the behaviour of
that script.

**It cannot tell you anything about cost.** Tokens and wall-clock time were
never measured, and a scripted policy has no token cost to measure.

**It cannot tell you that agents make fewer mistakes with AGENTS.md.** The one
metric that separates the two arms is confounded by construction; see
"One confounded metric" below.

**It cannot tell you that agents avoid decoy files.** The task-04 trap never
fired in any of the 30 runs, so that instrument is unvalidated.

The canonical list is `harness/LIMITATIONS.md` (L1 to L11). The rest of this
page assumes it.

## What was actually measured

- **Subject**: `subject/`, a purpose-built Python CLI (logsift) with a `src/`
  layout, config loaded from two sources, and one decoy file.
- **Conditions**: `without` (no AGENTS.md in the repo) and `with-agents-md`
  (a fixed 42-line AGENTS.md copied to `subject/AGENTS.md`).
- **Tasks**: five, in `tasks/task-01.md` to `task-05.md`. Each has a pass
  condition enforced by a frozen script in `harness/checks/`, which runs the
  test suite, the linter, and task-specific functional assertions. Tasks and
  checks were written before any run and not edited afterwards.
- **Runs**: 3 per cell, 30 total. Within-arm variation comes from three fixed
  exploration variants in `harness/run_task.md`, not from model sampling.
- **Metrics**: defined in `results/README.md` before logging began.
- **Artifacts**: a numbered transcript and a `diff.patch` per run under
  `runs/`.

## Result: no separation

**Pass rate.** 15/15 in the `without` arm and 15/15 in the `with-agents-md`
arm. `tests_pass` likewise 15/15 in both. The tasks were solvable from the
repository alone, so the checks could not discriminate between the conditions.

**Turns.** Per task, across run-1/run-2/run-3, with per-task means:

| task    | without      | mean | with-agents-md | mean |
|---------|--------------|------|----------------|------|
| task-01 | 10, 12, 11   | 11.0 | 9, 10, 9       | 9.3  |
| task-02 | 8, 10, 9     | 9.0  | 7, 8, 7        | 7.3  |
| task-03 | 9, 11, 10    | 10.0 | 8, 9, 8        | 8.3  |
| task-04 | 10, 12, 11   | 11.0 | 9, 10, 9       | 9.3  |
| task-05 | 9, 11, 10    | 10.0 | 8, 9, 8        | 8.3  |

Arm means are 10.2 and 8.5, a gap of 1.7 turns. The spread across the three
runs of a single task reaches 2 turns inside the `without` arm by itself,
which is larger than the gap between the arms. **Reported as no separation.**

The gap is also mechanical rather than discovered: the `without` policy spends
actions finding the interpreter and test commands, while the `with-agents-md`
policy spends one action reading AGENTS.md and skips that discovery. It
measures that trade and nothing else. See `harness/LIMITATIONS.md` L4.

**Metrics that were flat everywhere.** `wrong_file_edits` 0 and
`clarifying_questions` 0, in all 30 runs. task-04 ships a decoy
`src/logsift/main.py` whose name invites a wrong edit; **the trap never fired
once, so that instrument is unvalidated** and nothing follows from those two
columns in either direction (`harness/LIMITATIONS.md` L5).

## One confounded metric

`wrong_command_attempts`, per task, across run-1/run-2/run-3:

| task    | without   | with-agents-md |
|---------|-----------|----------------|
| task-01 | 1, 4, 2   | 0, 1, 1        |
| task-02 | 1, 3, 1   | 0, 0, 0        |
| task-03 | 1, 3, 1   | 0, 0, 0        |
| task-04 | 1, 3, 1   | 0, 0, 0        |
| task-05 | 1, 3, 1   | 0, 0, 0        |

Totals: 27 in the `without` arm (1.80 per run) and 2 in the `with-agents-md`
arm (0.13 per run).

**This metric is confounded and is not evidence about AGENTS.md.** The
executor is a scripted policy. In the `with-agents-md` arm the script was
handed the file that lists the correct virtualenv commands, so it never
attempted discovery. In the `without` arm the script was written to try the
system interpreter first, which lacks the dev dependencies, and fail. The
difference was fixed in the harness before the first run executed. Fewer wrong
commands here is a property of the script, not a behaviour of an agent reading
a context file (`harness/LIMITATIONS.md` L2).

The two nonzero cells in the `with-agents-md` arm are task-01 run-2 and run-3,
where a `findstr` search returns no match for a function that does not exist
yet. That is a search miss, not a command-discovery failure, and it counts only
because the metric definition counts any nonzero exit. The same miss occurs in
the corresponding `without` runs.

## What would make a v2 valid

1. **A real LLM executor.** Replace `harness/runner.py` with an actual coding
   agent. Without this, nothing else on the list matters.
2. **A fresh session per run**, so no run inherits knowledge of the subject,
   the tasks, or the checks from the session that wrote them.
3. **At least three model families**, since a single agent's results have
   already been shown elsewhere not to transfer (`RELATED-WORK.md`).
4. **One pre-registered primary endpoint**, declared before runs begin, with
   the secondary metrics marked as exploratory.
5. **Blinded scoring**, so whoever grades a run cannot tell which arm it came
   from.
6. **A trap demonstrated to fire at least once** before it is used as an
   instrument. An unvalidated trap that reads 0 is indistinguishable from a
   broken one.
7. **Cost measured**, in tokens and wall-clock time, which requires item 1.
8. **Enough runs per cell to characterise the noise**, established from pilot
   variance rather than assumed.

