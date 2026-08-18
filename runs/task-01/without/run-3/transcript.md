# task-01 / without / run-3

Actions are numbered in execution order. Output shows the last 6 lines,
with local absolute paths replaced by <repo>.

[1] CMD findstr /s /m /i "by_regex --regex" src\*.py -> exit 1
```

```
[2] READ src/logsift/filters.py
[3] READ src/logsift/cli.py
[4] READ pyproject.toml
[5] EDIT src/logsift/filters.py - apply change for task-01
[6] EDIT src/logsift/cli.py - apply change for task-01
[7] CMD python -m pytest -q -> exit 1
```
<abs> No module named pytest
```
[8] CMD dir /b -> exit 0
```
.pytest_cache
.ruff_cache
.venv
pyproject.toml
src
tests
```
[9] CMD .\.venv\Scripts\python.exe -m pytest -q -> exit 0
```
..........                                                               [100%]
10 passed in 0.04s
```
[10] CMD .\.venv\Scripts\python.exe -m ruff check . -> exit 0
```
All checks passed!
```
[11] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-01.py -> exit 0
```
10 passed in 0.04s
All checks passed!
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli <abs> --regex disk .* full
PASS
```
