"""Validate the active task library and fixed simulator fixtures offline."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "bench"
sys.path.insert(0, str(BENCH))

from eval.contracts.schemas import QuantTutorTask


def main() -> int:
    counts: Counter[str] = Counter()
    identifiers: set[str] = set()
    errors: list[str] = []
    for layer in ("L0", "L1", "L2"):
        for path in sorted((BENCH / "tasks" / layer).rglob("*.json")):
            try:
                raw = json.loads(path.read_text(encoding="utf-8"))
                task = QuantTutorTask.model_validate(raw)
                if task.task_id != path.stem:
                    raise ValueError("task_id must match the filename")
                if task.task_id in identifiers:
                    raise ValueError("duplicate task_id")
                identifiers.add(task.task_id)
                script = (raw.get("ground_truth") or {}).get("verification_script")
                if script and not (BENCH / script).is_file():
                    raise ValueError(f"missing verification script: {script}")
                counts[layer] += 1
            except (ValueError, TypeError) as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")

    fixtures = BENCH / "experiments/user_sim_stability/resources/tasks"
    fixture_count = 0
    for path in sorted(fixtures.rglob("*.json")):
        try:
            QuantTutorTask.model_validate_json(path.read_text(encoding="utf-8"))
            fixture_count += 1
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    for layer in ("L0", "L1", "L2"):
        print(f"{layer}: {counts[layer]} tasks")
    print(f"Total: {sum(counts.values())} active tasks")
    print(f"Simulator study: {fixture_count} separate fixed task fixtures")
    print("Task schemas, identifiers, and verification paths are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
