# Case study: repairing look-ahead bias

[Back to the benchmark](../README.md)

**Task:** `L1_DBG_01_lookahead_bias_fix`

**Purpose:** inspect whether an agent can diagnose a temporal-alignment error,
produce a repair, and supply evidence that can be evaluated.

This page explains the checked-in task contract. It does not claim that a new model
run was executed or that a strategy earned real returns.

![Task inputs, required artifacts, and evaluation evidence.](assets/lookahead-task.svg)

## Required output

| Artifact | Intended evidence |
| --- | --- |
| `output/diagnosis.md` | An explanation of the look-ahead issue and its effect on the result. |
| `output/lookahead_fixed.py` | The corrected strategy implementation. |
| `output/comparison.json` | Original and corrected return and Sharpe values, under the task's required field names. |

The [task definition](../bench/tasks/L1/debug/L1_DBG_01_lookahead_bias_fix.json)
is authoritative for the exact fields and constraints. In this constructed fixture,
the corrected return must be lower than the inflated original return. That is a
fixture condition, not a universal financial rule.

## How to read the evidence

1. Inspect the diagnosis and code difference for the time-alignment change.
2. Check the command records and execution status; the existence of a file alone
   does not establish that the intended code ran.
3. Validate the JSON fields and the task's numerical constraints.
4. Read the result-quality and process-quality evaluations with their coverage.

The default full aggregation uses **0.60 × QR + 0.40 × QP**. If a required scoring
track fails, the aggregate is not computable; a missing judge score is not silently
turned into zero. These weights describe this implementation, not a universal
measure of agent competence.

## Code to inspect

- [Task definition](../bench/tasks/L1/debug/L1_DBG_01_lookahead_bias_fix.json).
- [Task-specific verification entry](../bench/tasks/test_scripts/L1/L1_DBG_01_lookahead_bias_fix.py).
- [Score aggregation](../bench/eval/core/scoring.py).
- [Missing-score regression tests](../bench/tests/unit/test_scoring_missing_semantics.py).
- [Evaluation limits](evaluation.md).

For a future recorded demonstration, publish the acting-model revision, task
revision, trace, artifacts, score coverage, latency, and cost together. Keep such
run evidence separate from this task-contract explanation.
