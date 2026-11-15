# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 1.2 · A checklist adapted from REFORMS
#
# Day 1 · Session 2 (A team review checklist) · 25 min.
#
# In DS-310 you used a personal checklist of five areas. A unit of twelve needs one checklist that every reviewer
# applies the same way, at the level the standard sets. You adapt a published one: REFORMS, 32 reporting items for
# machine-learning-based science in 8 modules (Kapoor et al., 2024). You keep, rewrite or drop each item for the
# unit's work, add the privacy and classification check that every output passes, and set the level of each item.
#
# **AI policy: AI-tutor.** A tutor may question your items; it does not write them.
#
# **Reference state.** `data/reforms_items.json` (our short paraphrase of each item, with its REFORMS id).
#
# **Tasks**
# - [ ] 1 · Map the 32 items to the five review areas (6')
# - [ ] 2 · Keep, rewrite or drop each item (8')
# - [ ] 3 · Add the privacy and classification item (4')
# - [ ] 4 · Set the level of each item and test the length (7')
# - [ ] ✱ Stretch · Add one item for work an assistant drafted

# %%
import os, sys, subprocess
from pathlib import Path

IN_COLAB = "google.colab" in sys.modules
if IN_COLAB:
    REPO_URL = "https://github.com/SDAIAAcademy/ds-407.git"
    if not Path("/content/ds-407").exists():
        subprocess.run(["git", "clone", "-q", REPO_URL, "/content/ds-407"], check=True)
    os.chdir("/content/ds-407/labs")
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements-colab.txt"], check=True)
else:
    while not Path("rassahil.py").exists() and Path.cwd() != Path.cwd().parent:
        os.chdir("..")  # solutions/ notebooks run from labs/
sys.path.insert(0, os.getcwd())

import pandas as pd
import rassahil as U

items = pd.DataFrame(U.js("reforms_items"))
print(items.groupby("module", sort=False).size().to_string())

# %% [markdown]
# ## 1 · Map the items to the five areas (6')
#
# ✏️ **Exercise** · The five areas of a review are question fit, data, method, inference and communication. Map each
# REFORMS module to the area it mostly serves. Modules are about machine-learning studies; most of the unit's work is
# descriptive and comparative, so expect some modules to matter little.

# %%
def module_to_area() -> dict:
    # BEGIN SOLUTION
    return {"Study goals": "question fit", "Computational reproducibility": "data", "Data quality": "data",
            "Data preprocessing": "data", "Modelling": "method", "Data leakage": "method",
            "Metrics and uncertainty": "inference", "Generalisability and limitations": "inference"}
    # END SOLUTION


# %%
try:
    m2a = module_to_area()
except NotImplementedError:
    m2a = {"Study goals": "question fit", "Computational reproducibility": "data", "Data quality": "data",
           "Data preprocessing": "data", "Modelling": "method", "Data leakage": "method",
           "Metrics and uncertainty": "inference", "Generalisability and limitations": "inference"}
items["area"] = items.module.map(m2a)
print(items.groupby("area").size().to_string())
U.check(items.area.notna().all(), "every module has an area")
print("no REFORMS module serves communication: the unit must write those items itself")

# %% [markdown]
# ## 2 · Keep, rewrite or drop (8')
#
# ✏️ **Exercise** · Write the unit's items. Each is a **question** a reviewer answers yes or no, with the
# **evidence** that answers it, the REFORMS ids it comes `from` (empty when it is the unit's own), its `area`, and
# `min_level`: the lowest assurance level at which it is required. Merge items that a reviewer checks together (2a to
# 2e become one re-run item). Drop what the unit's work does not need, and say why in `dropped`.

# %%
def my_checklist() -> list[dict]:
    # BEGIN SOLUTION
    return [
        {"id": "Q1", "area": "question fit", "from": ["1a"], "item": "Does the analysis answer the decision question in the agreement, for the population it names?", "evidence": "the agreement and the headline cell", "min_level": 1},
        {"id": "Q2", "area": "question fit", "from": [], "item": "Is the decision rule written down before the results, and is the result read against it?", "evidence": "the dated agreement", "min_level": 2},
        {"id": "D1", "area": "data", "from": ["2a", "3a"], "item": "Are the data sources and extract dates recorded, so the same files can be found again?", "evidence": "the data manifest", "min_level": 1},
        {"id": "D2", "area": "data", "from": ["4a", "3f"], "item": "Are excluded and missing records counted, with the reason for each exclusion?", "evidence": "a count per exclusion step", "min_level": 1},
        {"id": "D3", "area": "data", "from": ["6b"], "item": "Have duplicates been looked for, and removed or explained?", "evidence": "the duplicate count", "min_level": 2},
        {"id": "R1", "area": "data", "from": ["2b", "2c", "2d", "2e"], "item": "Does the analysis re-run from the repository, with the lock file and the README alone, to the reported numbers?", "evidence": "the re-run log", "min_level": 2},
        {"id": "M1", "area": "method", "from": ["5f"], "item": "Is the comparison fair: a baseline, a control group, the same period?", "evidence": "the comparison cell", "min_level": 1},
        {"id": "M2", "area": "method", "from": ["5c", "6a", "6c"], "item": "For a model: is it tested on data it never saw, with only legitimate features?", "evidence": "the split and the feature list", "min_level": 3},
        {"id": "I1", "area": "inference", "from": ["7b"], "item": "Is uncertainty stated for every number the decision depends on?", "evidence": "an interval or a range", "min_level": 2},
        {"id": "I2", "area": "inference", "from": ["3g", "8a", "8b"], "item": "Are the groups and conditions where the result does not hold named?", "evidence": "the subgroup table", "min_level": 2},
        {"id": "C1", "area": "communication", "from": [], "item": "Does every number in the text match the output it comes from?", "evidence": "each number traced to a cell", "min_level": 1},
    ]
    # END SOLUTION


