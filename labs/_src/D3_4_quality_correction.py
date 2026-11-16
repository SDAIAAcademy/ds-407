# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 3.4 · A quality statement and a correction
#
# Day 3 · Session 4 (Reporting quality and correcting errors) · 25 min.
#
# Two pieces of writing close the week. First, the quality statement of the slot-booking board paper: what was
# checked, by whom, at which level, and what remains uncertain, short enough for a board to read. Second, a
# correction: the Q2 mean import dwell released in last quarter's board paper was wrong. You find why, size the
# error, and write the notice.
#
# **AI policy: AI-tutor.** A tutor may question your drafts; it does not write them.
#
# **Reference state.** `data/containers_q2_released.csv` (the extract behind the released figure),
# `data/unit_standard.md`, `data/berth_calls.csv`.
#
# **Tasks**
# - [ ] 1 · Write the quality statement (8')
# - [ ] 2 · Find and size the Q2 error (7')
# - [ ] 3 · Write the correction notice (7')
# - [ ] 4 · Check both against the standard (3')
# - [ ] ✱ Stretch · Decide who is told of the correction, and in which order

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

est = U.did_by_month(U.csv("berth_calls"), 12)
print(f"slot-booking estimate: {est['estimate_h']} h per call (standard error {est['se_h']}); feeders {U.subgroup_did('feeder')} h")

# %% [markdown]
# ## 1 · The quality statement (8')
#
# ✏️ **Exercise** · A board reads it in a minute: the assurance level, what was checked, by whom, what remains
# uncertain (with a number), whether an assistant drafted any part, and the classification. At most 160 words.

# %%
def my_statement() -> dict:
    # BEGIN SOLUTION
    lo, hi = round(est["estimate_h"] - 2 * est["se_h"], 1), round(est["estimate_h"] + 2 * est["se_h"], 1)
    return {
        "level": "Level 3, independent review, approved by the head of the analytics unit",
        "checked": ["re-run from the repository to the same figures", "comparison with the other terminals over the same months",
                    "every number in the text traced to its output", "no personal data in the paper"],
        "by_whom": "Analysis by Saleh Al-Ghamlas; independent review by Faleh Al-Musharraf; approval by Arjwan Al-Huqail",
        "uncertain": [f"the fall in waiting at T2 is {abs(est['estimate_h'])} hours per call, likely between {abs(hi)} and {abs(lo)}",
                      "diverted calls are counted at 24 hours, a lower bound of their wait"],
        "assisted": "The first draft of the method section was written with the authority's approved assistant and verified line by line",
        "classification": "Internal",
    }
    # END SOLUTION


# %%
try:
    st = my_statement()
except NotImplementedError:
    st = U.reference("quality")["statement"]
p1 = U.statement_problems(st)
print("problems:", p1 or "none")

# %% [markdown]
# ## 2 · The Q2 error (7')
#
# Last quarter's board paper said Q2 mean import dwell was the figure below. A colleague re-running it this week got a
# different number. Look at the extract: count rows per week, look for containers that appear twice.
#
# ✏️ **Exercise** · Return the released figure, the corrected figure, the number of duplicated rows and the weeks
# they come from.

# %%
q2 = U.csv("containers_q2_released")
print(q2.groupby("week").size().to_string())


def size_error(q2: pd.DataFrame) -> dict:
    # BEGIN SOLUTION
    released = round(float(q2[q2.move_type == "import"].dwell_days.mean()), 2)
    dup = q2.duplicated(subset=["container_id"], keep="first")
    clean = q2[~dup]
    corrected = round(float(clean[clean.move_type == "import"].dwell_days.mean()), 2)
    return {"released": released, "corrected": corrected, "duplicates": int(dup.sum()),
            "weeks": sorted(int(w) for w in q2[dup].week.unique())}
    # END SOLUTION


# %%
try:
    err = size_error(q2)
except NotImplementedError:
    err = U.reference("quality")["error"]
print(err)
U.check(err["corrected"] == U.reference("summary")["cargo"]["q2_corrected"], "the corrected figure matches the clean extract")

# %% [markdown]
# ## 3 · The correction notice (7')
#
# ✏️ **Exercise** · What was wrong, the released and corrected values, the cause (in the process, not a person),
# whether any decision used the wrong figure, what changes in the process, and who is told.

# %%
def my_notice() -> dict:
    # BEGIN SOLUTION
    return {
        "what_was_wrong": "The Q2 mean import dwell in last quarter's board paper",
        "released_value": f"{err['released']} days",
        "corrected_value": f"{err['corrected']} days",
        "cause": f"Two weeks of the extract (weeks {', '.join(map(str, err['weeks']))}) were loaded twice when the terminal system re-sent them; the duplicated weeks had short dwell, so the mean was understated",
        "decisions_affected": "The figure was quoted in the storage-fee discussion; no fee was changed on it. The Q3 comparison in the quarterly note used the corrected figure.",
        "process_change": "Every extract is checked for duplicate container ids before analysis (checklist item D3, now from level 1 for published figures)",
        "who_is_told": ["the board secretary", "the readers of the quarterly note", "the ministry indicator team, which received the figure"],
    }
    # END SOLUTION


# %%
try:
    notice = my_notice()
except NotImplementedError:
    notice = U.reference("quality")["notice"]
p2 = U.notice_problems(notice)
print("problems:", p2 or "none")

# %% [markdown]
# ## 4 · Check against the standard (3')
#
# The unit's standard (`data/unit_standard.md`) says what a quality statement and a correction contain. Fix what the
# checks report.

# %%
print([l for l in U.text("unit_standard.md").splitlines() if l.startswith(("S-9", "S-10"))])
U.check(not p1, "the quality statement passes the checks")
U.check(not p2, "the correction notice passes the checks")
md = ["# Quality statement: slot-booking board paper", ""] + [f"**{k.replace('_', ' ').capitalize()}.** {v if not isinstance(v, list) else '; '.join(v)}" for k, v in st.items()]
md += ["", "# Correction notice", ""] + [f"**{k.replace('_', ' ').capitalize()}.** {v if not isinstance(v, list) else '; '.join(v)}" for k, v in notice.items()]
U.save("quality_and_correction.md", "\n".join(md) + "\n")
print(U.tutor("\n".join(md), "would a board member understand what is uncertain?"))

# %% [markdown]
# ## ✱ Stretch · Who is told first
#
# Order the people to tell, and say why the order matters.

# %%
print("1 the board secretary (the paper of record), 2 the ministry indicator team (the figure left the authority), "
      "3 the readers of the quarterly note. Those who acted on it first; then those who only read it.")

# %% [markdown]
# ## Checkpoint
#
# 1. Why give the uncertainty as a range instead of "results may vary"?
#    <details><summary>Answer</summary>A board can weigh a range against the threshold of 2 hours; it cannot weigh a
#    phrase.</details>
# 2. Why does the notice name the process and not the analyst?
#    <details><summary>Answer</summary>The cause is a load that accepted duplicates and a check that did not exist;
#    naming a person discourages the next correction.</details>
# 3. The corrected figure is higher. Does that make the correction less urgent?
#    <details><summary>Answer</summary>No: the direction does not matter. The figure left the authority, so every
#    reader of it is told.</details>
#
# **Carry forward.** `out/quality_and_correction.md`. The capstone starts from `capstone/README.md`.
