from . import replace

EDIT_FILES = ["src/logsift/cli.py"]
READ_FILES = ["src/logsift/cli.py", "src/logsift/__init__.py", "pyproject.toml"]
KEYWORDS = "--version __version__ entry point"


def apply(subject):
    cli = subject / "src/logsift/cli.py"
    replace(
        cli,
        "from .config import load_config",
        "from . import __version__\nfrom .config import load_config",
    )
    replace(
        cli,
        '    p.add_argument("--counts", action="store_true")',
        '    p.add_argument("--counts", action="store_true")\n'
        '    p.add_argument("--version", action="version", version=__version__)',
    )
