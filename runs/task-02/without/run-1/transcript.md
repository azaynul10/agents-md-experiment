# task-02 / without / run-1

Actions are numbered in execution order. Output shows the last 6 lines,
with local absolute paths replaced by <repo>.

[1] READ pyproject.toml
[2] READ src/logsift/config.py
[3] EDIT src/logsift/config.py - apply change for task-02
[4] CMD python -m pytest -q -> exit 1
```
<abs> No module named pytest
```
[5] CMD dir /b -> exit 0
```
.pytest_cache
.ruff_cache
.venv
pyproject.toml
src
tests
```
[6] CMD .\.venv\Scripts\python.exe -m pytest -q -> exit 0
```
..........                                                               [100%]
10 passed in 0.06s
```
[7] CMD .\.venv\Scripts\python.exe -m ruff check . -> exit 0
```
All checks passed!
```
[8] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-02.py -> exit 0
```
..........                                                               [100%]
10 passed in 0.04s
All checks passed!
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
PASS
```
