# Limitations

This is the canonical list. `README.md`, `results/summary.md`,
`RELATED-WORK.md` and the run protocol link here instead of restating it.

Every number referenced below is recomputed from `results/results.csv` by
`results/recompute.py`.

## L1. The executor was a scripted policy, not a language model

Runs were carried out by a fixed script (`harness/runner.py`), which reads a
per-task solution module and replays a predetermined sequence of reads, edits
and commands. It is not an LLM and it does not make decisions. This is the
limitation that governs all the others: the experiment observes what the
script was written to do.

## L2. `wrong_command_attempts` is confounded and carries no evidence

The reported difference (1.80 vs 0.13 attempts per run) is a property of the
script, not a finding about AGENTS.md. In the `with-agents-md` arm the script
was given the file that lists the correct virtualenv commands and it therefore
skipped the discovery step; in the `without` arm it was written to attempt the
system interpreter first and fail. The gap was built into the harness before
any run executed. It is reported for completeness and must not be read as
evidence that a coding agent makes fewer mistakes when AGENTS.md is present.

## L3. No separation on the primary outcome

`pass` was 15/15 in both arms, and `tests_pass` was 15/15 in both arms. The
tasks were solvable from the repository alone, so the check scripts could not
discriminate between the conditions.

## L4. The turn-count difference is within noise and is structural

Turns were 10.2 without vs 8.5 with, a gap of 1.7. The spread across the three
runs of a single task reaches 2 turns inside the `without` arm alone, which
exceeds that gap. Beyond that, the difference is mechanical: the `without`
policy spends actions discovering the interpreter, and the `with-agents-md`
policy spends one action reading AGENTS.md and skips discovery. Reported as
no separation.

## L5. Two instruments never fired, so they are unvalidated

`wrong_file_edits` and `clarifying_questions` were 0 in all 30 runs. task-04
ships a decoy file (`src/logsift/main.py`) whose name invites an edit, and the
trap never once caught anything, because the script selects files from its
solution module rather than by guessing from names. An instrument that never
fires has not been shown to work. Nothing should be concluded from those two
columns in either direction.

## L6. Sample size

30 runs, 15 per arm, 3 runs per cell. No statistical test is reported and none
should be inferred from these tables.

## L7. Variance is understated

Within-arm variation comes only from three fixed exploration variants defined
in `run_task.md`, not from model sampling. A real agent re-run on the same
task varies for reasons this design cannot produce, so the spreads here are
narrower than a genuine agent's would be.

## L8. The experiment cannot speak to cost

Token usage and wall-clock cost were never measured, and could not have been:
a scripted policy consumes no tokens. Any claim about the cost of shipping an
AGENTS.md is outside what this harness observes. See `RELATED-WORK.md` for
published work that does measure cost.

## L9. The author of the codebase also ran the experiment

The same session wrote `subject/`, the tasks, the check scripts and the
AGENTS.md candidate, then executed the runs. The information policy in
`run_task.md` restricts what the executor may read, but prior knowledge cannot
be removed from a single session, so the "unfamiliar codebase" premise holds
only as far as that policy enforces it.

## L10. One small synthetic codebase, one fixed AGENTS.md

The subject is a purpose-built Python CLI of roughly a dozen files, and the
tasks were written by the same author against known solutions. The AGENTS.md
under test is a single fixed 42-line file; the design never varies its
content, length or accuracy, so it says nothing about what a context file
should contain.

## L11. One platform

All runs executed on Windows with PowerShell, using a single Python 3.10
virtualenv. Command discovery behaviour in the `without` arm is specific to
that environment.
