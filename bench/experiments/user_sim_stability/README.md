# Simulated-student reliability

[Back to the project](../../../README.md)

An LLM-driven student is part of the evaluation environment. If it ignores its assigned knowledge level or changes personality unpredictably, it can change the tutor's score for reasons unrelated to the tutor's ability.

This experiment tests persona behavior separately from the main agent benchmark.

## Design

| Axis | Configuration |
| --- | --- |
| Task fixtures | 6 fixed quantitative-finance scenarios |
| Personas | 2 assigned personas per task, drawn from a finance × coding matrix |
| Student models | 3 configured candidates |
| Repetitions | 3 |
| Tutor temperatures | 0.0 and 1.0 |
| Student temperature | Fixed at 0.0 |
| Main conversations | 216 |
| Generic-student controls | 36 |
| Total design | **252 conversations** |

The temperature perturbation belongs to the tutor. These are the dimensions of the experiment, not a claim that the full 142-task library was evaluated with every model.

The six task fixtures live in [resources/tasks](resources/tasks). They preserve the original experiment inputs independently of the active L0/L1/L2 catalog.

## Pipeline

```text
Persona contracts + task fixtures
              ↓
    Conversation generation
              ↓
    Rendered judge inputs
              ↓
       Judge responses
              ↓
 Aggregate + compare + inspect
              ↓
  Human alignment and reports
```

| Dimension | Question |
| --- | --- |
| S1 — persona adherence | Does the student behave within its assigned profile? |
| S2 — persona drift | Does that behavior change over the conversation? |
| S3 — repeatability | How stable is behavior across repeated runs? |
| S4 — blind identification | Can a judge identify the intended persona? |
| S5 — targeted probes | Does the student respect specific knowledge/behavior boundaries? |
| S6 — generic control | Is persona conditioning meaningfully different from a generic student? |

## Inspect without model calls

From the repository root:

```bash
PYTHONPATH=bench python -m experiments.user_sim_stability.cli dry-run
PYTHONPATH=bench python -m experiments.user_sim_stability.cli --help
```

Configuration is in [core/config.py](core/config.py), with model defaults in [server/config/llm_config.py](../../server/config/llm_config.py).

## Run a small live slice

Set your own `OPENROUTER_API_KEY` first. This command makes live model calls:

```bash
PYTHONPATH=bench python -m experiments.user_sim_stability.cli generate \
  --limit 1 --workers 1
```

Use `render-judges`, `judge`, `aggregate-multi-judge`, `validate`, and `report` for subsequent stages. The `all` command runs the broader pipeline and requires the judge-qualification gate. Inspect each command's `--help` before selecting a full run.

Generated conversations, judge outputs, review labels, and reports are kept in ignored result directories. They are not shipped as a ready-to-rerender full historical experiment.

## Interpretation

Repeated scoring, agreement between judges, and agreement with human reviewers answer different questions. Agreement alone does not establish validity, and the simulated-student study does not measure real learners' educational outcomes.

The pipeline retains per-dimension evidence and coverage so a missing result can be distinguished from a low score. For human review, see [the alignment guide](docs/HUMAN_ALIGNMENT.md).
