"""Recompute every number quoted anywhere in this repository from results.csv.

Run:  python results/recompute.py

This is the single source of truth. If a number in summary.md, README.md,
RELATED-WORK.md, PITCH.md or harness/LIMITATIONS.md disagrees with this
output, the prose is wrong and the prose gets changed -- never the CSV.

Exits nonzero if the dataset does not have the expected shape.
"""

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

CSV_PATH = Path(__file__).with_name("results.csv")
CONDITIONS = ("without", "with-agents-md")
TASKS = ("task-01", "task-02", "task-03", "task-04", "task-05")
RUNS = (1, 2, 3)

INT_FIELDS = (
    "run_n", "pass", "tests_pass", "wrong_file_edits",
    "wrong_command_attempts", "clarifying_questions", "turns_to_completion",
)


def load():
    with open(CSV_PATH, newline="") as f:
        rows = [r for r in csv.DictReader(f) if r.get("task_id")]
    for r in rows:
        for k in INT_FIELDS:
            r[k] = int(r[k])
    return rows


def check(rows):
    errs = []

    if len(rows) != 30:
        errs.append(f"expected 30 data rows, found {len(rows)}")

    per_cond = Counter(r["condition"] for r in rows)
    for cond in CONDITIONS:
        if per_cond[cond] != 15:
            errs.append(f"expected 15 rows for {cond}, found {per_cond[cond]}")
    unknown = set(per_cond) - set(CONDITIONS)
    if unknown:
        errs.append(f"unknown conditions: {sorted(unknown)}")

    keys = Counter((r["task_id"], r["condition"], r["run_n"]) for r in rows)
    dupes = sorted(k for k, n in keys.items() if n > 1)
    if dupes:
        errs.append(f"duplicate (task, condition, run) keys: {dupes}")

    for cond in CONDITIONS:
        for task in TASKS:
            for run in RUNS:
                if keys[(task, cond, run)] != 1:
                    errs.append(f"missing or repeated cell: {task} {cond} run-{run}")

    if errs:
        for e in errs:
            print(f"ASSERT FAILED: {e}")
        sys.exit(1)
    print("dataset shape OK: 30 rows, 15 per condition, no duplicate cells")


def by(rows, cond, task, field):
    return [
        r[field]
        for run in RUNS
        for r in rows
        if r["condition"] == cond and r["task_id"] == task and r["run_n"] == run
    ]


def mean(xs):
    return sum(xs) / len(xs)


def table(rows, field, dp):
    print(f"\n{field} -- per task, run-1/run-2/run-3, with per-task mean")
    header = f"{'task':<9}"
    for cond in CONDITIONS:
        header += f"{cond:<18}{'mean':<8}"
    print(header)
    for task in TASKS:
        line = f"{task:<9}"
        for cond in CONDITIONS:
            vals = by(rows, cond, task, field)
            line += f"{', '.join(str(v) for v in vals):<18}{mean(vals):<8.{dp}f}"
        print(line)

    print(f"\n{field} -- condition level")
    means = {}
    for cond in CONDITIONS:
        vals = [r[field] for r in rows if r["condition"] == cond]
        means[cond] = mean(vals)
        print(
            f"  {cond:<15} total={sum(vals):<5} mean={means[cond]:.{dp}f} "
            f"min={min(vals)} max={max(vals)}"
        )
    gap = means[CONDITIONS[0]] - means[CONDITIONS[1]]
    print(f"  mean gap (without - with) = {gap:.{dp}f}")

    print(f"\n{field} -- within-condition spread (max - min across the 3 runs of a task)")
    for cond in CONDITIONS:
        spreads = {task: max(v := by(rows, cond, task, field)) - min(v) for task in TASKS}
        print(f"  {cond:<15} per task: {spreads}  max={max(spreads.values())}")
    return means, gap


def main():
    rows = load()
    check(rows)

    print(f"\ntasks={len(TASKS)} conditions={len(CONDITIONS)} runs per cell={len(RUNS)} "
          f"total runs={len(rows)}")

    print("\npass / tests_pass -- count of 1s out of 15 per condition")
    for field in ("pass", "tests_pass"):
        parts = []
        for cond in CONDITIONS:
            vals = [r[field] for r in rows if r["condition"] == cond]
            parts.append(f"{cond}={sum(vals)}/{len(vals)}")
        print(f"  {field:<12} {'  '.join(parts)}")

    turn_means, turn_gap = table(rows, "turns_to_completion", 1)
    cmd_means, _ = table(rows, "wrong_command_attempts", 2)

    print("\nall-zero metrics (across all 30 runs)")
    for field in ("wrong_file_edits", "clarifying_questions"):
        tot = sum(r[field] for r in rows)
        nz = [
            f"{r['task_id']}/{r['condition']}/run-{r['run_n']}"
            for r in rows if r[field] != 0
        ]
        print(f"  {field:<22} total={tot}  nonzero runs={nz or 'none'}")

    print("\nwrong_command_attempts -- nonzero cells in with-agents-md")
    for r in rows:
        if r["condition"] == "with-agents-md" and r["wrong_command_attempts"]:
            print(f"  {r['task_id']} run-{r['run_n']}: {r['wrong_command_attempts']}")

    spread_without = max(
        max(v := by(rows, "without", t, "turns_to_completion")) - min(v) for t in TASKS
    )
    print("\nheadline sentences, recomputed")
    print(f"  pass rate: {sum(r['pass'] for r in rows if r['condition'] == 'without')}/15 "
          f"without vs "
          f"{sum(r['pass'] for r in rows if r['condition'] == 'with-agents-md')}/15 with")
    print(f"  turns: {turn_means['without']:.1f} without vs "
          f"{turn_means['with-agents-md']:.1f} with, gap {turn_gap:.1f}")
    print(f"  max within-condition turn spread (without) = {spread_without}, "
          f"which is {'>=' if spread_without >= turn_gap else '<'} the gap {turn_gap:.1f}")
    print(f"  wrong_command_attempts (CONFOUNDED): "
          f"{cmd_means['without']:.2f} vs {cmd_means['with-agents-md']:.2f} per run")

    counts = defaultdict(int)
    for r in rows:
        counts[r["task_id"]] += 1
    print(f"\nrows per task: {dict(counts)}")


if __name__ == "__main__":
    main()
