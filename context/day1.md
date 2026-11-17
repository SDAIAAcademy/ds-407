---
course: "Leading Analytical Work: Review, Standards and Stakeholders"
code: "DS-407"
version: "2027.1.0"
deck: "day1"
day: 1
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/ds-407/slides/day1.html"
---

# Leading Analytical Work: Review, Standards and Stakeholders

## Day 1: Set the standard

An assurance standard, a team checklist, re-runs as a rule and rules for assisted work

#### [day1#title] Set the standard

*SDAIA Academy · Leading Analytical Work: Review, Standards and Stakeholders*

Day 1: An assurance standard, a team checklist, re-runs as a rule and rules for assisted work

Data Science Track · 3 teaching days + capstone day · 4 sessions · 4 labs · DS-407

#### [day1#agenda] Set the standard

*Today*

- **Session 1 · Assurance proportionate to risk**: Four roles, business risk as effect and likelihood, and four assurance levels a peer can apply
- **Session 2 · A team review checklist**: From a personal checklist to the unit's: adapt a published one, item by item, and tie each item to a level
- **Session 3 · Reproducibility as a team rule**: Re-run before reading: the failures a re-run finds and the repository rules that prevent them
- **Session 4 · Rules for AI-assisted analysis**: What an analyst verifies, discloses and keeps when an assistant drafts the work

#### [day1#the-unit] Twelve analysts, four sponsors, and no shared rule for checking

*The case*

- **Ras Sahil Ports Authority**: four terminals, marine pilots and tugs, a board that decides tariffs and capital
- The analytics unit serves marine operations, commercial affairs, finance and staffing
- Three senior analysts, six mid-level, three juniors
- More and more drafts start with **Musawwada**, the unit's drafting assistant

- **You are Arjwan Al-Huqail.** Head of the unit. Your job is no longer to review one analysis well: it is to make every analysis reviewed well enough, by someone, on time.

### Session 1: Assurance proportionate to risk

#### [day1#s1] Assurance proportionate to risk

*Session 1*

- Explain the four assurance roles and why the assurer is independent of the analyst
- Grade a request by the effect of an error and the complexity of the work
- Assign an assurance level with a matrix a peer applies the same way

#### [day1#log-shows] The errors readers found came from work checked too little for its use

*Last year's log*

- **5 of 10** under-assured requests had an error found after release
- **1 of 20** of the others did

- "Under-assured": a lower level than the standard you write in Lab 1.1 requires
- A board paper on a fee change got a self-check; so did a public dwell statistic
- Two crane-downtime requests, alike in every way, got level 1 and level 3

#### [day1#four-roles] Four roles, and the assurer is never the analyst

*Who does what*

- **Commissioner.** Asks for the analysis and owns the decision it serves
- **Analyst.** Does the work and checks it first
- **Assurer.** Checks it independently, to the level required
- **Approver.** Signs off that it is fit for its use

> **From the AQuA Book.** The UK government's guide to quality analysis (2025 edition) names these four roles and requires the assurer to be independent of the analyst; the degree of separation grows with the importance of the output.

#### [day1#risk-two-axes] Assurance grows with the effect of an error and the complexity of the work

*Proportionate*

| effect \ complexity | low | medium |
| --- | --- | --- |
| high | high | 3 |
| 3 | 4 | medium |
| 2 | 2 | 3 |
| low | 1 | 1 |
| 2 |  |  |

The reference matrix of Lab 1.1. Business risk is the effect of an error and its likelihood; complexity raises the likelihood.

#### [day1#four-levels] Each level names who checks, who re-runs and who signs

*The levels*

| Level | Assurer | Re-run | Approver |
| --- | --- | --- | --- |
| **1** Self-check | The analyst, with the checklist | By the analyst | The requester's manager |
| **2** Peer review | Another analyst of the unit | By the reviewer | A senior analyst |
| **3** Independent review | A senior analyst who took no part | By the reviewer, from the repository | The head of the unit |
| **4** Second opinion | A senior analyst and a second reviewer | By both | Head of unit and requesting director |

#### [day1#escalators] Two uses add a level, whatever the matrix says

*Escalators*

- **Public release.** The figure leaves the authority: a bulletin, a ministry indicator, a regulator's return. A published error cannot be quietly corrected.
- **Safety use.** The result sets safety staffing (pilots on duty), a navigation limit or a safety rule. The effect of an error falls on people, not on a budget.

> **Personal data** does not raise the level. It adds a check by the data protection officer before the output leaves the unit.

#### [day1#definitions-matter] A peer applies your words, not your intentions

*The test of a standard*

