# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 2.4 · A quarter's review rota
#
# Day 2 · Session 4 (Review capacity and mentoring) · 25 min.
#
# Next quarter the unit plans 40 analyses, each with its assurance level. Reviews take hours, and the levels say who
# may do them: level 3 and 4 need a senior reviewer, and level 4 a second reviewer too. You turn levels into hours,
# assign reviewers under the rules, find where the senior hours run out, choose how to close the gap, and pair the
# three junior analysts with mentors.
#
# **AI policy: AI-tutor.** A tutor may question your plan; the assignment is yours.
#
# **Reference state.** `data/pipeline_q1.json`, `data/analysts.json`.
#
# **Tasks**
# - [ ] 1 · Review hours by level for the quarter (5')
# - [ ] 2 · Assign reviewers under the rules (9')
# - [ ] 3 · Find the overload and the shortfall (6')
# - [ ] 4 · Pair the juniors with mentors (5')
# - [ ] ✱ Stretch · Choose which mid-level analyst trains as a level 3 reviewer, and how

# %%
import os, sys, subprocess, math
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

pipe = pd.DataFrame(U.js("pipeline_q1"))
team = pd.DataFrame(U.js("analysts"))[["id", "name", "seniority", "review_hours"]]
print(team.to_string(index=False))
print("\nanalyses by level:", pipe.level.value_counts().sort_index().to_dict())

# %% [markdown]
# ## 1 · Hours by level (5')
#
# The unit's planning figures: a level 2 review takes 4 hours, level 3 takes 10, level 4 takes 16 for the first
# reviewer and 8 for the second. Level 1 is the analyst's own check. A co-signed level 3 review (a mid-level reviewer,
# a senior who checks the review) costs the senior 2 hours.
#
# ✏️ **Exercise** · Compute the hours that only seniors can give (levels 3 and 4, first reviewer) and compare with
# the seniors' review hours.

# %%
hrs = U.review_hours()


def senior_demand(pipe: pd.DataFrame) -> int:
    # BEGIN SOLUTION
    return int(sum(hrs[l] for l in pipe.level if l >= 3))
    # END SOLUTION


# %%
try:
    demand = senior_demand(pipe)
except NotImplementedError:
    demand = 184
supply = int(team[team.seniority == "senior"].review_hours.sum())
print(f"senior hours needed {demand}, available {supply}, short by {demand - supply}")
U.check(demand == 184, "senior demand computed from the levels")

# %% [markdown]
# ## 2 and 3 · Assign, find the overload, close the gap (9' + 6')
#
# ✏️ **Exercise** · Return `assign` (analysis id to reviewer id; `"A04+A01"` for a level 3 review by a mid-level
# analyst co-signed by a senior) and `second` (level 4 analysis id to second reviewer). Rules: nobody reviews their own
# work; juniors do not review alone; level 3 and 4 need a senior, or a co-signed review for level 3; nobody goes over
# their hours. Close the shortfall with the fewest co-signed reviews.

# %%
def plan_rota(pipe: pd.DataFrame, team: pd.DataFrame) -> tuple[dict, dict]:
    # BEGIN SOLUTION
    # By hand: level 4 and 3 first to the seniors, never to the author; five level 3 reviews co-signed (the fewest
    # that close a 34-hour gap at 8 hours saved each); level 2 and the second reviews spread over the mid-level team.
    assign = {"P01": "A04", "P02": "A04+A01", "P03": "A05", "P04": "A06", "P05": "A09", "P06": "A01", "P08": "A02", "P09": "A01", "P10": "A04", "P12": "A06",
              "P14": "A05+A02", "P15": "A04+A02", "P17": "A05+A03", "P18": "A06+A03", "P21": "A05", "P22": "A09", "P23": "A02", "P24": "A07",
              "P26": "A08", "P27": "A02", "P28": "A05", "P29": "A03", "P30": "A03", "P31": "A06", "P32": "A04", "P33": "A09", "P34": "A01",
              "P38": "A03", "P39": "A01", "P40": "A02"}
    second = {"P09": "A07", "P34": "A08", "P39": "A07", "P40": "A08"}
    return assign, second
    # END SOLUTION


