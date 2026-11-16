# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 1.1 · Six requests, four levels
#
# Day 1 · Session 1 (Assurance proportionate to risk) · 25 min.
#
# You are Arjwan Al-Huqail, head of the analytics unit of Ras Sahil Ports Authority. Last year the unit decided the
# assurance of each request case by case. You read the log of 30 requests, write the standard that sets the level
# from the effect of an error and the complexity of the work, grade six new requests with it, and test it the only
# way that counts: does a second reviewer, working alone with your standard, reach the same levels?
#
# **AI policy: AI-tutor.** A tutor may question your definitions; it does not write the standard.
#
# **Reference state.** `data/requests.json`, `data/faleh_grades.json`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Read the log: where errors after release came from (5')
# - [ ] 2 · Write the matrix and its escalators (7')
# - [ ] 3 · Grade the six new requests (7')
# - [ ] 4 · Compare with the second reviewer and tighten one definition (6')
# - [ ] ✱ Stretch · Add the sign-off rules: who may approve at each level

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

req = U.js("requests")
log = pd.DataFrame(req["log"])
print(f"{len(log)} requests; {log.error_after_release.sum()} had an error found after release")
log[["id", "title", "use", "effect", "complexity", "public", "safety", "level_given", "error_after_release"]].head(8)

# %% [markdown]
# ## 1 · Where the errors after release came from (5')
#
# The four levels are in `req["levels"]`: 1 self-check, 2 peer review, 3 independent review, 4 independent review
# with a second opinion. Look at the log first: which kinds of request had errors after release, and what level had
# they been given? Two requests, R07 and R19, are alike: compare their levels.

# %%
for k, v in req["levels"].items():
    print(k, v["name"], "| assurer:", v["assurer"], "| approver:", v["approver"])
print(log.groupby(["effect", "level_given"]).error_after_release.agg(["count", "sum"]))
print(log[log.id.isin(["R07", "R19"])][["id", "title", "effect", "complexity", "level_given"]].to_string(index=False))

# %% [markdown]
# ## 2 · The matrix and its escalators (7')
#
# ✏️ **Exercise** · Fill the matrix: the level for each effect of an error (rows) and complexity of the work
# (columns). Then the escalators: how many levels a public release or a safety use adds. The AQuA Book grades business
# risk by the effect of an error and its likelihood, and complexity raises the likelihood.
#
# Write the definitions too: a peer applies your words, not your intentions.

# %%
def my_standard() -> dict:
    # BEGIN SOLUTION
    return {
        "matrix": {"low": {"low": 1, "medium": 1, "high": 2},
                   "medium": {"low": 2, "medium": 2, "high": 3},
                   "high": {"low": 3, "medium": 3, "high": 4}},
        "escalators": {"public": 1, "safety": 1},
        "max_level": 4,
        "definitions": {
            "effect high": "an error could change a board, safety, tariff or capital decision, or cost more than one million riyals",
            "effect medium": "an error could change an operational decision for a month or more, or a published figure",
            "effect low": "an error would be noticed and corrected within a week with no lasting effect",
            "complexity high": "a model, a forecast or a method new to the unit",
            "complexity medium": "several sources joined, or a comparison over time or groups",
            "complexity low": "a count or average from one source, by a method the unit uses every month",
            "public": "the figure leaves the authority (bulletin, ministry indicator, regulator)",
            "safety": "the result sets safety staffing (pilots on duty), a navigation limit or a safety rule",
        },
    }
    # END SOLUTION


# %%
try:
    standard = my_standard()
except NotImplementedError:
    standard = U.reference("assurance") | {"definitions": {}}
t = U.log_table(standard)
under = t[t.under_assured]
print(f"under-assured by your standard: {len(under)} of 30; errors after release among them: {under.error_after_release.sum()}")
print(f"errors after release among the others: {t[~t.under_assured].error_after_release.sum()} of {len(t) - len(under)}")
U.check(all(standard["matrix"][e][c] >= 1 for e in U.EFFECTS for c in U.EFFECTS), "every cell of the matrix has a level")
U.check(all(standard["matrix"]["high"][c] >= standard["matrix"]["low"][c] for c in U.EFFECTS), "a higher effect never gets a lower level")
U.check(under.error_after_release.sum() >= 4, "the requests your standard calls under-assured hold most of the errors")

# %% [markdown]
# ## 3 · Grade the six new requests (7')
#
# ✏️ **Exercise** · Grade each new request with your definitions: effect, complexity, public, safety. The level then
# comes from your standard, not from you. N5 holds personal data: the level does not change, but the data protection
# officer's check is added (write it in `notes`).

