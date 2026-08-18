# Task 02: config error handling

`logsift.config.load_config` currently propagates a raw decode error when a
config file contains invalid TOML. Add a `ConfigError(Exception)` class to
`subject/src/logsift/config.py` and raise it (with the offending path in the
message) when either config source fails to parse.

Constraints:

- Do not modify existing tests.
- The config merge order must not change.
- The test suite and lint must exit 0.

Pass condition (run from `subject/`):

```
.\.venv\Scripts\python.exe ..\harness\checks\task-02.py
```

Exit code 0 means pass.
