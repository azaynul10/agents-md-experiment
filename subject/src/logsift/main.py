"""Legacy module kept for import compatibility. Not the CLI entry point.

The console script is defined in pyproject.toml as logsift.cli:main.
"""


def main() -> int:
    raise SystemExit("logsift.main is not the entry point; use logsift.cli:main")
