# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 3.3 · Drop the feeder result?
#
# Day 3 · Session 3 (Pressure on a finding) · 25 min.
#
# The slot-booking evaluation is written. Overall, waiting at T2 fell a little against the other terminals; for feeder
# vessels, the small local lines, it rose by several hours. Khaled Al-Kharji, deputy chief executive for commercial
# affairs, asks you to take the feeder table out of the board paper. You check the finding, weigh the options, decide,
# and record the decision with its reasons, citing the unit's standard and the AI Ethics Principles. Then you reply.
#
# **AI policy: AI-tutor.** A tutor may question your record; the decision is yours.
#
# **Reference state.** `data/khaled_request.md`, `data/berth_calls.csv`, `data/unit_standard.md`.
#
# **Tasks**
# - [ ] 1 · Read the request and recompute the subgroup (6')
# - [ ] 2 · Weigh the options (5')
# - [ ] 3 · Decide and write the decision record (8')
# - [ ] 4 · Draft the reply (6')
# - [ ] ✱ Stretch · Write the escalation note for a repeated request

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

print(U.text("khaled_request.md"))

# %% [markdown]
# ## 1 · Is the finding sound? (6')
#
# A request to remove a result may hide a fair point: maybe the subgroup is too small, or the effect is noise. Check
# before you decide. Recompute the effect by vessel type and the count of feeder calls at T2.
#
# ✏️ **Exercise** · Return the effect for feeders, for the other types together, and the share of T2 calls that are
# feeders.

# %%
calls = U.csv("berth_calls")


def check_finding(calls: pd.DataFrame) -> dict:
    # BEGIN SOLUTION
    t2 = calls[calls.terminal == "T2"]
    return {"feeder_h": U.subgroup_did("feeder"), "others_h": U.subgroup_did(exclude="feeder"), "all_h": U.subgroup_did(),
            "feeder_share_t2": round(100 * float((t2.vessel_type == "feeder").mean()), 1),
            "feeder_calls_t2_after": int(((t2.vessel_type == "feeder") & (t2.month >= 13)).sum()),
            "feeder_diverted_t2_after": int(t2[(t2.vessel_type == "feeder") & (t2.month >= 13)].diverted.sum())}
    # END SOLUTION


# %%
try:
    f = check_finding(calls)
except NotImplementedError:
    f = U.reference("pressure")["finding"]
print(f)
U.check(f["feeder_h"] > 2 and f["feeder_calls_t2_after"] > 200, "the feeder result is large and rests on hundreds of calls")

# %% [markdown]
# ## 2 · The options (5')
#
# ✏️ **Exercise** · List at least three options, each with what it does to the board's decision and to the people
# affected. One of them is what Khaled asked for.

# %%
def options() -> list[dict]:
    # BEGIN SOLUTION
    return [
        {"option": "Remove the feeder table", "effect": "The board sees a small overall gain and may extend a scheme that adds hours of waiting for the local lines; the decision rule signed in the agreement is not applied."},
        {"option": "Keep the table as it is", "effect": "The board sees the rule's second condition fail; the commercial team may feel ambushed."},
        {"option": "Keep the table, add context and the commercial team's plan", "effect": "The finding stays; the feeder share of calls and revenue is stated, and Khaled's team can propose the fix for the feeder slots in the same paper."},
    ]
    # END SOLUTION


# %%
try:
    opts = options()
except NotImplementedError:
    opts = U.reference("pressure")["options"]
for o in opts:
    print("-", o["option"], ":", o["effect"])

# %% [markdown]
# ## 3 · The decision record (8')
#
# ✏️ **Exercise** · Record the decision so someone who was not there can see why. Cite the clauses of the unit's
# standard you rely on (`data/unit_standard.md`, by number and what each says) and the principles of the SDAIA AI
# Ethics Principles, by the names SDAIA uses (`U.PRINCIPLES`).

# %%
print(U.text("unit_standard.md"))
print(U.PRINCIPLES)


