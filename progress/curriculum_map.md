# Curriculum Map

Detailed learning objectives and scope for each module.

---

## Module 01 — Python Basics
**Goal:** Understand core Python syntax well enough to write simple scripts and notebooks.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_variables_and_types | int, float, str, bool, None, type(), f-strings | Storing and printing model scores, response text |
| 02_control_flow | if/elif/else, for loops, while, break/continue, range() | Iterating over batches of outputs, filtering results |
| 03_functions | def, parameters, return, docstrings, scope | Reusable scoring/flagging functions |
| 04_collections | list, dict, set, tuple, comprehensions | Storing batches of prompts, responses, metadata |
| 05_review | Mini-project: score text responses | End-to-end flow on a tiny eval dataset |

---

## Module 02 — Data Workflows
**Goal:** Read/write files, work with JSON and CSV, understand Python modules.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_imports_and_modules | import, from/import, os, sys, pathlib, random | Loading datasets, navigating directories |
| 02_files_and_io | open/read/write, with statement, pathlib.Path | Loading model output files, saving results |
| 03_json_and_csv | json.load/dump, csv.reader/DictReader, pandas read_csv | Reading real eval datasets, API output files |
| 04_review | Mini-project: load + summarize model outputs | Full pipeline: load → inspect → summarize |

---

## Module 03 — Debugging
**Goal:** Read error messages confidently, use basic debugging techniques.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_reading_errors | TypeError, NameError, IndexError, KeyError, tracebacks | Diagnosing broken analysis scripts |
| 02_debugging_strategies | print(), assert, pdb, defensive coding | Finding bugs in evaluation pipelines |
| 03_review | Buggy code exercises | Fix broken research analysis code |

---

## Module 04 — NumPy & Pandas
**Goal:** Work with arrays and dataframes for numerical and tabular data.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_numpy_arrays | ndarray, vectorized ops, boolean indexing, np.where, argmax/argmin | Processing score arrays, pass/fail masking, z-scores |
| 02_pandas_dataframes | pd.read_csv, DataFrame/Series, filtering with &, missing values, sort_values | Loading eval CSVs, filtering low-scoring models |
| 03_groupby_and_aggregation | groupby, .agg(), .idxmax(), computed columns, pivot_table | Per-model summaries, benchmark scorecards |
| 04_eval_data_mini_project | End-to-end: CSV + JSON → scorecard, flag analysis, response length, z-scores | Full eval data pipeline on synthetic model outputs |

---

## Module 05 — Plotting & Exploratory Analysis
**Goal:** Visualize data to find patterns and communicate findings.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_matplotlib_basics | Figure/Axes, bar charts, value labels, axhline, colors, savefig | Model performance bar charts, threshold lines |
| 02_distributions_and_scatter | ax.hist, sns.histplot(kde=True), sns.boxplot, sns.stripplot, scatter | Score distributions, flagged vs. clean response lengths |
| 03_heatmaps_and_subplots | sns.heatmap, difference heatmaps, plt.subplots multi-panel | Model×task scorecards, v1→v2 improvement grids |
| 04_eval_plots_mini_project | Full 5-figure eval report saved to output/plots/ | Publication-ready eval visualizations |

---

## Module 06 — Writing Reusable Scripts
**Goal:** Move beyond notebooks to write clean, importable Python scripts.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_script_structure | `if __name__ == "__main__"`, `%%writefile`, `main()`, importlib.reload | Turning notebook analysis into reusable scripts |
| 02_argparse_and_logging | ArgumentParser, type=Path/float, action="store_true", logging levels | Production eval scripts with CLI flags and structured logs |
| 03_eval_script_mini_project | End-to-end: run_evaluation.py + v2 with --model filter, subprocess testing | Full CLI eval tool: --input, --output, --threshold, --model |

---

