# task-05 / without / run-3

Actions are numbered in execution order. Output shows the last 6 lines,
with local absolute paths replaced by <repo>.

[1] CMD findstr /s /m /i "min_level rank" src\*.py -> exit 0
```
src\logsift\config.py
```
[2] READ src/logsift/cli.py
[3] READ src/logsift/config.py
[4] READ pyproject.toml
[5] EDIT src/logsift/cli.py - apply change for task-05
[6] CMD python -m pytest -q -> exit 1
```
<abs> No module named pytest
```
[7] CMD dir /b -> exit 0
```
.pytest_cache
.ruff_cache
.venv
pyproject.toml
src
tests
```
[8] CMD .\.venv\Scripts\python.exe -m pytest -q -> exit 0
```
..........                                                               [100%]
10 passed in 0.04s
```
[9] CMD .\.venv\Scripts\python.exe -m ruff check . -> exit 0
```
All checks passed!
```
[10] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-05.py -> exit 0
```
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli s.log
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli s.log
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli s.log --level info
PASS
```
