# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 2.1 · Two reviewers, one analysis
#
# Day 2 · Session 1 (Calibrating reviewers) · 25 min.
#
# Bader Al-Khayyal, director of marine operations, has a draft that says slot booking **halved** berth waiting at
# terminal T2 and recommends extending it to all terminals. Before it goes further, two reviewers review it alone: you
# and Faleh Al-Musharraf, a senior analyst. You re-run it, list your findings, rate each by its effect on the
# decision, then compare your ratings with Faleh's, measure the agreement beyond chance, and change the checklist where
# the two of you disagreed.
#
# **AI policy: AI-off.** The first-pass review is yours alone: no assistant, no tutor, until task 3.
#
# **Reference state.** `data/repos/berth_delay/` (the analysis, its data and its report), `data/faleh_ratings.json`
# (his ratings, sealed until task 3), `data/reference/checklist.json` (the unit's checklist).
#
# **Tasks**
# - [ ] 1 · Re-run and review alone (9')
# - [ ] 2 · Rate each finding by its effect on the decision (5')
# - [ ] 3 · Agreement table and weighted kappa (6')
# - [ ] 4 · Revise the checklist where you disagreed (5')
# - [ ] ✱ Stretch · Measure what each flaw does to the headline by fixing it alone

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

repo = U.copy_repo("berth_delay")
print((repo / "REPORT.md").read_text(encoding="utf-8"))

# %% [markdown]
# ## 1 · Re-run and review alone (9')
#
# Run the analysis, then read its code, its output and the report side by side. You may run your own checks on
# `berth_calls.csv` (counts, a comparison before the change), but you do not redo the analysis. The checklist is in
# `data/reference/checklist.json`.
#
# ✏️ **Exercise** · List your findings: a short id and one sentence each, saying where you saw it.

# %%
ok, out = U.rerun(repo, "analysis.py", full=True)
print((repo / "analysis.py").read_text(encoding="utf-8"))
print("---- output ----")
print(out)
U.check(ok, "the analysis re-runs")
calls = pd.read_csv(repo / "berth_calls.csv")
print("diverted calls (no waiting time), by terminal and period:")
print(calls.assign(period=calls.month.gt(12).map({False: "months 1-12", True: "months 13-24"}))
      .pivot_table(index="terminal", columns="period", values="diverted", aggfunc="sum"))


def my_findings() -> dict:
    # BEGIN SOLUTION
    return {
        "C1": "Cell 2 compares T2 with the other terminals after the change only; T2 already had the shortest waits before it",
        "C2": "Cell 1 drops calls without a waiting time: these are diverted calls, and they rose at T2 after the change (17 to 35)",
        "M1": "The report says 'halved'; cell 2 prints a smaller reduction",
        "M2": "Cell 3's before period at T2 includes the weather closures of months 3 and 4",
        "m1": "Table 4 is labelled minutes; the values are hours",
        "P1": "Cell 5 prints vessel masters' names and mobile numbers: personal data in an output",
    }
    # END SOLUTION


# %%
try:
    findings = my_findings()
except NotImplementedError:
    findings = {k: v["title"] for k, v in U.reference("flaws").items()}
for k, v in findings.items():
    print(f"{k}: {v}")
U.check(len(findings) >= 5, "five or more findings")

# %% [markdown]
# ## 2 · Severity by effect on the decision (5')
#
# ✏️ **Exercise** · Rate each finding 3 (critical: it changes the decision, or the output cannot leave the unit),
# 2 (major: it changes the size or the confidence of the result, not the decision) or 1 (minor: presentation). Rate
# from what the flaw does, not from how hard it was to find. Use the same ids as the reference where your finding is
# the same (`U.reference("flaws")` after you have rated, not before).

# %%
def my_ratings() -> dict:
    # BEGIN SOLUTION
    return {"C1": 3, "C2": 2, "M1": 2, "M2": 1, "m1": 1, "P1": 3}
    # END SOLUTION


# %%
try:
    mine = my_ratings()
except NotImplementedError:
    mine = {k: v["severity"] for k, v in U.reference("flaws").items()}
ref = U.reference("flaws")
found = [k for k, v in ref.items() if v["severity"] == 3 and k in mine]
print("critical flaws in the reference:", [k for k, v in ref.items() if v["severity"] == 3], "| you found:", found)
U.check(all(k in mine for k, v in ref.items() if v["severity"] == 3), "your review finds every critical flaw")

