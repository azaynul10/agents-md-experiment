from . import replace

EDIT_FILES = ["src/logsift/filters.py"]
READ_FILES = ["src/logsift/filters.py", "src/logsift/cli.py"]
KEYWORDS = "by_level comma-separated"


def apply(subject):
    filters = subject / "src/logsift/filters.py"
    replace(
        filters,
        "def by_level(records: list[Record], level: str) -> list[Record]:\n"
        "    lv = level.upper()\n"
        "    return [r for r in records if r.level == lv]",
        "def by_level(records: list[Record], level: str) -> list[Record]:\n"
        '    wanted = {part.strip().upper() for part in level.split(",") if part.strip()}\n'
        "    return [r for r in records if r.level in wanted]",
    )
