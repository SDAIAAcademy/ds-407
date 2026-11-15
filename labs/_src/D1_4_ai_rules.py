# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 1.4 · Rules for assisted work
#
# Day 1 · Session 4 (Rules for AI-assisted analysis) · 25 min.
#
# More and more of the unit's work starts as a draft by Musawwada, the drafting assistant. The national Generative AI
# Guidelines for Government set duties for every user; your unit needs them as rules an analyst can follow and a
# reviewer can check: what is **verified**, what is **disclosed**, what process evidence is **kept**, what **data**
# may go to an assistant. You write them on one page and test them on eight scenarios from the unit.
#
# **AI policy: AI-tutor.** A tutor may question your rules; it does not write them.
#
# **Reference state.** `data/guidelines_digest.json` (our paraphrase of the passages used, with their sections) and
# `data/scenarios.json`.
#
# **Tasks**
# - [ ] 1 · Read the guideline duties (5')
# - [ ] 2 · Write the verify, disclose and keep rules (9')
# - [ ] 3 · Decide eight scenarios with your rules (7')
# - [ ] 4 · Cut the rules to one page (4')
# - [ ] ✱ Stretch · Add the unaided-practice rule: work each analyst still does without the assistant

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
# ## 1 · The guideline duties (5')
#
# Read the seven duties. Each is a duty of a **user**; a rule of the unit says who does what, when, and what record
# shows it was done. Read the official text for the full wording (see the course sources).

# %%
for g in U.js("guidelines_digest"):
    print(f"{g['id']} [{g['section']}] {g['duty']}")

# %% [markdown]
# ## 2 · Verify, disclose, keep, data (9')
#
# ✏️ **Exercise** · Write the rules. Each has an id and one sentence an analyst can follow and a reviewer can check.
# Name the record that shows it was done. Avoid words a reviewer cannot check ("be careful", "where possible").

# %%
def my_rules() -> dict:
    # BEGIN SOLUTION
    return {
        "verify": [
            {"id": "V1", "rule": "Re-run every number an assistant produced from the data, in your own code, before it enters a draft."},
            {"id": "V2", "rule": "Read and run any code an assistant wrote before its output is used; keep the run."},
            {"id": "V3", "rule": "Check every claim about a method or a source against the source itself."},
        ],
        "disclose": [
            {"id": "D1", "rule": "Every deliverable with assisted content carries a disclosure line: which tool, which parts, who verified them."},
            {"id": "D2", "rule": "Tell the reviewer which parts were assisted before the review starts."},
        ],
        "keep": [
            {"id": "K1", "rule": "Keep the prompts and the assistant's outputs with the analysis, in the repository."},
            {"id": "K2", "rule": "Keep a verification record: each assisted number, its re-run value and who re-ran it."},
        ],
        "data": [
            {"id": "C1", "rule": "Only data classified public, or anonymised under the data protection officer's rule, may be sent to a hosted assistant."},
            {"id": "C2", "rule": "Use only assistants on the authority's approved list."},
        ],
    }
    # END SOLUTION


# %%
try:
    rules = my_rules()
except NotImplementedError:
    rules = {k: v for k, v in U.reference("rules").items() if k != "unaided"}
for part, rs in rules.items():
    for r in rs:
        print(f"{r['id']:3} [{part}] {r['rule']}")
probs = U.rules_problems(rules)
print("problems:", probs or "none")
U.check(not probs, "the rules pass the problems check")

# %% [markdown]
# ## 3 · Eight scenarios (7')
#
# ✏️ **Exercise** · Decide each scenario with your rules: `allowed`, `needs action` (allowed once something is done)
# or `breach`, and the ids of the rules that decide it. A scenario your rules cannot decide shows a gap: add a rule.

# %%
scen = U.js("scenarios")
for s in scen:
    print(f"{s['id']}: {s['text']}")


def my_decisions() -> dict:
    # BEGIN SOLUTION
    return {
        "S1": {"decision": "allowed", "rules": []},
        "S2": {"decision": "breach", "rules": ["C1"]},
        "S3": {"decision": "breach", "rules": ["D1"]},
        "S4": {"decision": "needs action", "rules": ["K1", "K2"]},
        "S5": {"decision": "breach", "rules": ["V1"]},
        "S6": {"decision": "allowed", "rules": []},
        "S7": {"decision": "needs action", "rules": ["U1"]},
        "S8": {"decision": "breach", "rules": ["C2"]},
    }
    # END SOLUTION


# %%
try:
    decisions = my_decisions()
except NotImplementedError:
    decisions = U.reference("scenarios")
right, wrong = U.score_scenarios(decisions)
print(f"same decision as the reference on {right} of 8; differ on {wrong}")
cited = {r for d in decisions.values() for r in d["rules"]}
defined = {r["id"] for rs in rules.values() for r in rs}
print("rules cited but not written yet:", sorted(cited - defined) or "none")
U.check(right >= 7, "at least seven of eight scenarios decided as the reference")

# %% [markdown]
# ## 4 · One page (4')
#
# The rules are read before a deadline, not after. At most 350 words. Then the stretch: S7 needs a rule your set may
# not have yet.

# %%
md = ["# Rules for AI-assisted analysis, Ras Sahil analytics unit (draft)", ""]
for part, rs in rules.items():
    md += [f"**{part.capitalize()}**"] + [f"- {r['id']}. {r['rule']}" for r in rs] + [""]
md += ["Based on the SDAIA Generative AI Guidelines for Government (duties G1 to G7 of the digest)."]
page = "\n".join(md)
print(f"{U.words(page)} words")
U.check(U.words(page) <= 350, "the rules fit on one page")
U.save("ai_rules.md", page + "\n")
print(U.tutor(page, "could a reviewer check each rule from the files of an analysis?"))

# %% [markdown]
# ## ✱ Stretch · Unaided practice
#
# An analyst who never works without the assistant cannot tell when it is wrong. Add a rule that keeps unaided work in
# the job, and check S7 again.

# %%
rules["unaided"] = [{"id": "U1", "rule": "Each analyst does one analysis a quarter without an assistant, reviewed like any other."}]
print(U.rules_problems(rules) or "still passes", "| S7 now decided by U1")

# %% [markdown]
# ## Checkpoint
#
# 1. Why is S2 a breach even though the assistant is approved?
#    <details><summary>Answer</summary>The roster holds names and shifts: restricted data. The guideline limits
#    generative AI tools to public data, whichever tool it is.</details>
# 2. S5's analyst plans to check the 18% after the review. What is wrong with that?
#    <details><summary>Answer</summary>The reviewer then reviews an unverified number as if it were the analyst's.
#    Verification comes before the draft, and the record shows it.</details>
# 3. Why keep the prompts?
#    <details><summary>Answer</summary>They are the process evidence: a reviewer or an auditor can see what was asked,
#    what came back and what the analyst changed.</details>
#
# **Carry forward.** `out/ai_rules.md`. Lab 2.2 starts from `data/rules_reference.json`.
