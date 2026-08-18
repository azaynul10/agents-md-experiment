# task-01 / without / run-2

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
[3] CMD findstr /s /m /i "by_regex --regex" src\*.py -> exit 1
```

```
[4] READ src/logsift/filters.py
[5] READ src/logsift/cli.py
[6] EDIT src/logsift/filters.py - apply change for task-01
[7] EDIT src/logsift/cli.py - apply change for task-01
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
[12] CMD .\.venv\Scripts\python.exe ..\harness\checks\task-01.py -> exit 0
```
10 passed in 0.05s
All checks passed!
+ <repo>\subject\.venv\Scripts\python.exe -m pytest -q
+ <repo>\subject\.venv\Scripts\python.exe -m ruff check .
+ <repo>\subject\.venv\Scripts\python.exe -m logsift.cli <abs> --regex disk .* full
PASS
```
