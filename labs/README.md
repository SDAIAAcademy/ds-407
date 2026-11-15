# Leading Analytical Work: Review, Standards and Stakeholders: labs

Notebooks for the SDAIA Academy course **DS-407 Leading Analytical Work: Review, Standards and Stakeholders**. Every
lab works on **Ras Sahil Ports Authority**, a fictional port authority, and its analytics unit of twelve analysts. Each
lab starts from files supplied in `data/`, so none depends on an earlier lab, and each has a solution in `solutions/`.
All data is synthetic and generated with a fixed seed by `prepare_data.py`.

Nothing runs a model on your machine. A laptop CPU or a Colab CPU runtime is enough.

## Quick start

**Google Colab.** Open a notebook from the table below. Its first cell clones this repository and installs
`requirements-colab.txt`. To use the AI-tutor cells with a live model, add `OPENROUTER_API_KEY` in the Secrets panel
and turn on notebook access.

**Locally**, with [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/SDAIAAcademy/ds-407
cd ds-407/labs
cp .env.example .env            # optional: paste a free OpenRouter key
uv sync                         # creates .venv from pyproject.toml; uv.lock pins every version
uv run python prepare_data.py   # optional: rebuilds data/ (committed) from the seed
uv run jupyter lab
```

On Windows, set `PYTHONUTF8=1` before running if the console shows encoding errors.

Run `00_setup_check.ipynb` once before Day 1.

## Models, stand-ins and role-plays

No lab needs a model. The AI-tutor cells ask questions about your draft through a free hosted open-weight model on
OpenRouter when `OPENROUTER_API_KEY` is set; without a key, or when the model does not answer, they print a rule-based
stand-in and say so.

| Setting (`.env`) | Default | Notes |
|---|---|---|
| `OPENROUTER_API_KEY` | empty | a free key from <https://openrouter.ai/keys>; optional |
| `ASSISTANT_MODEL` | `google/gemma-4-31b-it:free` | any free model id from <https://openrouter.ai/models?max_price=0> |
| `ASSISTANT_FALLBACKS` | `google/gemma-4-26b-a4b-it:free` | tried in order when the first is busy |
| `RASSAHIL_QUICK` | `0` | `1` is accepted for the course's test runs; every lab is already fast |

Free model ids change every few weeks: if the default disappears, pick another free model.

The drafts of Musawwada, the unit's assistant, are recorded in `data/`: the labs review and audit them, they do not
generate new ones. The sponsor and the second reviewer of the role-plays (Labs 2.1 and 3.1) have scripted stand-ins
in `data/roles.json`; in class the trainer or a peer plays them, with an observer for Lab 3.1.

Day 2's first-pass review (Lab 2.1) and the audit (Lab 2.2) are AI-off: form your own judgement first.

## Notebooks

| Unit | Session | Notebook |
|---|---|---|
| Setup | Before Day 1 | [`00_setup_check.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/00_setup_check.ipynb) |
| Day 1 | Session 1 · Assurance proportionate to risk | [`D1_1_assurance_levels.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D1_1_assurance_levels.ipynb) |
| Day 1 | Session 2 · A team review checklist | [`D1_2_team_checklist.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D1_2_team_checklist.ipynb) |
| Day 1 | Session 3 · Reproducibility as a team rule | [`D1_3_rerun_repository.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D1_3_rerun_repository.ipynb) |
| Day 1 | Session 4 · Rules for AI-assisted analysis | [`D1_4_ai_rules.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D1_4_ai_rules.ipynb) |
| Day 2 | Session 1 · Calibrating reviewers | [`D2_1_calibrate_reviewers.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D2_1_calibrate_reviewers.ipynb) |
| Day 2 | Session 2 · Auditing assisted work | [`D2_2_audit_assisted.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D2_2_audit_assisted.ipynb) |
| Day 2 | Session 3 · Feedback that builds skill | [`D2_3_feedback_plan.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D2_3_feedback_plan.ipynb) |
| Day 2 | Session 4 · Review capacity and mentoring | [`D2_4_review_capacity.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D2_4_review_capacity.ipynb) |
| Day 3 | Session 1 · Scope and deadline | [`D3_1_scope_deadline.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D3_1_scope_deadline.ipynb) |
| Day 3 | Session 2 · Agreeing the evidence first | [`D3_2_analysis_agreement.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D3_2_analysis_agreement.ipynb) |
| Day 3 | Session 3 · Pressure on a finding | [`D3_3_pressure_finding.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D3_3_pressure_finding.ipynb) |
| Day 3 | Session 4 · Reporting quality and correcting errors | [`D3_4_quality_correction.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/ds-407/blob/main/labs/D3_4_quality_correction.ipynb) |
| Capstone | The night pilot staffing analysis | [`capstone/README.md`](capstone/README.md) |

Your work is saved to `labs/out/`, which is not part of the course.

## For maintainers

The notebooks are generated from the percent-format sources in `_src/` by `_tools/py2nb.py`
(`uv run python _tools/py2nb.py` from `labs/`), which also writes the solutions to `solutions/`. Edit the sources, not
the notebooks. `solutions/answer_key.md` lists every planted problem and the numbers each solution prints.
