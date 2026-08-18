# task-04 / without / run-2

Actions are numbered in execution order. Output shows the last 6 lines,
with local absolute paths replaced by <repo>.

[1] CMD python -m pytest -q -> exit 1
```
<abs> No module named pytest
```
[2] CMD python -m ruff check . -> exit 1
```
<abs> No module named ruff
```
[3] CMD findstr /s /m /i "version __version__" src\*.py -> exit 0
```
src\logsift\__init__.py
```
[4] READ src/logsift/cli.py
[5] READ src/logsift/__init__.py
[6] READ pyproject.toml
[7] EDIT src/logsift/cli.py - apply change for task-04
[8] CMD python -m pytest -q -> exit 1
```
<abs> No module named pytest
```
[9] CMD dir /b -> exit 0
```
.pytest_cache
.ruff_cache
.venv
pyproject.toml
src
tests
```
[10] CMD .\.venv\Scripts\python.exe -m pytest -q -> exit 0
```
..........                                                               [100%]
10 passed in 0.05s
```
[11] CMD .\.venv\Scripts\python.exe -m ruff check . -> exit 0
```
All checks passed!
```
[12] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-04.py -> exit 0
```
All checks passed!
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli --version
+ git diff --name-only HEAD -- src/logsift/main.py
PASS
```
