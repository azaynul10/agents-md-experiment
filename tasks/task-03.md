# Task 03: multi-level filter

Extend level filtering so `--level` accepts a comma-separated list, e.g.
`--level info,error` keeps records whose level is INFO or ERROR.
`by_level` in `subject/src/logsift/filters.py` must accept both a single
level string and a comma-separated string. Matching stays case-insensitive.

Constraints:

- Do not modify existing tests (they must keep passing unchanged).
- The test suite and lint must exit 0.

Pass condition (run from `subject/`):

```
.\.venv\Scripts\python.exe ..\harness\checks\task-03.py
```

Exit code 0 means pass.
