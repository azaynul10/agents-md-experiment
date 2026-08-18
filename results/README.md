# Metric definitions

Defined before the first run. Not changed afterwards. One CSV row per run.

- task_id: task-01 through task-05.
- condition: `with-agents-md` (AGENTS.md present at `subject/AGENTS.md`) or
  `without` (file absent). The file content is `AGENTS.md.candidate` verbatim.
- run_n: 1, 2, or 3. Each run number uses the exploration variant of the same
  number defined in `harness/run_task.md`.
- pass: 1 if the task's check script (`harness/checks/task-NN.py`) exits 0 at
  the end of the run, else 0.
- tests_pass: 1 if `.\.venv\Scripts\python.exe -m pytest -q` exits 0 in
  `subject/` at the end of the run, else 0.
- wrong_file_edits: number of files modified at any point during the run that
  are not part of the final `diff.patch`, plus any file modified that the task
  text names as off-limits. Reverted edits count.
- wrong_command_attempts: number of shell commands executed during the run
  that exited nonzero. Commands run deliberately to observe a documented
  failure still count; the transcript marks each.
- clarifying_questions: number of times the agent stopped to ask the user a
  question instead of acting.
- turns_to_completion: total number of agent actions in the transcript (file
  reads, file edits, and shell commands each count as one action) from start
  until the final check invocation, inclusive.
- notes: free text; must not introduce new metrics.