# %% [markdown]
# ## 3 · Agreement with the second reviewer (6')
#
# Now open Faleh's ratings. Percent agreement counts the findings you rated the same; weighted kappa corrects for the
# agreement you would reach by chance and counts a gap of two levels more than a gap of one (Cohen, 1968). With the
# tutor allowed again, discuss only the findings where the gap is two.

# %%
faleh = U.js("faleh_ratings")
table = U.agreement_table(mine, faleh)
print(table.to_string(index=False))
both = [k for k in table.finding if k in mine and k in faleh]
a, b = [mine[k] for k in both], [faleh[k] for k in both]
pct = 100 * sum(x == y for x, y in zip(a, b)) / len(both)
kappa = U.weighted_kappa(a, b)
print(f"agreement {pct:.0f}% on {len(both)} findings; weighted kappa {kappa:.2f}")
U.reset_role("faleh")
for q in ["Why did you rate the names and mobile numbers as minor?", "Did you count the diverted calls by terminal?"]:
    print("Q:", q, "\n ", U.sponsor("faleh", q))
U.check(len(both) >= 5, "an agreement table on at least five shared findings")

# %% [markdown]
# ## 4 · Revise the checklist where you disagreed (5')
#
# ✏️ **Exercise** · Each gap of two levels is a sentence the checklist does not yet have. Write the revision: which
# item changes, and the new wording or the new severity anchor.

# %%
def my_revisions() -> list[dict]:
    # BEGIN SOLUTION
    return [
        {"item": "P1", "change": "Add the anchor: personal data or a classification breach in an output is critical, whatever its effect on the decision, because the output cannot leave the unit."},
        {"item": "D2", "change": "Count excluded records by group and period, and say whether the exclusion is related to the outcome (a diverted call is a long wait)."},
        {"item": "severity", "change": "Rate by re-running with the flaw fixed: critical if the decision changes, major if the size changes by more than a quarter, minor otherwise."},
    ]
    # END SOLUTION


# %%
try:
    revisions = my_revisions()
except NotImplementedError:
    revisions = [{"item": "P1", "change": "Personal data in an output is critical: it cannot leave the unit."}]
big = table[table.gap >= 2].finding.tolist()
print("gaps of two:", big)
U.check(len(revisions) >= len(big), "one revision for each gap of two levels")
md = ["# Review of berth_delay: severity agreement", "", table.to_string(index=False), "",
      f"Agreement {pct:.0f}%, weighted kappa {kappa:.2f}.", "", "**Checklist revisions**"]
md += [f"- {r['item']}: {r['change']}" for r in revisions]
U.save("calibration.md", "\n".join(md) + "\n")

# %% [markdown]
# ## ✱ Stretch · What each flaw does
#
# Fix one flaw at a time and see what happens to the headline and the decision. A flaw that flips the decision is
# critical by the unit's rule.

# %%
rows = []
for fx in [set(), {"C1"}, {"C2"}, {"M2"}, {"C1", "C2"}, {"C1", "C2", "M2"}]:
    r = U.berth_run(fx)
    rows.append({"fixed": ", ".join(sorted(fx)) or "none", "effect at T2 (h)": r["effect_h"], "supports": r["decision"]})
print(pd.DataFrame(rows).to_string(index=False))

# %% [markdown]
# ## Checkpoint
#
# 1. You and Faleh agree on half the findings. Why is the weighted kappa so much lower than "half"?
#    <details><summary>Answer</summary>Two reviewers who rate mostly 1s and 3s agree often by chance; kappa removes
#    that, and the two-level gap on P1 weighs most.</details>
# 2. Why rate the names and mobile numbers critical when they do not change the decision?
#    <details><summary>Answer</summary>The unit's standard: an output with personal data cannot leave the unit, so the
#    review cannot pass whatever the analysis says.</details>
# 3. Why review alone before comparing?
#    <details><summary>Answer</summary>A second opinion formed after seeing the first is not a second opinion; the
#    disagreements are the information.</details>
#
# **Carry forward.** `out/calibration.md`. Lab 2.2 starts from `data/assisted_log.json` and `data/rules_reference.json`.
