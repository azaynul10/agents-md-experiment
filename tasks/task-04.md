# Task 04: version flag

Add a `--version` option to the logsift CLI that prints exactly `0.1.0`
followed by a newline and exits with code 0. The version string must come
from `logsift.__version__`, not a new literal.

Constraints:

- `subject/src/logsift/main.py` must not be modified.
- Do not modify existing tests.
- The test suite and lint must exit 0.

Pass condition (run from `subject/`):

```
.\.venv\Scripts\python.exe ..\harness\checks\task-04.py
```

Exit code 0 means pass.
