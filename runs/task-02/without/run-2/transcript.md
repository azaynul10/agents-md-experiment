# task-02 / without / run-2

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
[3] CMD findstr /s /m /i "ConfigError load_config" src\*.py -> exit 0
```
src\logsift\cli.py
src\logsift\config.py
```
[4] READ src/logsift/config.py
[5] EDIT src/logsift/config.py - apply change for task-02
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
10 passed in 0.05s
```
[9] CMD .\.venv\Scripts\python.exe -m ruff check . -> exit 0
```
All checks passed!
```
[10] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-02.py -> exit 0
```
..........                                                               [100%]
10 passed in 0.05s
All checks passed!
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
PASS
```