1. **1 · You grade** effect, complexity, public, safety for six new requests
2. **2 · A peer grades** the same six, alone, with your definitions
3. **3 · Compare levels** every difference points at a definition

> **What goes wrong.** "Medium effect: a moderate impact." Two readers, two levels. Write what an error would change: "an operational decision for a month or more".

#### [day1#six-requests] Six requests the unit received this month

*The six new requests*

| Id | Request | Use |
| --- | --- | --- |
| N1 | Weekly berth occupancy for the terminal planning meeting | Planning decision |
| N2 | Revenue estimate of a proposed tariff change | Board paper |
| N3 | Arrival-delay model to allocate marine pilots at night | Safety staffing |
| N4 | Average cargo dwell for the annual public statistics | Public statistic |
| N5 | Staff survey summary for human resources | Internal note, personal data |
| N6 | Evaluation of the berth-allocation pilot: continue or stop | Board decision |

#### [day1#check-public-statistic] A simple count for a public statistic: which level?

*Checkpoint*

**Question:** N4: mean import dwell by quarter, one source, a method the unit runs every month. It goes into the authority's published annual statistics. With the matrix and escalators on the earlier slides, what level?

- A. Level 1: the method is simple
- B. Level 2: medium effect, low complexity
- C. Level 3: level 2 from the matrix, plus one for public release
- D. Level 4: anything public gets the highest level

#### [day1#lab-1-1] Six requests, four levels

Lab 1.1 · 25 min

Read the unit's log of 30 requests, write the assurance matrix with its escalators, grade six new requests by risk and complexity, and compare your levels with a second reviewer's.

[D1_1_assurance_levels.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D1_1_assurance_levels.ipynb)

- [ ] Read the log: where errors after release came from (5 min)
- [ ] Write the matrix and its escalators (7 min)
- [ ] Grade the six new requests (7 min)
- [ ] Compare with the second reviewer and tighten one definition (6 min)
- [ ] ✱ Stretch: Add the sign-off rules: who may approve at each level

### Session 2: A team review checklist

#### [day1#s2] A team review checklist

*Session 2*

- Adapt a published checklist to the unit's work instead of adopting it whole
- Write each item as a question answered with evidence
- Tie each item to the assurance levels, with a privacy and classification check in every level

#### [day1#personal-to-team] Your personal checklist becomes the unit's, tied to the levels

*From DS-310*

- **In DS-310.** Five areas, question fit to communication, scored 0 to 2 by one reviewer on one analysis.
- **Here.** The same five areas as yes-or-no items with named evidence, each required from a level, used by twelve people the same way.

> **Recap only.** How to score one analysis is DS-310's; this session decides what the whole unit checks, and when.

#### [day1#adapt-not-adopt] REFORMS: 32 items in 8 modules, written for others' work

*Start from a published checklist*

- Reporting standards for machine-learning-based science, by a consensus of 19 researchers
- Modules from study goals and reproducibility to leakage and generalisability
- Its authors say not every item fits every study: decide which are relevant

- **Adapt, do not adopt.** Most of the unit's work is counts and comparisons. A checklist of 32 machine-learning items gets skipped on every dashboard request.

#### [day1#modules-to-areas] No REFORMS module covers communication: the unit writes those items

*Mapping*

| Item | Value |
| --- | --- |
| Data | 15 items |
| Method | 9 |
| Inference | 5 |
| Question fit | 3 |
| Communication | 0 |

The 32 REFORMS items by the review area of their module (Lab 1.2, task 1).

#### [day1#item-shape] An item is a yes-or-no question with the evidence that answers it

*One item*

| Weak | Usable |
| --- | --- |
| Is the work reproducible? | Does it re-run from the repository, with the lock file and README alone, to the reported numbers? **Evidence:** the re-run log |
| Are the data good? | Are excluded and missing records counted, with the reason for each exclusion? **Evidence:** a count per step |
| Is the comparison valid? | Is the comparison fair: a baseline, a control group, the same period? **Evidence:** the comparison cell |

#### [day1#levels-per-item] Six items at level 1, eleven from level 2

*Proportionate again*

- **Level 1**: question, sources, exclusions, fair comparison, numbers match, privacy
- **Level 2** adds: decision rule first, duplicates, re-run, uncertainty, where it does not hold
- **Level 3** adds the model item, when there is a model

**12** items in the Lab 1.2 checklist, drawing on 18 of the 32 REFORMS items

#### [day1#privacy-item] Nothing leaves the unit before the privacy and classification check

*Every level*

- **The item.** Before anything leaves the unit: is it free of personal data, and is its classification marked and respected?

- Required from **level 1**: a dashboard leaks as easily as a board paper
- Classification under the NDMO Data Classification Policy
- Personal data under the Personal Data Protection Law

