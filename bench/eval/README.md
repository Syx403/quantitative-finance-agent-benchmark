# Evaluation package

[Project overview](../../README.md) · [Scoring guide](../../docs/evaluation.md)

This package evaluates saved agent evidence independently of the server runtime.

| Directory | Purpose |
| --- | --- |
| `contracts/` | Bundle, request, output, and schema definitions |
| `core/` | Coordination, preflight, aggregation, and missing-score handling |
| `tracks/` | QR and QP orchestration |
| `judges/` | Rubric-driven LLM evaluation |
| `programmatic/` | Artifact, code, and tool checks |
| `inputs/` | Dimension-specific evidence preparation |
| `rubrics/` | Versioned scoring rubrics |
| `storage/` | File-backed, versioned evaluation records |
| `backfill/` | Compatibility conversion for saved result bundles |

`score.py` exposes the standalone scoring entry point. The coordinator provides the persisting path used by the server. Some indexes and state files are updated in place; storage is not an entirely immutable event log.

Run the relevant offline checks from the repository root:

```bash
python -m pytest bench/tests/unit/test_scoring_missing_semantics.py \
  bench/tests/unit/test_eval_score_standalone.py -q
```
