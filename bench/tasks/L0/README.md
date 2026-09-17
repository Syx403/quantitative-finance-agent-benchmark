# L0: knowledge and reasoning

[Task library guide](../../../docs/tasks.md)

This layer contains 100 selected financial knowledge and reasoning tasks:

- Conceptual questions.
- Numerical and data interpretation.
- Multi-step reasoning.

The task JSON files retain their source metadata and references. Material was selected and normalized from existing financial QA datasets and reference sources; it is not a set of 100 newly authored questions.

The earlier ingestion and synthesis pipeline is outside this repository's runtime scope. Use the included definitions with the current task schema and reference evaluator.

From the repository root, validate the active library with:

```bash
python scripts/check_catalog.py
```
