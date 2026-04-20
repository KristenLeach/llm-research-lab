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

Topics: mean, median, variance, standard deviation, confidence intervals, p-values (intro), effect size
AI Research Connection: Comparing model scores, determining if differences are meaningful

---

## Module 09 — Evaluation Methodology
**Goal:** Design and run small, rigorous evaluations.

Topics: task design, metrics, baselines, avoiding contamination, inter-rater agreement
AI Research Connection: Designing evals for honesty, safety, helpfulness

---

## Module 10 — Analysis of Model Outputs
**Goal:** Load, inspect, and analyze batches of model responses.

Topics: loading output files, computing statistics, identifying patterns, flagging heuristics
AI Research Connection: Analyzing real LLM output datasets

---

## Module 11 — Prompt/Output Datasets
**Goal:** Create and manage small datasets of prompts and model outputs.

Topics: dataset structure, annotation schemas, versioning, sampling strategies
AI Research Connection: Building eval datasets, annotation workflows

---

## Module 12 — Safety-Oriented Classification & Evaluation
**Goal:** Apply classification logic to safety-relevant model outputs.

Topics: rule-based classifiers, keyword matching, threshold tuning, precision/recall
AI Research Connection: Detecting harmful content, jailbreaks, misinformation

---

## Module 13 — Error Analysis
**Goal:** Systematically analyze where models fail.

Topics: confusion matrices, false positives/negatives, slice analysis, root cause reasoning
AI Research Connection: Understanding model failure modes, improving evals

---

## Module 14 — Research-Style Coding Habits
**Goal:** Write code the way a research engineer would.

Topics: notebooks vs. scripts, version control basics, naming conventions, documentation, reproducibility checklists
AI Research Connection: Making research code shareable and trustworthy

---

## Module 15 — Research Memos from Findings
**Goal:** Write short, clear memos summarizing experimental findings.

Topics: memo structure, presenting quantitative results, caveats, next steps
AI Research Connection: Communicating research findings to teammates, writing paper sections