#### [day1#check-every-level] Which item belongs in every level?

*Checkpoint*

**Question:** Your checklist must stay short at level 1, the self-check that most dashboard requests get. Which of these items is required from level 1?

- A. The output is free of personal data and its classification is marked
- B. The model is tested on data it never saw
- C. A reviewer re-runs it from the repository
- D. Every number has an interval

#### [day1#lab-1-2] A checklist adapted from REFORMS

Lab 1.2 · 25 min

Draft a checklist from question to conclusion by adapting a published reproducibility checklist (REFORMS, 32 items): keep, rewrite or drop each item, add the privacy and classification check, and set the level at which each item applies.

[D1_2_team_checklist.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D1_2_team_checklist.ipynb)

- [ ] Map the 32 items to the five review areas (6 min)
- [ ] Keep, rewrite or drop each item (8 min)
- [ ] Add the privacy and classification item (4 min)
- [ ] Set the level of each item and test the length (7 min)
- [ ] ✱ Stretch: Add one item for work an assistant drafted

### Session 3: Reproducibility as a team rule

#### [day1#s3] Reproducibility as a team rule

*Session 3*

- Re-run an analysis from its repository before reading its conclusions
- Classify reproduction failures by kind
- Write repository rules that make a re-run routine

#### [day1#rerun-rule] From level 2, the reviewer re-runs the analysis before reading it

*A team rule*

1. **1 · Clone** the repository, nothing else
2. **2 · Follow the README** exactly as written
3. **3 · Log** each failure, its kind, the fix
4. **4 · Compare** the figure with the report

> **Recap from DS-310.** Re-run first, so the prose does not set your expectations. Here it becomes a rule with a log as its evidence.

#### [day1#saleh-repo] Saleh's repository, as he sent it

*Lab 1.3*

```text
# file: cargo_dwell/
README.md
dwell.py
requirements.txt     pandas
report.md            4.60 days
data/
  containers_q3.csv
```

- Saleh is a senior analyst; the figure goes in the quarterly note
- The README says: put `containers.csv` in `data/`, install, run
- Nothing is wrong that Saleh would notice: it runs on his laptop

#### [day1#five-failures] Five failures before the script ran to the end

*The re-run log*

| # | What failed | Kind |
| --- | --- | --- |
| 1 | A path to a folder on Saleh's own computer | path |
| 2 | README names `containers.csv`; the file is `containers_q3.csv` | documentation |
| 3 | `berth_lookup.csv` is read but not in the repository | missing input |
| 4 | `DataFrame.append` is gone in pandas 2; no version pinned | library version |
| 5 | Two runs, two figures: an unseeded sample of 2,000 | randomness |

#### [day1#the-silent-gap] It ran, and gave 5.18 days against the reported 4.60

*The sixth failure*

```python
# file: dwell.py
imports = boxes[boxes.move_type != "export"]
```

- The filter keeps **transshipment** with imports
- The report removed transshipment by hand, in a spreadsheet
- No file records that step: only the gap shows it
- Filter on imports in code: 4.60, reproduced

> **What goes wrong.** The manual step is the dangerous one: no error, a plausible number, and a reviewer who reads before re-running never sees it.

#### [day1#failure-kinds] One repository rule for each kind of failure

*Rules from the log*

- **Paths and inputs.** Relative paths only; every input in the repository or named with its owner
- **Environment.** A lock file (`uv.lock`) and the one command that installs from it
- **Determinism.** A fixed seed in code; no step outside the code

#### [day1#rerun-cost] A re-run is the cheapest check that finds the most expensive errors

*The cost*

- With the rules followed, a re-run is one command and a comparison
- Without them, it is the 25 minutes of Lab 1.3
- The rules move the cost from the reviewer to the analyst, where it is smallest

- **Your call as head of unit.** A repository that does not re-run goes back to its analyst before the review starts. The review clock starts when it runs.

#### [day1#check-dangerous-failure] Which failure is most dangerous to the unit?

*Checkpoint*

**Question:** A re-run of a colleague's repository meets four problems. Which one most threatens the quality of what the unit releases?

- A. The script crashes on a missing file
- B. An old library call fails with an error
- C. The README names the wrong file
- D. A step done by hand that no file records

#### [day1#lab-1-3] Re-run Saleh's repository

Lab 1.3 · 25 min

Re-run a colleague's cargo-dwell analysis from its repository, record every step that failed and its kind, and reproduce the reported figure.

[D1_3_rerun_repository.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D1_3_rerun_repository.ipynb)