## Module 07 — Environments, Dependencies, Reproducibility
**Goal:** Understand how Python environments work; make work reproducible.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_virtual_environments | venv isolation, uv venv, python -m venv, activate/deactivate, sys.executable, importlib.metadata | Understanding why experiment environments must be isolated |
| 02_package_management | uv pip install, pip install, version specifiers (==, >=, ~=), requirements.txt, uv pip freeze, pyproject.toml overview | Pinning exact dependencies so results can be reproduced |
| 03_seeds_and_reproducibility | random.seed(), np.random.seed(), default_rng(), SEED constant, limits of seeding (GPU, APIs) | Making stochastic code deterministic: train/test splits, sampling, weight initialization |
| 04_mini_project | analyze_scores.py with seeds, requirements.txt, REPRODUCE.md, two-run identity check | Full reproducible experiment scaffold matching real AI research practices |

---

## Module 08 — Basic Statistics for Experiments
**Goal:** Apply basic statistics to interpret evaluation results.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_descriptive_stats | mean, median, mode (`statistics` stdlib); mean vs. median (outlier sensitivity); detecting skew by comparing mean and median | Summarizing model eval scores; spotting left-skewed distributions where rare catastrophic failures drag down the mean |
| 02_distributions_and_spread | variance, standard deviation, range, IQR; manual variance from list comprehension; reliability labeling by std dev threshold | Two models can share the same mean but differ in reliability; high spread in safety-critical scores is a deployment risk |
| 03_comparing_groups | null hypothesis and p-value intuition; Welch's t-statistic (manual); Cohen's d effect size; bootstrap confidence intervals (manual loop, `random.choice`) | Determining whether a score difference between prompt variants or model versions is real vs. noise; reporting effect size in research memos |
| 04_mini_project | Load CSV with `csv.DictReader`; `stats_summary()` returning mean/median/std/reliable dict; full model scorecard; Cohen's d comparison of v1 vs v2 on synthetic eval data | End-to-end stats pipeline: load evaluation_results.csv, summarize all models, compare versions, flag unreliable models |

---

## Module 09 — Evaluation Methodology
**Goal:** Design and run small, rigorous evaluations.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_eval_design | Eval task types (classification, ranking, open-ended scoring), rubric design, data contamination (train/test leakage, prompted-answer contamination), eval design checklist | Designing trustworthy evals for honesty, safety, and helpfulness; avoiding misleading benchmark scores |
| 02_metrics_and_baselines | Accuracy, precision, recall, F1 (from-scratch computation); random and majority-class baselines; macro vs micro averaging (conceptual) | Measuring safety classifier performance; establishing that a model beats chance before claiming it works |
| 03_inter_rater_agreement | Why annotator disagreement threatens eval validity; percent agreement; Cohen's kappa formula and intuition; kappa interpretation thresholds (κ > 0.6 rule) | Auditing annotation rubrics before scaling human evaluation; reporting agreement in eval methodology sections |
| 04_mini_project | End-to-end eval pipeline: load model_outputs.json, apply heuristic rubric, compute precision/recall/F1 vs ground truth, compute majority-class baseline, write findings dict (stdlib only) | Full small-scale safety eval: from raw model outputs to a structured findings report |

---

## Module 10 — Analysis of Model Outputs
**Goal:** Load, inspect, and analyze batches of model responses.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_loading_and_inspecting | json.load, list comprehensions, flag_rate, unique model list | First-pass inspection of a batch of model outputs |
| 02_per_model_analysis | pd.DataFrame, groupby, .size(), .mean(), .round(), per-model stats | Comparing flag rates and response lengths across model versions |
| 03_heuristics_and_patterns | str.contains, short-response filter, sort_values, boolean indexing | Building fast imperfect rules to surface suspicious outputs |
| 04_mini_project | End-to-end: overall_stats, model_scorecard, pattern finding, findings dict | Full analysis pipeline from raw JSON to structured research findings |

---

