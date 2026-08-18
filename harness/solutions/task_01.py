from . import replace

EDIT_FILES = ["src/logsift/filters.py", "src/logsift/cli.py"]
READ_FILES = ["src/logsift/filters.py", "src/logsift/cli.py"]
KEYWORDS = "by_regex --regex re.search"


def apply(subject):
    filters = subject / "src/logsift/filters.py"
    cli = subject / "src/logsift/cli.py"

    replace(filters, "from .parser import Record", "import re\n\nfrom .parser import Record")
    replace(
        filters,
        "def by_substring(records: list[Record], needle: str) -> list[Record]:\n"
        "    return [r for r in records if needle in r.msg]",
        "def by_substring(records: list[Record], needle: str) -> list[Record]:\n"
        "    return [r for r in records if needle in r.msg]\n"
        "\n"
        "\n"
        "def by_regex(records: list[Record], pattern: str) -> list[Record]:\n"
        "    rx = re.compile(pattern)\n"
        "    return [r for r in records if rx.search(r.msg)]",
    )
    replace(
        cli,
        "from .filters import by_level, by_substring",
        "from .filters import by_level, by_regex, by_substring",
    )
    replace(
        cli,
        '    p.add_argument("--counts", action="store_true")',
        '    p.add_argument("--regex")\n    p.add_argument("--counts", action="store_true")',
    )
    replace(
        cli,
        "    if args.contains:\n        records = by_substring(records, args.contains)",
        "    if args.contains:\n        records = by_substring(records, args.contains)\n"
        "    if args.regex:\n        records = by_regex(records, args.regex)",
    )