def my_record() -> dict:
    # BEGIN SOLUTION
    return {
        "request": "Khaled Al-Kharji asked by email to remove the feeder table from the slot-booking board paper",
        "finding_checked": f"Feeders wait {f['feeder_h']} hours longer at T2 against the other terminals; other types {f['others_h']} hours; {f['feeder_calls_t2_after']} feeder calls at T2 after the change, {f['feeder_diverted_t2_after']} diverted",
        "options": [o["option"] for o in opts],
        "decision": "Keep the feeder table, with context and the commercial team's proposal for the feeder slots",
        "reasons": [
            "The agreement signed before the analysis makes 'no vessel type worse by more than 2 hours' part of the decision rule; removing the table removes the condition the board agreed to apply.",
            "The result is large and rests on hundreds of calls; it is not noise.",
            "The people who bear the cost, the local feeder lines, are the ones the paper would leave out.",
        ],
        "standard_clauses": ["S-7: findings are not removed from a paper after review; a disagreement is recorded beside the finding",
                             "S-8: pressure to change a finding is recorded and, if repeated, escalated to the chief executive's office"],
        "principles": ["Fairness", "Transparency & Explainability", "Accountability & Responsibility"],
        "who_told": "Khaled Al-Kharji (reply), Bader Al-Khayyal (sponsor), recorded in the unit's decision log",
        "date_recorded": "the day of the request",
    }
    # END SOLUTION


# %%
try:
    rec = my_record()
except NotImplementedError:
    rec = U.reference("pressure")["record"]
probs = U.record_problems(rec)
print("problems:", probs or "none")
U.check(not probs, "the decision record is complete")
U.check("remove" not in rec["decision"].lower() or "keep" in rec["decision"].lower(), "the decision keeps the finding")

# %% [markdown]
# ## 4 · The reply (6')
#
# ✏️ **Exercise** · Reply to Khaled: keep the relationship and the finding. Acknowledge his concern, say what you will
# do and why, offer what he can add. At most 150 words.

# %%
def my_reply() -> str:
    # BEGIN SOLUTION
    return ("Thank you, Khaled. I understand the concern that the feeder table could distract the board. I will keep it: "
            "the agreement signed before the analysis makes the effect on each vessel type part of the decision rule, "
            f"and feeders wait {f['feeder_h']} hours longer at T2, on {f['feeder_calls_t2_after']} calls. Removing it would "
            "leave the board deciding without the condition it agreed to apply. I will add the feeder share of calls and "
            "revenue, so the size is clear, and I would welcome a short proposal from your team on the feeder slots to sit "
            "beside the table. The final paper will be with you by the end of tomorrow.")
    # END SOLUTION


# %%
try:
    reply = my_reply()
except NotImplementedError:
    reply = U.reference("pressure")["reply"]
print(reply, f"\n\n({U.words(reply)} words)")
U.check(U.words(reply) <= 150, "the reply is at most 150 words")
md = ["# Decision record: request to remove the feeder table", ""] + [f"**{k.replace('_', ' ').capitalize()}.** {v if not isinstance(v, list) else '; '.join(v)}" for k, v in rec.items()]
md += ["", "**Reply sent**", reply]
U.save("decision_record.md", "\n".join(md) + "\n")
print(U.tutor("\n".join(md), "would someone who was not there understand why?"))

# %% [markdown]
# ## ✱ Stretch · If the request comes again
#
# Khaled writes again, more firmly, copying the chief executive. Write the escalation note: to whom, what is attached,
# and what you ask them to decide.

# %%
print("To the chief executive's office: the request, the decision record, the signed agreement and the paper. "
      "Asked: to confirm the paper goes with the feeder table and the commercial team's proposal beside it.")

# %% [markdown]
# ## Checkpoint
#
# 1. Why recompute the subgroup before deciding?
#    <details><summary>Answer</summary>A request to drop a result can carry a fair point (a tiny group, noise). Checked,
#    the feeder effect is large and rests on hundreds of calls, so the request is pressure, not a correction.</details>
# 2. What makes the agreement from Lab 3.2 decisive here?
#    <details><summary>Answer</summary>The rule signed before the analysis already includes the vessel-type condition;
#    removing the table would change the rule after the result was seen.</details>
# 3. Why offer Khaled's team a place in the paper?
#    <details><summary>Answer</summary>It keeps the finding and gives the sponsor a constructive role: the fix for the
#    feeder slots, not the removal of the evidence.</details>
#
# **Carry forward.** `out/decision_record.md`. Lab 3.4 starts from `data/containers_q2_released.csv`.