# %%
for n in req["new"]:
    print(f"{n['id']} {n['title']}\n    {n['detail']} (use: {n['use']})")


def my_grades() -> dict:
    # BEGIN SOLUTION
    return {
        "N1": {"effect": "medium", "complexity": "low", "public": False, "safety": False},
        "N2": {"effect": "high", "complexity": "medium", "public": False, "safety": False},
        "N3": {"effect": "high", "complexity": "high", "public": False, "safety": True},
        "N4": {"effect": "medium", "complexity": "low", "public": True, "safety": False},
        "N5": {"effect": "low", "complexity": "medium", "public": False, "safety": False,
               "notes": "personal data: the data protection officer checks the output before it leaves the unit"},
        "N6": {"effect": "high", "complexity": "medium", "public": False, "safety": False},
    }
    # END SOLUTION


# %%
try:
    grades = my_grades()
except NotImplementedError:
    grades = U.reference("assurance")["grades"]
mine = U.apply_standard(standard, grades)
print("your levels:", mine)
U.check(set(mine) == {f"N{i}" for i in range(1, 7)}, "six requests graded")

# %% [markdown]
# ## 4 · The second reviewer, working alone (6')
#
# Faleh Al-Musharraf, a senior analyst, graded the six requests without seeing your grades. His levels come from
# **your** standard applied to **his** grades. Where you differ, the definitions were not clear enough: tighten the
# one that caused the difference, and say which.

# %%
faleh = U.js("faleh_grades")
his = U.apply_standard(standard, faleh)
rows = [{"request": k, "you": mine[k], "Faleh": his[k],
         "differs on": ", ".join(f for f in ("effect", "complexity", "public", "safety") if grades[k].get(f) != faleh[k].get(f))}
        for k in sorted(mine)]
agree = pd.DataFrame(rows)
print(agree.to_string(index=False))
same = int((agree.you == agree.Faleh).sum())
print(f"same level on {same} of 6")


def tightened_definition() -> str:
    # BEGIN SOLUTION
    return ("public: the figure leaves the authority, including a ministry indicator or a statistic published once a "
            "year; a figure shown only to the board is not public")
    # END SOLUTION


# %%
try:
    tighter = tightened_definition()
except NotImplementedError:
    tighter = "(not written yet)"
U.check(same >= 5, "a peer with your standard reaches your level on at least five of six requests")
md = ["# Assurance standard, Ras Sahil analytics unit (draft)", "", "| effect \\ complexity | low | medium | high |", "|---|---|---|---|"]
md += [f"| {e} | " + " | ".join(str(standard["matrix"][e][c]) for c in U.EFFECTS) + " |" for e in U.EFFECTS]
md += ["", f"Escalators: {standard['escalators']} (at most level {standard['max_level']}).", "", "**Definitions**"]
md += [f"- {k}: {v}" for k, v in standard.get("definitions", {}).items()]
md += ["", f"**Tightened after the comparison.** {tighter}", "", "**The six new requests**", agree.to_string(index=False)]
U.save("standard.md", "\n".join(md) + "\n")
print(U.tutor("\n".join(md), "would a peer read my definitions the same way?"))

# %% [markdown]
# ## ✱ Stretch · Sign-off rules
#
# For each level, who may sign the work off? The AQuA Book separates the analyst, the assurer and the approver. Write
# one line per level, and one rule that holds at every level.

# %%
signoff = {
    1: "the requester's manager, after the analyst's checklist",
    2: "a senior analyst, after a peer's review",
    3: "the head of the unit, after an independent senior review",
    4: "the head of the unit and the requesting director, after two reviews",
    "always": "nobody signs off work they analysed or assured",
}
print(signoff)

# %% [markdown]
# ## Checkpoint
#
# 1. Why does the log show more errors after release among under-assured requests?
#    <details><summary>Answer</summary>They are the high-effect or public requests that got a self-check: the errors
#    nobody caught were found by the readers, after release.</details>
# 2. R07 and R19 are the same kind of request. What did their levels show?
#    <details><summary>Answer</summary>Level 1 and level 3 for the same profile: without a written standard, the
#    level depended on who asked and who was free.</details>
# 3. Why test the standard with a second reviewer instead of reading it again?
#    <details><summary>Answer</summary>The author reads intentions into the words; a peer applies only the words. Where
#    the levels differ, a definition is ambiguous.</details>
#
# **Carry forward.** `out/standard.md`. Lab 1.2 starts from `data/reforms_items.json`.
