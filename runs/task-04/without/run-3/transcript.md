# task-04 / without / run-3

Actions are numbered in execution order. Output shows the last 6 lines,
with local absolute paths replaced by <repo>.

[1] CMD findstr /s /m /i "version __version__" src\*.py -> exit 0
```
src\logsift\__init__.py
```
[2] READ src/logsift/cli.py
[3] READ src/logsift/__init__.py
[4] READ pyproject.toml
[5] READ pyproject.toml
[6] EDIT src/logsift/cli.py - apply change for task-04
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
10 passed in 0.10s
```
[10] CMD .\.venv\Scripts\python.exe -m ruff check . -> exit 0
```
All checks passed!
```
[11] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-04.py -> exit 0
```
All checks passed!
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli --version
+ git diff --name-only HEAD -- src/logsift/main.py
PASS
```
