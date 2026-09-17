# Human alignment

[Back to the experiment](../README.md)

Human ratings provide an independent comparison for the simulator judges. Review the same evidence and rubric used for the corresponding dimension; do not infer a rating from the model name or an aggregate score.

## Review sequence

1. Select items with coverage across tasks, personas, student models, and evaluation dimensions.
2. Preserve the sample identifier, rubric identifier/version, and dimension throughout export, review, and aggregation.
3. Read the persona contract and the relevant transcript or probe response.
4. Assign a rating using the anchored rubric. Record a short reason tied to the evidence.
5. Keep missing labels separate from low scores. Inspect disagreements before summarizing them.
6. Report matched sample counts, agreement criteria, and per-dimension results.

The shared review schema is [human_review.schema.json](../../human_review/human_review.schema.json). Experiment contracts and rubric definitions are under [resources](../resources).

## Commands

From the repository root:

```bash
PYTHONPATH=bench python -m experiments.user_sim_stability.cli human-alignment --help
PYTHONPATH=bench python -m experiments.user_sim_stability.cli human-alignment-extend --help
PYTHONPATH=bench python -m experiments.user_sim_stability.cli judge-agreement --help
```

These analysis commands require the corresponding generated results and review data. The repository does not include personal reviewer records or the full historical conversation corpus.

## Checks before interpreting a number

- Verify that sample IDs join correctly between experiment output, review plans, and labels.
- Use the actual number of matched items as the denominator.
- Count multiple judges rating one conversation as repeated views of the same item, not new independent conversations.
- Inspect sample size and disagreements for each dimension.
- Keep persona fidelity, drift, and other dimensions separate. Agreement on one dimension does not establish the validity of all dimensions.

The original control-condition mapping used `S6`; an earlier `control` alias caused missing matches. The retained pipeline uses explicit dimension mapping to keep those results aligned.
