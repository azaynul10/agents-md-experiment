# task-05 / without / run-2

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
[3] CMD findstr /s /m /i "min_level rank" src\*.py -> exit 0
```
src\logsift\config.py
```
[4] READ src/logsift/cli.py
[5] READ src/logsift/config.py
[6] EDIT src/logsift/cli.py - apply change for task-05
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
[11] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-05.py -> exit 0
```
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli s.log
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli s.log
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli s.log --level info
PASS
```
