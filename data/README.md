# data/

This directory holds datasets used in exercises throughout the curriculum.

## data/synthetic/

Synthetic (artificially generated) datasets that simulate real AI research data.
These are safe to use, modify, and re-generate.

### model_outputs.json

Simulates a small batch of model responses with metadata:
- `id`: unique identifier
- `prompt`: the input given to the model
- `response`: the model's output
- `flagged`: whether a human reviewer flagged the response (bool)
- `category`: the type of potential issue (or `null` if not flagged)
- `model`: which model produced the response

Used in: Module 02 (JSON/CSV), Module 10 (model output analysis), Module 12 (safety eval)

### evaluation_results.csv

Simulates evaluation results across tasks and models:
- `model`: model name
- `task`: evaluation task name
- `score`: numeric score (0.0–1.0)
- `n_samples`: how many samples the score is based on
- `notes`: optional notes from the evaluator

Used in: Module 02 (CSV), Module 08 (statistics), Module 09 (evaluation methodology)