- [ ] Follow the README exactly (5 min)
- [ ] Log each failure with its kind (8 min)
- [ ] Fix a copy until it runs (7 min)
- [ ] Reproduce the reported figure or explain the gap (5 min)
- [ ] ✱ Stretch: Write the repository rule that would have prevented each failure

### Session 4: Rules for AI-assisted analysis

#### [day1#s4] Rules for AI-assisted analysis

*Session 4*

- Turn the national generative AI guidelines into rules for analytical work
- Specify the process evidence each analyst keeps
- Test a rule set on real cases before adopting it

#### [day1#assisted-share] When an assistant drafts the analysis, the analyst's duty does not move

*Why rules now*

- Musawwada drafts code, numbers and summaries in seconds
- A fluent draft looks reviewed; it is not
- The national guidelines put the duty to verify on the **user**

- **What a unit needs.** Rules an analyst can follow before the deadline and a reviewer can check from the files.

#### [day1#guideline-duties] Five duties the unit's rules must carry

*The national guidelines*

| Duty, in our words | Where |
| --- | --- |
| Check generated content for accuracy before it is used | 3.2 Reliability and Safety |
| Tell recipients when content was created with generative AI | 3.3 Transparency and Interpretability |
| Enter no data classified restricted or higher; public data only | 3.5 Privacy and Security |
| Keep a clear record of an analysis done with generative AI | Practical guidelines: analysing data |
| Verify outputs and generated code before use | Appendix 2: checklist |

#### [day1#four-rule-kinds] Verify, disclose, keep, and what data may go in

*The rule set*

- **Verify.** Re-run every assisted number in your own code before it enters a draft
- **Disclose.** A line on the deliverable: which tool, which parts, who verified
- **Keep.** Prompts, outputs and a verification record in the repository
- **Data.** Public or anonymised data only, approved tools only

#### [day1#checkable-rule] A rule a reviewer cannot check from the files is a wish

*Checkable*

| A wish | A rule |
| --- | --- |
| Use the assistant responsibly | Re-run every number it produced, in your own code, before it enters a draft |
| Be transparent about AI use | Every deliverable with assisted content carries a disclosure line: tool, parts, verifier |
| Protect sensitive data where possible | Only public or anonymised data goes to a hosted assistant |

#### [day1#eight-scenarios] Eight scenarios from the unit decide whether the rules work

*Test before adopting*

- **Allowed.** Explaining an error message; the approved tool on public statistics, prompts kept
- **Needs action.** Code checked by hand but no record kept; an analyst who never works unaided
- **Breach.** A pilot roster pasted in; no disclosure on a board paper; an unchecked 18%; an unapproved tool

#### [day1#unaided-practice] Who cannot do the work unaided cannot tell when the draft is wrong

*Keeping the skill*

- Verification needs the skill the assistant replaces
- One analysis a quarter without an assistant, reviewed like any other
- The supervised check of this course is AI-off for the same reason

> **Day 2.** The same idea returns in development plans: every plan keeps unaided practice in the work.

#### [day1#check-restricted-data] An approved assistant and a restricted file

*Checkpoint*

**Question:** An analyst pastes the night pilot roster, with pilots' names and shifts, into the authority's approved hosted assistant to find fatigue risks. She plans to disclose it and re-run every number. Under the rules, what is it?

- A. Allowed: the tool is approved
- B. A breach: restricted data may not go to the assistant
- C. Allowed once the deliverable is disclosed
- D. Needs action: re-run the numbers first

#### [day1#lab-1-4] Rules for assisted work

Lab 1.4 · 25 min

Write what analysts must verify, disclose and keep as evidence when an assistant drafts work, on one page, and test the rules on eight scenarios from the unit.

[D1_4_ai_rules.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D1_4_ai_rules.ipynb)

- [ ] Read the guideline duties (5 min)
- [ ] Write the verify, disclose and keep rules (9 min)
- [ ] Decide eight scenarios with your rules (7 min)
- [ ] Cut the rules to one page (4 min)
- [ ] ✱ Stretch: Add the unaided-practice rule: work each analyst still does without the assistant

#### [day1#wrap-up] Three things to keep

*Day 1 · wrap-up*

- **Proportionate.** The level comes from the effect of an error and the complexity, with written definitions a peer applies the same way.
- **Re-run first.** From level 2 the reviewer re-runs from the repository and logs every failure; the log writes the repository rules.
- **Checkable rules.** Assisted work is verified, disclosed and kept, and only public data goes to an assistant.

#### [day1#next] Day 2: Review and develop

*Next*

Tomorrow's first review is AI-off: you form your own judgement before you compare it with a colleague's. Bring your Day 1 standard and checklist; the labs also supply reference versions.
