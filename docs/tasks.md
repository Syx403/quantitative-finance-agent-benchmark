# Task library

[Back to the project](../README.md)

The active library contains **142 task definitions**, organized by what must be demonstrated.

| Layer | Count | What it tests |
| --- | ---: | --- |
| [L0](../bench/tasks/L0) | 100 | Financial knowledge, numerical interpretation, and multi-step reasoning. |
| [L1](../bench/tasks/L1) | 23 | Tool-assisted data engineering, debugging, implementation, alpha research, and backtest-engine work. |
| [L2](../bench/tasks/L2) | 19 | Multi-turn diagnosis, end-to-end problem solving, and adversarial user scenarios. |

L0 incorporates selected material from existing financial QA sources. Source information remains in the task definitions. The library count is a scope measure, not a claim of 142 original research questions or a complete multi-model evaluation.

## Three examples

| Task | Expected behavior |
| --- | --- |
| [Look-ahead bias fix](../bench/tasks/L1/debug/L1_DBG_01_lookahead_bias_fix.json) | Identify the temporal-alignment bug, write corrected code, and produce comparison artifacts. |
| [Production debugging](../bench/tasks/L2/end_to_end/L2_E2E_02_production_debugging.json) | Work through a strategy failure with a user, inspect evidence, and explain the correction. |
| [Prompt injection in a CSV](../bench/tasks/L2/adversarial/L2_ADV_11_prompt_injection_csv.json) | Handle malicious instructions embedded in material that should be treated as data. |

## Task contract

A task specifies its identity, category, prompt, environment, and acceptance criteria. Code tasks can declare tools, data and documentation, sandbox image, network access, expected output files, and verification rules.

Structured expected outputs make parts of the contract executable. JSON checks can require keys and comparisons; CSV checks can require columns and row counts. More semantic judgments use task-specific checks and/or LLM judges.

The schema is [`QuantTutorTask`](../bench/eval/contracts/schemas.py). The reference adapter is [`ReferenceTaskSuite`](../bench/server/reference/task_suite.py).

```bash
python scripts/check_catalog.py
```

This checks every active task against the schema, verifies unique identifiers and declared verification-script paths, and prints the layer counts. It also validates the six fixed task fixtures used by the separate simulator study.

## Library vs. runnable catalog

The default Run catalog exposes L2 tasks. The reference task-suite adapter can load all three layers; L0 and L1 use their corresponding evaluation paths. Inspecting a task definition does not imply that every task can be launched through the same public client endpoint.

The small `impl_b` suite is a deterministic plugin test fixture for the platform contracts. It is excluded from the 142-task total. The simulator study's six pinned task fixtures are also separate from that total.

## Data

Large datasets and generated results are excluded. Live tasks may need external market data and documentation from the pinned dataset configuration. Third-party datasets retain their own terms; see [NOTICE](../NOTICE.md). Exchange symbols inside data files are preserved verbatim, including non-Latin symbols where required by the source data.
