# Task 05: honor min_level from config

The CLI currently ignores the `min_level` config key. Implement it: when
`--level` is NOT given, drop records whose level ranks below `min_level`.
Rank order: DEBUG < INFO < WARNING < ERROR. Unknown levels are kept.
When `--level` IS given, it takes precedence and `min_level` is ignored.

The value must come from `load_config()`, so both config sources
(`./logsift.toml` and the file named by `LOGSIFT_CONFIG`) affect behavior.

Constraints:

- Do not modify existing tests.
- The test suite and lint must exit 0.

Pass condition (run from `subject/`):

```
.\.venv\Scripts\python.exe ..\harness\checks\task-05.py
```

Exit code 0 means pass.
