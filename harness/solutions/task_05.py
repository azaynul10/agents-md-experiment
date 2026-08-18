from . import replace

EDIT_FILES = ["src/logsift/cli.py"]
READ_FILES = ["src/logsift/cli.py", "src/logsift/config.py"]
KEYWORDS = "min_level rank DEBUG INFO WARNING ERROR"


def apply(subject):
    cli = subject / "src/logsift/cli.py"
    replace(
        cli,
        "from .stats import level_counts",
        "from .stats import level_counts\n"
        "\n"
        '_RANK = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3}\n'
        "\n"
        "\n"
        "def apply_min_level(records, min_level):\n"
        "    floor = _RANK.get(str(min_level).upper())\n"
        "    if floor is None:\n"
        "        return records\n"
        "    return [r for r in records if _RANK.get(r.level, floor) >= floor]",
    )
    replace(
        cli,
        "    if args.level:\n        records = by_level(records, args.level)",
        "    if args.level:\n        records = by_level(records, args.level)\n"
        "    else:\n"
        '        records = apply_min_level(records, cfg["min_level"])',
    )
