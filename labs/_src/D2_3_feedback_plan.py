# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 2.3 · Feedback and a three-month plan
#
# Day 2 · Session 3 (Feedback that builds skill) · 25 min.
#
# Shaden Al-Ruwayshid joined the unit six months ago. Faleh reviewed her notebook on berth waiting and cargo dwell and
# found seven things. You turn the review into feedback she can act on: three findings, each with what you saw, what
# it does to the decision, the reasoning she missed and the next step. Then a three-month plan built on her skills
# profile, with unaided practice in it.
#
# **AI policy: AI-tutor.** A tutor may question your notes; it does not write them.
#
# **Reference state.** `data/shaden_review.json`, `data/analysts.json` (skills profiles, 1 to 4).
#
# **Tasks**
# - [ ] 1 · Choose three findings to raise (5')
# - [ ] 2 · Write each note: observation, effect, reasoning, next step (9')
# - [ ] 3 · A three-month plan from the skills profile (8')
# - [ ] 4 · Check that every line is specific (3')
# - [ ] ✱ Stretch · Write the two-line summary for the analyst's file

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

review = pd.DataFrame(U.js("shaden_review"))
print(review.to_string(index=False))
shaden = next(a for a in U.js("analysts") if a["id"] == "A10")
print("\nskills profile (1 to 4):", shaden["skills"])

# %% [markdown]
# ## 1 · Three findings (5')
#
# Seven findings is a list; three is feedback. Choose the three that teach the most: a pattern in her reasoning, not
# the most findings of one kind. A finding about naming can wait.
#
# ✏️ **Exercise** · Return the ids of the three findings you will raise, and one strength to name.

# %%
def choose() -> dict:
    # BEGIN SOLUTION
    return {"raise": ["F2", "F1", "F7"],
            "strength": "Her charts and headings are clear: cell 7's chart is easy to read once its axis starts at zero."}
    # END SOLUTION


# %%
try:
    chosen = choose()
except NotImplementedError:
    chosen = {"raise": ["F2", "F1", "F7"], "strength": "Clear headings and charts."}
sev = dict(zip(review.id, review.severity))
print("chosen:", chosen["raise"], "severities:", [sev[i] for i in chosen["raise"]])
U.check(len(chosen["raise"]) == 3, "three findings chosen")
U.check(sum(sev[i] >= 2 for i in chosen["raise"]) == 3, "none of the three is a minor finding")

# %% [markdown]
# ## 2 · The notes (9')
#
# ✏️ **Exercise** · One note per chosen finding. **Observation**: what you saw, with the cell and the number.
# **Effect**: what it did to the answer or the decision. **Reasoning**: the question she did not ask herself.
# **Next**: one thing she does differently in her next analysis.

# %%
def my_notes() -> list[dict]:
    # BEGIN SOLUTION
    return [
        {"id": "F2", "observation": "In cell 5 waiting at T2 is compared before and after slot booking, with no other terminal as a comparison.",
         "effect": "Waiting fell at every terminal in month 13, so most of the fall you attribute to slot booking would have happened anyway.",
         "reasoning": "Before saying a change caused a difference, ask what would have happened without it, and find a group that shows that.",
         "next": "In your next comparison, write the comparison group in the first cell before you compute anything."},
        {"id": "F1", "observation": "In cell 3 the mean dwell of 5.2 days includes transshipment containers with the imports.",
         "effect": "Transshipment boxes wait for a connecting vessel, so the import figure is overstated by about half a day.",
         "reasoning": "Every average is over a population; check that the rows in it are the ones the question is about.",
         "next": "Print the counts by move type before every average, and filter in code, never by hand."},
        {"id": "F7", "observation": "Cells 3 to 6 were drafted by the assistant, and the notebook has no disclosure line and no verification record.",
         "effect": "The reviewer could not tell which numbers you had re-run, so every number had to be checked again.",
         "reasoning": "An assistant's number is a claim to test; your name on the analysis means you tested it.",
         "next": "Add the disclosure line and a table of each assisted number with your re-run value before you ask for review."},
    ]
    # END SOLUTION


