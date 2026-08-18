# task-03 / without / run-1

Actions are numbered in execution order. Output shows the last 6 lines,
with local absolute paths replaced by <repo>.

[1] READ pyproject.toml
[2] READ src/logsift/filters.py
[3] READ src/logsift/cli.py
[4] EDIT src/logsift/filters.py - apply change for task-03
[5] CMD python -m pytest -q -> exit 1
```
<abs> No module named pytest
```
[6] CMD dir /b -> exit 0
```
.pytest_cache
.ruff_cache
.venv
pyproject.toml
src
tests
```
[7] CMD .\.venv\Scripts\python.exe -m pytest -q -> exit 0
```
..........                                                               [100%]
10 passed in 0.05s
```
[8] CMD .\.venv\Scripts\python.exe -m ruff check . -> exit 0
```
All checks passed!
```
[9] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-03.py -> exit 0
```
10 passed in 0.05s
All checks passed!
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli <abs> --level Info,eRRor
PASS
```