def dropped() -> dict:
    # BEGIN SOLUTION
    return {"1c": "most of the unit's work uses no machine learning; M2 covers models when they appear",
            "5a, 5b, 5d, 5e": "model documentation belongs in the model's own record, checked under M2 at level 3",
            "3e": "a count of records is part of D2"}
    # END SOLUTION


# %%
try:
    checklist = my_checklist()
except NotImplementedError:
    checklist = [i for i in U.reference("checklist") if not i.get("privacy") and i["id"] != "C2"]
try:
    why_dropped = dropped()
except NotImplementedError:
    why_dropped = {}
used = sorted({r for i in checklist for r in i.get("from", [])})
print(f"{len(checklist)} items, built from {len(used)} of 32 REFORMS items; dropped with a reason: {list(why_dropped)}")
U.check(all(i["item"].strip().endswith("?") for i in checklist), "every item is a question")

# %% [markdown]
# ## 3 · The privacy and classification item (4')
#
# ✏️ **Exercise** · Nothing leaves the unit before this check: no personal data in an output unless the purpose allows
# it, and the classification marked and respected (the NDMO Data Classification Policy; the Personal Data Protection
# Law). Write it as an item with `"privacy": True` and `min_level` 1.

# %%
def privacy_item() -> dict:
    # BEGIN SOLUTION
    return {"id": "P1", "area": "communication", "from": [], "privacy": True, "min_level": 1,
            "item": "Before anything leaves the unit: is it free of personal data, and is its classification marked and respected?",
            "evidence": "the classification mark and a scan of the output"}
    # END SOLUTION


# %%
try:
    p1 = privacy_item()
except NotImplementedError:
    p1 = next(i for i in U.reference("checklist") if i.get("privacy"))
checklist = [i for i in checklist if not i.get("privacy")] + [p1]

# %% [markdown]
# ## 4 · Levels and length (7')
#
# A checklist that is too long is skipped. Look at how many items apply at each level, then run the problems check.
# Fix what it reports in your cells above and run again.

# %%
for lvl in (1, 2, 3, 4):
    ids = U.items_at_level(checklist, lvl)
    print(f"level {lvl}: {len(ids):2d} items  {ids}")
probs = U.checklist_problems(checklist)
print("problems:", probs or "none")
U.check(not probs, "the checklist passes the problems check")
md = ["# Review checklist, Ras Sahil analytics unit (draft)", "", "| id | area | question | evidence | from level | REFORMS |", "|---|---|---|---|---|---|"]
md += [f"| {i['id']} | {i['area']} | {i['item']} | {i['evidence']} | {i['min_level']} | {', '.join(i.get('from', [])) or 'unit'} |" for i in checklist]
md += ["", "**Dropped**"] + [f"- {k}: {v}" for k, v in why_dropped.items()]
U.save("checklist.md", "\n".join(md) + "\n")
U.save("checklist.json", __import__("json").dumps(checklist, indent=2))
print(U.tutor("\n".join(i["item"] for i in checklist), "would two reviewers answer these the same way?"))

# %% [markdown]
# ## ✱ Stretch · Assisted work
#
# Add one item for work an assistant drafted. Lab 1.4 writes the rules it checks.

# %%
assisted = {"id": "C2", "area": "communication", "from": [], "min_level": 1,
            "item": "Is any part drafted by an assistant disclosed, and was each of its numbers re-run?",
            "evidence": "the disclosure line and the verification record"}
print(U.checklist_problems(checklist + [assisted]) or "still passes with the assisted-work item")

# %% [markdown]
# ## Checkpoint
#
# 1. Why adapt REFORMS instead of adopting all 32 items?
#    <details><summary>Answer</summary>It was written for machine-learning studies; most of the unit's work is
#    descriptive and comparative. A checklist reviewers skip protects nothing.</details>
# 2. Why is the privacy and classification item required from level 1?
#    <details><summary>Answer</summary>The harm of personal data leaving the unit does not depend on how important the
#    analysis is: a self-checked dashboard can leak as well as a board paper.</details>
# 3. What makes an item answerable the same way by two reviewers?
#    <details><summary>Answer</summary>A yes-or-no question and named evidence: "the re-run log", not "is the work
#    reproducible".</details>
#
# **Carry forward.** `out/checklist.json`. Lab 2.1 starts from `data/reference/checklist.json`.
