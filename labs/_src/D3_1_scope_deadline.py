# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 3.1 · A result in a week
#
# Day 3 · Session 1 (Scope and deadline) · 25 min.
#
# Bader Al-Khayyal, director of marine operations, wants the slot-booking evaluation for the board in a week. The
# unit has one analyst free. Five questions could be asked of the berth data; each takes analyst days plus the review
# its assurance level requires. You size them, run the meeting, keep the agreement when his constraints change halfway
# through, and record it. An observer scores the meeting.
#
# **Role-play.** In class the trainer, or a peer with the role card, plays Bader, and a third participant observes with
# the rubric. Working alone, use the scripted stand-in `U.sponsor("bader", message)`: it changes a constraint on the
# fourth message, as the real one will.
#
# **AI policy: AI-off during the meeting.** The tutor may question your record afterwards.
#
# **Reference state.** `data/inventory.json`, `data/roles.json`.
#
# **Tasks**
# - [ ] 1 · Size the questions against the deadline (5')
# - [ ] 2 · Open the meeting and ask (6')
# - [ ] 3 · Respond when the constraints change (6')
# - [ ] 4 · Record the scope agreement (5')
# - [ ] 5 · The observer's score (3')
# - [ ] ✱ Stretch · Play the sponsor for a peer, with the role card

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

inv = U.js("inventory")
q = pd.DataFrame(inv["questions"])
q["review_days"] = q.level.map({int(k): v for k, v in inv["review_days"].items()})
q["total_days"] = q.analyst_days + q.review_days
print(q.to_string(index=False))
print(f"\nworking days to the deadline: {inv['working_days']}; analysts free: {inv['analysts_available']}")

# %% [markdown]
# ## 1 · What fits (5')
#
# ✏️ **Exercise** · Choose the questions that fit in five working days, review included, and that serve the board's
# decision best. Then prepare at least two options to offer Bader, each a set of questions with what it leaves out.

# %%
def size_options() -> dict:
    # BEGIN SOLUTION
    return {
        "A": {"questions": ["Q-a", "Q-c"], "leaves_out": "vessel types, forecast and cost to the lines"},
        "B": {"questions": ["Q-a", "Q-b"], "leaves_out": "diversions, forecast and cost to the lines"},
        "C": {"questions": ["Q-a", "Q-b", "Q-c", "Q-e"], "leaves_out": "the forecast; needs ten and a half working days, so a later board"},
    }
    # END SOLUTION


# %%
try:
    options = size_options()
except NotImplementedError:
    options = U.reference("scope")["options"]
for k, o in options.items():
    print(f"option {k}: {o['questions']} -> {U.days_needed(o['questions'])} days; leaves out {o['leaves_out']}")
U.check(sum(U.days_needed(o["questions"]) <= inv["working_days"] for o in options.values()) >= 2, "at least two options fit the deadline")

# %% [markdown]
# ## 2 and 3 · The meeting (6' + 6')
#
# ✏️ **Exercise** · Write your messages in order. Ask before you offer: the decision, the deadline, the evidence he
# would accept, what exists already. Then offer the options. On the fourth message his constraints change: read the
# change and answer it with your options, not with a new promise.

# %%
U.reset_role("bader")


def my_messages() -> list[str]:
    # BEGIN SOLUTION
    return [
        "Which decision will the board take with this, and what will you recommend to them?",
        "When exactly do the board papers close, and is there any time after that for a correction?",
        "What evidence would convince you, and what would make the shipping lines object?",
        "What exists already: is there a draft or an earlier report on slot booking?",
        "Given four working days, option B fits: the effect at T2 against the other terminals, and the same by vessel type with feeders separate. Diversions and the cost to the lines would follow for the next board.",
    ]
    # END SOLUTION


# %%
try:
    messages = my_messages()
except NotImplementedError:
    messages = U.reference("scope")["messages"]
transcript = []
for m in messages:
    a = U.sponsor("bader", m)
    transcript.append((m, a))
    print("You:", m, "\n ", a, "\n")
cov = U.role_coverage("bader")
print(f"constraints heard: {cov[0]} of {cov[1]}; missed: {cov[2] or 'none'}")

# %% [markdown]
# ## 4 · The scope agreement (5')
#
# ✏️ **Exercise** · Record what was agreed after the change: the questions in scope, those out of scope and when
# they come, the working days, the options you offered, and what you said when the constraints changed.

# %%
def my_record() -> dict:
    # BEGIN SOLUTION
    return {
        "decision": "Whether to extend slot booking to all four terminals next quarter",
        "in_scope": ["Q-a", "Q-b"],
        "out_of_scope": ["Q-c diversions and Q-e cost to the lines: for the following board", "Q-d forecast: not before a decision to extend"],
        "working_days": 4,
        "options_offered": ["A: effect and diversions", "B: effect and vessel types, feeders separate", "C: four questions, a later board"],
        "after_change": "With four days, option B: it answers the feeder question the deputy chief executive added, and diversions move to the next board.",
        "evidence": "Mean waiting at T2 against the other terminals, by vessel type; the lines' view through the feeder table",
    }
    # END SOLUTION


# %%
try:
    record = my_record()
except NotImplementedError:
    record = U.reference("scope")["record"]
print(f"in scope: {record['in_scope']} -> {U.days_needed(record['in_scope'])} days of {record['working_days']}")
U.check(U.days_needed(record["in_scope"]) <= record["working_days"], "the agreed scope fits the new deadline")
U.check(bool(record["out_of_scope"]), "what is out of scope is written down")

# %% [markdown]
# ## 5 · The observer's score (3')
#
# The observer scores five criteria 0 to 2. The rule-based score below is a stand-in for a person with the rubric.

# %%
score = U.observer_score(record, cov)
print(score)
U.check(score["total"] >= 8, "an observer's score of at least 8 of 10")
md = ["# Scope agreement: slot-booking evaluation", "", f"**Decision.** {record['decision']}",
      f"**In scope.** {', '.join(record['in_scope'])} ({U.days_needed(record['in_scope'])} of {record['working_days']} working days)",
      "**Out of scope.**"] + [f"- {x}" for x in record["out_of_scope"]] + [
      f"**After the change.** {record['after_change']}", f"**Observer.** {score['total']} of 10", "", "**Transcript**"]
md += [f"- You: {m}\n  {a}" for m, a in transcript]
U.save("scope_agreement.md", "\n".join(md) + "\n")
print(U.tutor("\n".join(md[:8]), "is the agreement clear about what will not be answered?"))

# %% [markdown]
# ## ✱ Stretch · Play the sponsor
#
# Swap roles with a peer: read the role card in `data/roles.json` and change the constraint on their fourth message.

# %%
print(U.js("roles")["bader"]["change"])

# %% [markdown]
# ## Checkpoint
#
# 1. Why ask four questions before offering anything?
#    <details><summary>Answer</summary>The deadline, the evidence he would accept and the existing draft change which
#    option is best; an offer made before them answers the wrong request.</details>
# 2. The deadline moved from five days to four. Why answer with an option and not by working the weekend?
#    <details><summary>Answer</summary>The review time is part of the assurance level; promising the same scope in
#    less time silently cuts the review.</details>
# 3. Why write down what is out of scope?
#    <details><summary>Answer</summary>So nobody reads the board paper as having answered it, and so the next board
#    knows what is still owed.</details>
#
# **Carry forward.** `out/scope_agreement.md`. Lab 3.2 starts from `data/berth_calls.csv`.
