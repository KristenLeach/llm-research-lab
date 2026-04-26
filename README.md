# LLM Research Lab

A hands-on, notebook-based Python curriculum designed for someone learning Python
specifically for **AI research engineering** — evaluations, model behavior analysis,
safety research, and empirical AI safety work. This repo is a work in progress and will be updated as more content is added.

---

## Who This Is For

- You're a software engineer comfortable with JavaScript/Node, new to Python
- You want to learn Python for AI research engineering roles
- You're aiming toward work like: evaluations, model behavior analysis, honesty
  research, harmful output detection, dataset creation, and research-style coding

Every module connects Python skills back to concrete research engineering tasks.

---

## Curriculum Overview

| Module | Topic | Status |
|--------|-------|--------|
| 01 | Python Basics: Variables, Types, Control Flow, Functions, Collections | ✅ Full |
| 02 | Data Workflows: Imports, Files, JSON, CSV | ✅ Full |
| 03 | Debugging: Reading Errors, Stack Traces, Strategies | ✅ Full |
| 04 | NumPy & Pandas Basics | ✅ Full |
| 05 | Plotting & Exploratory Analysis | ✅ Full |
| 06 | Writing Reusable Scripts | ✅ Full |
| 07 | Environments, Dependencies, Reproducibility | ✅ Full |
| 08 | Basic Statistics for Experiments | ✅ Full |
| 09 | Evaluation Methodology | ✅ Full |
| 10 | Analysis of Model Outputs | ✅ Full |
| 11 | Prompt/Output Datasets | ✅ Full |
| 12 | Safety-Oriented Classification & Evaluation | ✅ Full |
| 13 | Error Analysis | ✅ Full |
| 14 | Research-Style Coding Habits | ✅ Full |
| 15 | Research Memos from Findings | ✅ Full |

See [progress/curriculum_map.md](progress/curriculum_map.md) for detailed learning objectives.

---

## Setup

### 1. Install `uv` (recommended)

[`uv`](https://docs.astral.sh/uv/) is a fast Python package manager. Think of it like
`npm` for Python — it handles your Python version, virtual environment, and dependencies
all in one tool.

```bash
# Install uv (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create the environment and install dependencies

```bash
# In the repo root:
uv sync
```

This reads `pyproject.toml` and installs everything into a local `.venv/` directory.

### 3. Launch Jupyter

```bash
uv run jupyter lab
```

Or if you prefer the classic interface:

```bash
uv run jupyter notebook
```

### Alternative: plain pip

If you prefer not to use `uv`:

```bash
python3 -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate
pip install -e ".[dev]"
jupyter lab
```

---

## How to Use This Repo

1. Open a module folder in `notebooks/`
2. Start with the first numbered notebook (e.g. `01_variables_and_types.ipynb`)
3. Read the explanations, run the examples, then attempt the **"Your Turn"** exercises
4. Use the **check cells** (assertion-based) to verify your answers
5. If stuck, peek at `solutions/` — but try first!
6. Update your [progress/PROGRESS.md](progress/PROGRESS.md) as you go

---

## Repo Structure

```
llm-research-lab/
├── README.md                    ← you are here
├── pyproject.toml               ← dependencies
├── .claude/CLAUDE.md            ← guidance for Claude-assisted work
├── notebooks/
│   ├── module_01_python_basics/
│   ├── module_02_data_workflows/
│   ├── module_03_debugging/
│   └── module_04 ... module_15/ (scaffolded)
├── data/
│   └── synthetic/               ← sample datasets for exercises
├── src/
│   └── checks.py                ← helper functions for exercise validation
├── progress/
│   ├── PROGRESS.md              ← your personal progress tracker
│   └── curriculum_map.md        ← detailed curriculum overview
└── tests/
    └── test_checks.py
```

---

## Validation Helpers

`src/checks.py` provides functions you can use in notebooks to verify your work:

```python
import sys
sys.path.insert(0, "../../")  # from inside a notebook
from src.checks import check_equal, check_type, check_contains
```

Or from the repo root:

```python
from src.checks import check_equal
check_equal("my_answer", expected_value, label="Exercise 1")
```

---

## Running Tests

```bash
uv run pytest
```

---

## Authorship & AI Usage

This repository was developed with the assistance of AI tools to help generate
initial lesson structure and draft content. All materials have been reviewed,
edited, and curated as part of a personal learning process.

The focus of this repo is not just on the content itself, but on developing
research-oriented thinking and workflows. It is my hope that this repo will
serve as a valuable resource for others learning Python for AI research engineering.

If you have any feedback or suggestions, please feel free to open an issue or submit
a pull request! I welcome any contributions to improve the content and make it more
useful for others.

---

## Goal

By the end of this curriculum, you will be ready to:
- Write clean, readable Python for research purposes
- Load, inspect, and analyze datasets of model outputs
- Design and run small evaluations
- Identify patterns in harmful or misleading model responses
- Organize results and write short research memos
- Begin a serious AI safety / societal impacts research project
