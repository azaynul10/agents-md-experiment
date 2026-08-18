# task-05 / without / run-1

Actions are numbered in execution order. Output shows the last 6 lines,
with local absolute paths replaced by <repo>.

[1] READ pyproject.toml
[2] READ src/logsift/cli.py
[3] READ src/logsift/config.py
[4] EDIT src/logsift/cli.py - apply change for task-05
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
10 passed in 0.04s
```
[8] CMD .\.venv\Scripts\python.exe -m ruff check . -> exit 0
```
All checks passed!
```
[9] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-05.py -> exit 0
```
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli s.log
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli s.log
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli s.log --level info
PASS
```
