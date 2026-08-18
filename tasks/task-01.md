# Task 01: regex filter

Add a `by_regex(records, pattern)` function to `subject/src/logsift/filters.py`
that returns records whose `msg` matches the regular expression `pattern`
(using `re.search`). Wire it to a new `--regex PATTERN` CLI option in
`subject/src/logsift/cli.py`, applied after `--level` and `--contains`.

Constraints:

- Do not modify existing tests.
- The test suite and lint must exit 0.

Pass condition (run from `subject/`):

```
.\.venv\Scripts\python.exe ..\harness\checks\task-01.py
```

Exit code 0 means pass.
