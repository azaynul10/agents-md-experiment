import argparse
import sys

from .config import load_config
from .filters import by_level, by_substring
from .parser import parse_lines
from .stats import level_counts


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="logsift")
    p.add_argument("path")
    p.add_argument("--level")
    p.add_argument("--contains")
    p.add_argument("--counts", action="store_true")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    cfg = load_config()
    with open(args.path, encoding="utf-8") as f:
        records = parse_lines(f.readlines()[: cfg["max_lines"]])
    if args.level:
        records = by_level(records, args.level)
    if args.contains:
        records = by_substring(records, args.contains)
    if args.counts:
        for k, v in sorted(level_counts(records).items()):
            print(f"{k} {v}")
        return 0
    for r in records:
        print(f"{r.ts} {r.level} {r.msg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
