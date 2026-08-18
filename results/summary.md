# Results summary

30 runs: 5 tasks x 2 conditions x 3 runs. Metric definitions are in
results/README.md. The agent policy and its limitations are in
harness/run_task.md; the variance caveat there applies to every number below.

## Pass rates

Every run passed in both conditions. Per task: 3/3 without, 3/3 with-agents-md,
for all five tasks. The pass metric did not separate the conditions.

## turns_to_completion

Per-task values across run-1/run-2/run-3, with the per-task mean:

| task    | without      | mean | with-agents-md | mean |
|---------|--------------|------|----------------|------|
| task-01 | 10, 12, 11   | 11.0 | 9, 10, 9       | 9.3  |
| task-02 | 8, 10, 9     | 9.0  | 7, 8, 7        | 7.3  |
| task-03 | 9, 11, 10    | 10.0 | 8, 9, 8        | 8.3  |
| task-04 | 10, 12, 11   | 11.0 | 9, 10, 9       | 9.3  |
| task-05 | 9, 11, 10    | 10.0 | 8, 9, 8        | 8.3  |

Condition means: 10.2 without, 8.5 with-agents-md; mean gap 1.7 turns per run.
The within-condition spread across the three runs of a task is 2 turns in the
without condition. That spread exceeds the between-condition mean gap of 1.7,
so at the level of individual runs the two conditions overlap: the fastest
without run of a task (its run-1) uses fewer turns than the slowest
with-agents-md run of the same task (its run-2) in no case, but the ranges
adjoin within one turn. The gap is also structural rather than emergent: the
without policy must discover the interpreter and test commands (one failed
system-interpreter attempt plus one directory listing), while the with
condition spends one action reading AGENTS.md and skips discovery. The
difference measures exactly that trade and nothing else.

## wrong_command_attempts

Per-task values across run-1/run-2/run-3:

| task    | without   | with-agents-md |
|---------|-----------|----------------|
| task-01 | 1, 4, 2   | 0, 1, 1        |
| task-02 | 1, 3, 1   | 0, 0, 0        |
| task-03 | 1, 3, 1   | 0, 0, 0        |
| task-04 | 1, 3, 1   | 0, 0, 0        |
| task-05 | 1, 3, 1   | 0, 0, 0        |

Totals: 27 without (mean 1.8 per run), 2 with-agents-md (mean 0.13). The
without failures are attempts to run pytest and ruff through the system
interpreter, which lacks the dev dependencies; AGENTS.md names the venv
commands, so those attempts do not occur. The two with-agents-md failures on
task-01 are a findstr search returning no match for a not-yet-written function
name, which counts under the metric definition even though it is a search
miss, not a command-discovery failure. The task-01 without runs contain the
same search miss, so the per-task contrast is unaffected by it.

## Metrics on which the conditions were indistinguishable

- pass: 15/15 in both conditions.
- tests_pass: 15/15 in both conditions.
- wrong_file_edits: 0 in all 30 runs. The task-04 trap (a misleading main.py)
  produced no wrong-file edit in either condition, because the scripted policy
  never selects a file by name resemblance; a policy that did could behave
  differently, and this harness cannot observe that.
- clarifying_questions: 0 in all 30 runs; the scripted policy never asks.

## Limitations

The sample is 3 runs per cell on one small synthetic codebase with one
scripted agent policy, which is too small and too constrained to generalize.
Within-condition variance comes only from three fixed exploration variants,
not from model sampling, so the spread figures understate the variance a
stochastic agent would show. The same session that wrote the codebase also
executed the runs, so the no-prior-knowledge premise holds only as far as the
information policy in harness/run_task.md enforces it.
