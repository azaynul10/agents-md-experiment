# task-02 / without / run-3

Actions are numbered in execution order. Output shows the last 6 lines,
with local absolute paths replaced by <repo>.

[1] CMD findstr /s /m /i "ConfigError load_config" src\*.py -> exit 0
```
src\logsift\cli.py
src\logsift\config.py
```
[2] READ src/logsift/config.py
[3] READ pyproject.toml
[4] EDIT src/logsift/config.py - apply change for task-02
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
[9] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-02.py -> exit 0
```
..........                                                               [100%]
10 passed in 0.06s
All checks passed!
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
PASS
```
