# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 3.2 · An analysis agreement
#
# Day 3 · Session 2 (Agreeing the evidence first) · 25 min.
#
# Bader agreed the scope. Before anyone computes the effect of slot booking, you and he sign an analysis agreement:
# the question, the options, the decision rule, and the evidence threshold, the change in waiting that would make the
# board extend slot booking. A threshold the data cannot detect is a promise nobody can keep, so you compute what the
# data can detect first.
#
# **AI policy: AI-tutor.** A tutor may question your agreement; it does not write it.
#
# **Reference state.** `data/berth_calls.csv`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · The decision and its options (5')
# - [ ] 2 · Compute the change the data can detect (8')
# - [ ] 3 · Set the decision rule and the threshold (7')
# - [ ] 4 · Roles, level and sign-off (5')
# - [ ] ✱ Stretch · Say in the agreement what happens when the result falls between the thresholds

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

calls = U.csv("berth_calls")
print(f"{len(calls):,} calls, months {calls.month.min()} to {calls.month.max()}; slot booking at T2 from month 13")

# %% [markdown]
# ## 1 · The decision and its options (5')
#
# ✏️ **Exercise** · Write the question as the board's choice, with at least two options, one of them not to extend.

# %%
def decision() -> dict:
    # BEGIN SOLUTION
    return {"question": "Should slot booking be extended from T2 to all four terminals next quarter?",
            "options": ["Extend to all terminals", "Keep at T2 only and fix the feeder slots", "Stop slot booking"]}
    # END SOLUTION


# %%
try:
    dec = decision()
except NotImplementedError:
    dec = U.reference("agreement")["decision"]
print(dec)

# %% [markdown]
# ## 2 · What the data can detect (8')
#
# The comparison is a difference in differences: T2 against the other terminals, before against after. With more
# months after the change, the estimate is more precise. `U.did_by_month(calls, m)` gives the estimate's standard
# error with `m` months after the change and the minimum detectable change (about 2.8 standard errors: 80% power at a
# 5% two-sided test). Weather-closure calls are left out and diverted calls count at 24 hours, the rules the review
# of Day 2 agreed.
#
# ✏️ **Exercise** · Tabulate the minimum detectable change for 3, 6 and 12 months after the change. Do **not** look
# at the estimate column yet: the threshold is set before the result is seen.

# %%
def detectable(calls: pd.DataFrame) -> pd.DataFrame:
    # BEGIN SOLUTION
    return pd.DataFrame([U.did_by_month(calls, m) for m in (3, 6, 12)])[["months_after", "se_h", "mdc_h"]]
    # END SOLUTION


# %%
try:
    mdc = detectable(calls)
except NotImplementedError:
    mdc = pd.DataFrame(U.reference("agreement")["mdc"])
print(mdc.to_string(index=False))
U.check(set(mdc.months_after) == {3, 6, 12} and "estimate_h" not in mdc, "detectable change for 3, 6 and 12 months, estimate not shown")

# %% [markdown]
# ## 3 · The decision rule and the threshold (7')
#
# Bader's first wish was "extend it if waiting falls at all". The operations team says a berth hour saved per call is
# worth the cost of slot booking only from **2 hours** per call. A threshold the data cannot detect is not a rule.
#
# ✏️ **Exercise** · Write the decision rule with numbers: the threshold in hours, the data window, and the condition
# on vessel types (no type worse by more than 2 hours). Check the threshold against the detectable change.

# %%
def rule() -> dict:
    # BEGIN SOLUTION
    return {"decision_rule": "Extend if waiting at T2 falls by at least 2.0 hours per call against the other terminals, and no vessel type waits more than 2.0 hours longer; otherwise keep at T2 and fix the slots for the type that lost.",
            "evidence_threshold_h": 2.0,
            "data": "Berth calls of months 1 to 24 (12 months after the change), weather-closure calls left out, diverted calls at 24 hours"}
    # END SOLUTION


# %%
try:
    r = rule()
except NotImplementedError:
    r = U.reference("agreement")["rule"]
mdc12 = float(mdc[mdc.months_after == 12].mdc_h.iloc[0])
print(f"threshold {r['evidence_threshold_h']} h; detectable with 12 months: {mdc12} h")
U.check(r["evidence_threshold_h"] >= mdc12, "the threshold is larger than what the data can detect")

# %% [markdown]
# ## 4 · Roles, level and sign-off (5')
#
# ✏️ **Exercise** · Complete the agreement: the assurance level (N6 in Lab 1.1), the analyst, the assurer and the
# approver (three different people), and that it is signed before the analysis.

# %%
def roles() -> dict:
    # BEGIN SOLUTION
    return {"level": 3, "analyst": "Saleh Al-Ghamlas", "assurer": "Faleh Al-Musharraf", "approver": "Arjwan Al-Huqail (head of the unit)",
            "commissioner": "Bader Al-Khayyal", "signed_before": "the analysis starts; any change to the rule is dated and signed again"}
    # END SOLUTION


# %%
try:
    rl = roles()
except NotImplementedError:
    rl = U.reference("agreement")["roles"]
agreement = {**dec, **r, **rl, "decision": dec["question"]}
probs = U.agreement_problems(agreement)
print("problems:", probs or "none")
U.check(not probs, "the agreement is complete")
md = ["# Analysis agreement: slot booking", ""] + [f"**{k.replace('_', ' ').capitalize()}.** {v if not isinstance(v, list) else '; '.join(v)}" for k, v in agreement.items()]
md += ["", "**What the data can detect**", mdc.to_string(index=False)]
U.save("analysis_agreement.md", "\n".join(md) + "\n")
print(U.tutor("\n".join(md), "would the sponsor and the analyst read the decision rule the same way?"))

# %% [markdown]
# Now, and only now, the estimate. Read it against the rule you signed.

# %%
est = U.did_by_month(calls, 12)
print(f"estimate with 12 months: {est['estimate_h']} h (standard error {est['se_h']})")
print("feeders:", U.subgroup_did("feeder"), "h; other vessel types:", U.subgroup_did(exclude="feeder"), "h")

# %% [markdown]
# ## ✱ Stretch · Between the thresholds
#
# What does the agreement say if the fall is real but smaller than 2 hours, as it is here? Write it, so the board is
# not left to decide after seeing the number.

# %%
print("Between the detectable change and the threshold: the effect is real but below the value that pays for "
      "extension; the recommendation is to keep slot booking at T2, fix the feeder slots and measure again in six months.")

# %% [markdown]
# ## Checkpoint
#
# 1. Why compute the detectable change before seeing the estimate?
#    <details><summary>Answer</summary>A threshold chosen after the result can be set to make the result pass; set
#    before, it is a test.</details>
# 2. "Extend if waiting falls at all": what is wrong with that rule?
#    <details><summary>Answer</summary>Any fall smaller than about 0.6 hours cannot be told from noise with these data,
#    and a tiny fall does not pay for slot booking.</details>
# 3. Why must the analyst, assurer and approver be three people?
#    <details><summary>Answer</summary>The standard separates them: nobody assures or approves their own analysis.</details>
#
# **Carry forward.** `out/analysis_agreement.md`. Lab 3.3 starts from `data/khaled_request.md`.
