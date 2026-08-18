# Verified facts

Every fact below was established by running the stated command and pasting its
output. Absolute local paths in outputs are replaced with `<abs>` per the
no-local-paths rule. All commands were run from the `subject/` directory on
Windows, PowerShell 5.1, system Python 3.10.

## F1. Editable install fails with old pip (system pip 21.2.3)

Command: `python -m pip install -e .[dev]`

Output (last lines):

```
ERROR: File "setup.py" or "setup.cfg" not found. Directory cannot be installed in editable mode: <abs>\subject
(A "pyproject.toml" file was found, but editable mode currently requires a setuptools-based build.)
WARNING: You are using pip version 21.2.3; however, version 26.2.1 is available.
```

Exit code: 1. A pip new enough for PEP 660 is required for the editable install.

## F2. Virtual environment and pip upgrade succeed

Commands:

```
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip --quiet
.\.venv\Scripts\python.exe -m pip --version
```

Output: `pip 26.2.1 from <abs>\subject\.venv\lib\site-packages\pip (python 3.10)`

## F3. Editable install succeeds inside the venv

Command: `.\.venv\Scripts\python.exe -m pip install -e .[dev]`

Output (last line):

```
Successfully installed colorama-0.4.6 exceptiongroup-1.3.1 iniconfig-2.3.0 logsift-0.1.0 packaging-26.3 pluggy-1.6.0 pygments-2.21.0 pytest-9.1.1 ruff-0.16.3 tomli-2.4.1 typing-extensions-4.16.0
```

Exit code: 0.

## F4. Historical failure: `import tomllib` broke tests on Python 3.10

Command: `.\.venv\Scripts\python.exe -m pytest -q` (at commit 589387f)

Output (last lines):

```
E   ModuleNotFoundError: No module named 'tomllib'
=========================== short test summary info ===========================
ERROR tests/test_config.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.26s
```

Exit code: 1. Fixed in commit 6f5a30c by a tomli fallback in
`src/logsift/config.py` and a conditional `tomli` dependency in
`pyproject.toml`.

## F5. Test command passes (at commit 6f5a30c)

Command: `.\.venv\Scripts\python.exe -m pytest -q`

Output (last lines):

```
..........                                                               [100%]
10 passed in 0.09s
```

Exit code: 0.

## F6. Lint command passes (at commit 6f5a30c)

Command: `.\.venv\Scripts\python.exe -m ruff check .`

Output: `All checks passed!`

Exit code: 0.

## F7. CLI entry point works; `logsift.main` is not the entry point

Command:

```
"2024-01-01T00:00:00 INFO started`n2024-01-01T00:00:01 ERROR disk full" | Out-File -Encoding ascii $env:TEMP\sample.log
.\.venv\Scripts\logsift.exe $env:TEMP\sample.log --counts
```

Output:

```
ERROR 1
INFO 1
exit=0
```

The console script is declared in `pyproject.toml` as `logsift = "logsift.cli:main"`.
`src/logsift/main.py` raises `SystemExit` if called (source: its module docstring
and body; confirmed by reading the file, and by F5 in which no test imports it).

## F8. Config merge order (source: passing tests in F5)

`tests/test_config.py` passes (part of F5), which asserts:
defaults, then `./logsift.toml` in the working directory, then the file named
by the `LOGSIFT_CONFIG` environment variable. Later sources override earlier ones.

## F9. Repository layout (source: `git ls-files subject/` at 6f5a30c)

```
subject/pyproject.toml
subject/src/logsift/__init__.py
subject/src/logsift/cli.py
subject/src/logsift/config.py
subject/src/logsift/filters.py
subject/src/logsift/main.py
subject/src/logsift/parser.py
subject/src/logsift/stats.py
subject/tests/test_config.py
subject/tests/test_filters.py
subject/tests/test_parser.py
subject/tests/test_stats.py
```