## Module 11 — Prompt/Output Datasets
**Goal:** Create and manage small datasets of prompts and model outputs.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_dataset_structure | Annotation schemas, JSONL format, json.dumps/loads, write/read JSONL | Defining and building structured eval dataset entries |
| 02_sampling_strategies | random.sample, stratified sampling by category, adversarial examples | Building representative, diverse eval sets that probe model weaknesses |
| 03_versioning_and_formats | JSON↔JSONL↔CSV conversion, csv.DictWriter/DictReader, dataset cards | Packaging and documenting datasets for reproducible research |
| 04_mini_project | Full dataset: schema → 9+ entries → JSONL → dataset card | End-to-end eval dataset creation matching real AI safety lab practices |

---

## Module 12 — Safety-Oriented Classification & Evaluation
**Goal:** Apply classification logic to safety-relevant model outputs.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_rule_based_classifiers | Keyword trigger lists, flag_response(), confusion matrix (TP/FP/FN/TN) | Building auditable first-line safety filters for model outputs |
| 02_precision_recall_tradeoff | Precision, recall, F1 formulas; asymmetric costs of FP vs FN in safety | Reasoning about over- vs under-flagging tradeoffs in deployment |
| 03_evaluating_classifiers | classifier v1 vs v2 comparison, accuracy caveat, which is better for safety | Systematic classifier evaluation to choose the right safety threshold |
| 04_mini_project | compute_metrics() helper, both classifiers, comparison dict, findings summary | Full safety classifier pipeline: build → evaluate → compare → report |

---

## Module 13 — Error Analysis
**Goal:** Systematically analyze where models fail.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_confusion_matrix | TP/FP/FN/TN definitions, confusion dict, accuracy vs majority-class baseline | Understanding why 90% accuracy on an imbalanced safety dataset can still miss most harmful outputs |
| 02_fp_fn_analysis | Extract FN/FP examples, qualitative review, `zip(outputs, preds, labels)` pattern | Reading actual failure cases to identify systematic causes, not just error counts |
| 03_slice_analysis | Per-model FN rates, `max(..., key=...)`, identifying worst-performing slice | Discovering that all errors concentrate in model-b-v1 — a targeted fix target |
| 04_mini_project | Full pipeline: confusion matrix → FN examples → per-model slice → improvements dict | End-to-end error analysis from raw classifier to actionable improvement proposals |

---

## Module 14 — Research-Style Coding Habits
**Goal:** Write code the way a research engineer would.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_notebooks_vs_scripts | Notebook vs script decision criteria, `load_and_count()`, `%%writefile` extraction | Knowing when exploration code should become a reusable pipeline script |
| 02_docstrings_and_naming | snake_case, magic numbers → named constants, type hints, docstrings, `__doc__` | Making research functions readable enough for colleagues to reproduce and trust |
| 03_reproducibility_checklist | 5-item checklist, `%%writefile analysis_readme.md`, reproducibility_report dict | Ensuring an analysis can be re-run exactly by anyone, anytime |
| 04_mini_project | Refactor MESSY_CODE → clean_analysis.py with SEED, docstrings, constants, entry guard | Full code cleanup: messy notebook snippet → production-quality research script |

---

## Module 15 — Research Memos from Findings
**Goal:** Write short, clear memos summarizing experimental findings.

| Notebook | Topics | AI Research Connection |
|----------|--------|------------------------|
| 01_memo_structure | 5-section memo (question/method/results/caveats/next_steps), the "lede", memo outline dict | Structuring safety evaluation findings so colleagues can act on them quickly |
| 02_numbers_in_context | Baseline comparison, version comparison, formatted_result string, results_summary dict | Presenting F1=0.86 as meaningful: "up from 0.83 v1, vs. 0.0 for majority-class baseline" |
| 03_caveats_and_next_steps | Caveat types, specific vs vague next steps, prioritized next_steps list of dicts | Writing honest limitations without underselling findings; turning results into actions |
| 04_mini_project | Full memo dict (5 sections), technical vs nontechnical audience versions | Complete 1-page research memo from Module 12 classifier results — the final curriculum artifact |