# %%
try:
    assign, second = plan_rota(pipe, team)
except NotImplementedError:
    ref = U.reference("rota")
    assign, second = ref["assign"], ref["second"]
viol = U.rota_violations(assign, second)
print("violations:", viol or "none")
load = U.loads(assign, second)
team["assigned"] = team.id.map(load).fillna(0).astype(int)
team["use"] = (100 * team.assigned / team.review_hours).round().astype(int).astype(str) + "%"
print(team.to_string(index=False))
cos = [k for k, v in assign.items() if "+" in v]
print(f"co-signed level 3 reviews: {len(cos)} {cos}")
U.check(not viol, "the rota keeps every rule and nobody is over their hours")

# %% [markdown]
# ## 4 · Mentors for the juniors (5')
#
# ✏️ **Exercise** · Pair each junior (Shaden, Turki, Dalia) with a mentor who is not a junior, one junior per mentor.
# The junior shadows the mentor's reviews: no hours are booked, but the mentor's load matters. Prefer a mentor who
# reviews at least one of the junior's analyses this quarter.

# %%
def mentors(assign: dict) -> dict:
    # BEGIN SOLUTION
    return {"A10": "A01", "A11": "A04", "A12": "A05"}
    # END SOLUTION


# %%
try:
    pairs = mentors(assign)
except NotImplementedError:
    pairs = U.reference("rota")["mentors"]
sen_of = dict(zip(team.id, team.seniority))
names = dict(zip(team.id, team.name))
for j, m in pairs.items():
    theirs = [p for p, r in assign.items() if pipe.set_index("id").author[p] == j and m in r.split("+")]
    print(f"{names[j]} with {names[m]} ({sen_of[m]}); reviews of the junior's own work by the mentor: {theirs or 'none'}")
U.check(len(set(pairs.values())) == 3 and all(sen_of[m] != "junior" for m in pairs.values()), "three juniors, three different mentors")
U.save("rota_q1.md", "# Review rota, next quarter\n\n" + team.to_string(index=False) +
       f"\n\nCo-signed level 3 reviews: {', '.join(cos)}\n\nMentors: " +
       "; ".join(f"{names[j]} with {names[m]}" for j, m in pairs.items()) + "\n")

# %% [markdown]
# ## ✱ Stretch · A new level 3 reviewer
#
# Co-signing is a bridge. Which mid-level analyst should train to review level 3 alone, and what evidence would show
# she is ready? Look at the skills profiles.

# %%
prof = pd.DataFrame([{"id": a["id"], "name": a["name"], **a["skills"]} for a in U.js("analysts") if a["seniority"] == "mid"])
prof["mean"] = prof.drop(columns=["id", "name"]).mean(axis=1).round(2)
print(prof.sort_values("mean", ascending=False).to_string(index=False))

# %% [markdown]
# ## Checkpoint
#
# 1. Why does the shortfall sit with the seniors when the unit has spare hours overall?
#    <details><summary>Answer</summary>Level 3 and 4 reviews need seniors: 184 hours of their 150. The mid-level
#    analysts have hours, but the rule says they may not use them on those reviews alone.</details>
# 2. Why co-sign rather than lower the level of five analyses?
#    <details><summary>Answer</summary>The level comes from the risk, not from the hours available. Lowering it to fit
#    the rota is the under-assurance that caused last year's errors.</details>
# 3. What does a co-signed review buy besides hours?
#    <details><summary>Answer</summary>It trains the next level 3 reviewers, the only lasting cure for the
#    shortfall.</details>
#
# **Carry forward.** `out/rota_q1.md`. Day 3 starts from `data/inventory.json` and `data/roles.json`.
