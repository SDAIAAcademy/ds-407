# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 2.2 · Audit five assisted analyses
#
# Day 2 · Session 2 (Auditing assisted work) · 25 min.
#
# The unit adopted rules for assisted work last quarter. You audit five analyses that Musawwada helped draft, as they
# appear in the unit's log: their disclosure lines, the data each sent to the assistant, the prompts kept and the
# verification records. An audit checks the evidence a rule asks for, not the analyst's word. One headline can be
# recomputed from the authority's own data: you recompute it.
#
# **AI policy: AI-off for the audit.** The tutor may question your audit table afterwards.
#
# **Reference state.** `data/rules_reference.json` (the unit's rules: Lab 1.4's reference set),
# `data/assisted_log.json`, `data/berth_calls.csv`.
#
# **Tasks**
# - [ ] 1 · Read the rules and the log (4')
# - [ ] 2 · Check each record against the rules (9')
# - [ ] 3 · Recompute one headline number (7')
# - [ ] 4 · Write the audit table (5')
# - [ ] ✱ Stretch · Propose the one rule change the audit suggests

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

import json
import pandas as pd
import rassahil as U

# %% [markdown]
# ## 1 · The rules and the log (4')

# %%
rules = U.js("rules_reference")
for part, rs in rules.items():
    for r in rs:
        print(f"{r['id']:3} [{part}] {r['rule']}")
log = U.js("assisted_log")
for a in log:
    print(f"\n{a['id']} {a['title']} (analyst: {a['analyst']}, reviewer: {a['reviewer']})")
    for k in ("tool", "data_class", "disclosure", "prompts_kept", "verification", "headline", "note"):
        if k in a:
            print(f"   {k}: {a[k]}")

# %% [markdown]
# ## 2 · Check each record (9')
#
# ✏️ **Exercise** · For each analysis, list the ids of the rules it breaks, from the evidence in its record. No
# evidence is a breach of a "keep" rule even when the analyst says the work was done.

# %%
def my_breaches() -> dict:
    # BEGIN SOLUTION
    return {"A1": [], "A2": ["C1"], "A3": ["V1", "K2"], "A4": ["D1"], "A5": ["K1", "K2"]}
    # END SOLUTION


# %%
try:
    breaches = my_breaches()
except NotImplementedError:
    breaches = U.reference("audit")["breaches"]
key = U.reference("audit")["breaches"]
for a in key:
    got, want = set(breaches.get(a, [])), set(key[a])
    print(f"{a}: you {sorted(got) or 'none'}  reference {sorted(want) or 'none'}  {'same' if got == want else 'differs'}")
U.check(sum(set(breaches.get(a, [])) == set(key[a]) for a in key) >= 4, "at least four of five analyses audited as the reference")

# %% [markdown]
# ## 3 · Recompute the headline of A3 (7')
#
# A3 says: "18.4% of calls at T1 waited more than 12 hours" in months 13 to 24. Its verification record is empty.
#
# ✏️ **Exercise** · Recompute it from `berth_calls.csv`: calls at T1, months 13 to 24, with a recorded waiting time,
# the share above 12 hours. Then say how many calls were diverted (no waiting time) and whether that changes the
# reading.

# %%
calls = U.csv("berth_calls")


def recompute_a3(calls: pd.DataFrame) -> dict:
    # BEGIN SOLUTION
    t1 = calls[(calls.terminal == "T1") & (calls.month >= 13)]
    recorded = t1.dropna(subset=["wait_h"])
    share = round(100 * float((recorded.wait_h > 12).mean()), 1)
    return {"share_pct": share, "calls": len(recorded), "diverted": int(t1.diverted.sum())}
    # END SOLUTION


# %%
try:
    a3 = recompute_a3(calls)
except NotImplementedError:
    a3 = {"share_pct": U.reference("audit")["a3_recomputed_pct"], "calls": None, "diverted": None}
print(f"A3 says 18.4%; the data say {a3['share_pct']}% ({a3['calls']} calls with a waiting time, {a3['diverted']} diverted)")
U.check(a3["share_pct"] == U.reference("audit")["a3_recomputed_pct"], "A3's headline recomputed")

# %% [markdown]
# ## 4 · The audit table (5')
#
# One row per analysis: the breaches, the evidence, what must happen before the work is used again, and who acts.

# %%
actions = {
    "A1": ("none", "no action"),
    "A2": ("restricted data (names and shifts of pilots) sent to the assistant", "report to the data protection officer; redo on anonymised data"),
    "A3": (f"headline 18.4% never re-run; the data give {a3['share_pct']}%", "withdraw the figure; re-run and re-review"),
    "A4": ("board paper sent without a disclosure line", "send a disclosure note to the board secretary"),
    "A5": ("no prompts and no verification record kept", "re-run the figures and keep the record before reuse"),
}
audit = pd.DataFrame([{"analysis": a, "breaches": ", ".join(breaches.get(a, [])) or "none", "evidence": actions[a][0], "action": actions[a][1]} for a in key])
print(audit.to_string(index=False))
U.save("audit.md", "# Audit of five assisted analyses\n\n" + audit.to_string(index=False) + "\n")
print(U.tutor(audit.to_string(index=False), "does each action follow from the breach?"))

# %% [markdown]
# ## ✱ Stretch · One rule change
#
# Two of five analyses had no verification record. Which change to the rules would make the gap visible before the
# work leaves the unit?

# %%
print("K3 (proposed): the reviewer does not start a review of assisted work without its verification record; "
      "the checklist item C2 asks for it.")

# %% [markdown]
# ## Checkpoint
#
# 1. A5's analyst says he checked the numbers. Why is it still a breach?
#    <details><summary>Answer</summary>The rule asks for a record; an audit sees evidence, not intentions. Without the
#    record nobody can tell which numbers were checked.</details>
# 2. Which breach did only the recomputation reveal?
#    <details><summary>Answer</summary>That A3's 18.4% is wrong: the record showed it was not verified, but only the
#    recomputation showed by how much.</details>
# 3. A2 used the approved tool and re-ran its figures. Why is it the most serious?
#    <details><summary>Answer</summary>Restricted personal data left the authority's control; no later step undoes
#    that, and the data protection officer must be told.</details>
#
# **Carry forward.** `out/audit.md`. Lab 2.3 starts from `data/shaden_review.json` and `data/analysts.json`.
