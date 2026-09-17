# Evaluation

[Back to the project](../README.md)

The evaluator combines checks that can be made in code with judgments that require interpretation. It consumes a saved bundle rather than controlling the agent's execution loop.

## Result and process

| Track | Question | Evidence |
| --- | --- | --- |
| **QR — result quality** | Did the agent produce the required outcome? | Task requirements, references, output files, numerical checks, code checks, and semantic judgment. |
| **QP — process quality** | How did the agent work toward that outcome? | Tool choices, execution status, action economy, code changes, planning, and problem solving. |

The retained full-evaluation configuration uses `0.60 × QR + 0.40 × QP`. Applicable checks and their internal combination vary with the task. These weights are a versioned design choice, not an independently established universal measure of agent quality.

The standalone entry point is [`eval.score.score`](../bench/eval/score.py). The server uses the coordinator and storage layer when persisted score files are required.

## A concrete example: look-ahead bias

[`L1_DBG_01_lookahead_bias_fix`](../bench/tasks/L1/debug/L1_DBG_01_lookahead_bias_fix.json) asks the agent to inspect a strategy, fix its temporal alignment, and produce:

- `output/diagnosis.md` — an explanation of the issue.
- `output/lookahead_fixed.py` — corrected code.
- `output/comparison.json` — original and corrected returns and Sharpe values.

The JSON check validates required fields and numerical relationships. In this constructed fixture, the corrected return should be below the inflated original return.

The generic verifier checks Python/Markdown outputs mainly for existence and non-empty content. Passing those structural checks does not independently prove that the intended code ran or that every financial conclusion is correct. Execution records and task-specific checks provide additional evidence.

## Failure semantics

| Situation | Interpretation |
| --- | --- |
| A command returns a non-zero exit status | Tool execution failed, even if its Python wrapper returned normally. |
| A warning appears on stderr | Inspect the exit status and result; a warning alone is not a failure. |
| A required judge fails | Preserve valid partial scores and mark the requested overall score as not computable. |
| A dimension is not applicable | Handle it according to the requested evaluation mode and task contract. |
| A Session reaches its time/turn limit | Inspect the termination reason; termination alone does not establish task success. |

The [proxy regression tests](../bench/tests/test_proxy_success_detection.py) and [missing-score tests](../bench/tests/unit/test_scoring_missing_semantics.py) cover these distinctions. Aggregates must report missing-score coverage so excluded runs do not silently change the meaning of an average.

## Judge inputs and reliability

Judges receive context relevant to their dimension, with versioned rubrics and prompts. A result judge and a problem-solving judge need different evidence. Structured JSON makes output parseable, but does not guarantee that the judgment is correct.

Reliability has several parts: stability across repetitions, agreement between judges, and alignment with human judgments. Agreement can coexist with shared bias. The [simulator study](../bench/experiments/user_sim_stability/README.md) explores those questions for the simulated student.

The retained task-pass threshold is `0.5`. A compact calibration fixture preserves the original numeric judge scores, human ratings, and matching keys used by its regression test. Generated transcript text, reviewer identities, and unrelated historical reports are omitted. That calibration has a limited sample and does not establish benchmark-wide validity.

## Records and rescoring

The server saves evidence and separate `score_n` evaluations with score/cost metadata. File locking protects allocation; indexes and state files can be updated. Records are therefore versioned, but the entire storage system is not append-only.

If a judge changes, saved evidence can be rescored. If the acting model or its prompt changes, run the agent again: its actions and artifacts may change. Report quality, completion, latency, cost, and score coverage together when comparing versions.

Process heuristics can favor expected tool paths, so valid alternative solutions require care. Tool outputs and displayed traces also have size limits. These are engineering constraints of the current implementation, rather than claims of complete observability or a fully validated leaderboard.