# %%
try:
    notes = my_notes()
except NotImplementedError:
    notes = U.reference("feedback")["notes"]
for n in notes:
    print(n["id"], U.note_problems(n) or "specific")

# %% [markdown]
# ## 3 · A three-month plan (8')
#
# ✏️ **Exercise** · Build on her profile: her lowest skills are methods, inference and assisted-work verification (1
# of 4). Each month has a goal, an activity, the evidence that shows it was reached, and the support she gets. Keep
# unaided practice in the plan: the analysis she does without the assistant.

# %%
def my_plan() -> list[dict]:
    # BEGIN SOLUTION
    return [
        {"month": 1, "goal": "Choose a comparison group for every before-and-after question",
         "activity": "Pair review with Faleh on two comparison analyses; she writes the comparison group first in each",
         "evidence": "Two analyses whose first cell names the comparison group, passed by the reviewer on item M1",
         "support": "Faleh Al-Musharraf, one hour a week of pair review"},
        {"month": 2, "goal": "Verify every assisted number before review",
         "activity": "Keeps a verification table in each assisted analysis and re-runs every number herself",
         "evidence": "Three analyses with complete verification records and no assisted number changed by the reviewer",
         "support": "The audit checklist from Lab 2.2; a monthly check by the head of unit"},
        {"month": 3, "goal": "State uncertainty for the numbers a decision depends on",
         "activity": "One analysis done unaided, without the assistant, with an interval for its headline",
         "evidence": "An unaided analysis that passes a level 2 review with items I1 and M1 rated yes",
         "support": "A worked example from the unit's archive and a review by Saleh Al-Ghamlas"},
    ]
    # END SOLUTION


# %%
try:
    plan = my_plan()
except NotImplementedError:
    plan = U.reference("feedback")["plan"]
pp = U.plan_problems(plan)
print("plan problems:", pp or "none")

# %% [markdown]
# ## 4 · Specific, line by line (3')
#
# The peer test of the outcome: would a colleague reading this know exactly what Shaden should do next week? The
# checks flag vague words and notes without a cell or a number.

# %%
all_probs = [p for n in notes for p in U.note_problems(n)] + pp
print(all_probs or "every note and month is specific")
U.check(not all_probs, "every note and month passes the specificity check")
md = ["# Feedback for Shaden Al-Ruwayshid", "", f"**What works.** {chosen['strength']}", ""]
for n in notes:
    md += [f"## {n['id']}", f"- What I saw: {n['observation']}", f"- What it does: {n['effect']}",
           f"- The reasoning: {n['reasoning']}", f"- Next time: {n['next']}", ""]
md += ["# Three-month plan", ""] + [f"**Month {m['month']}.** {m['goal']}. {m['activity']}. Evidence: {m['evidence']}. Support: {m['support']}." for m in plan]
U.save("feedback_shaden.md", "\n".join(md) + "\n")
print(U.tutor("\n".join(md), "would Shaden know what to do differently next week?"))

# %% [markdown]
# ## ✱ Stretch · The file summary
#
# Two lines for her development file: where she is, and what the plan should show in three months.

# %%
print("Strong communicator; needs a comparison group in every causal claim and a verification record for assisted work.\n"
      "By month 3: an unaided analysis that passes level 2 review with uncertainty stated.")

# %% [markdown]
# ## Checkpoint
#
# 1. Why raise three findings and not seven?
#    <details><summary>Answer</summary>Seven findings tell her what was wrong; three, chosen for the reasoning behind
#    them, tell her what to change. The minor ones go in the review notes, not the feedback.</details>
# 2. What makes "be more careful with comparisons" useless?
#    <details><summary>Answer</summary>It names no cell, no number and no action; she cannot tell what to do
#    differently.</details>
# 3. Why is there unaided work in month 3?
#    <details><summary>Answer</summary>Her verification skill is 1 of 4: she cannot check the assistant until she can
#    do the work herself.</details>
#
# **Carry forward.** `out/feedback_shaden.md`. Lab 2.4 starts from `data/pipeline_q1.json` and `data/analysts.json`.
