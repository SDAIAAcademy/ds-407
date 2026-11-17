---
course: "Leading Analytical Work: Review, Standards and Stakeholders"
code: "DS-407"
version: "2027.1.0"
scope: "course"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/ds-407/"
---

# Leading Analytical Work: Review, Standards and Stakeholders

Set the unit's quality standard, run review as a system, and hold the line on evidence with sponsors

Participants lead the analytics unit of the fictional Ras Sahil Ports Authority: twelve analysts whose work increasingly starts as an assistant's draft. They write a proportionate quality-assurance standard and review checklist, re-run and review colleagues' analyses, set the unit's rules for AI-assisted work, turn review findings into feedback, and negotiate scope, deadline and evidence with role-played sponsors, one of whom asks for an unfavourable result to be dropped. DS-310 teaches reviewing one analysis; this course sets the standards and runs the system.

- **Audience:** Specialists. Data scientists who have completed the level 300 core and practicum, or can show equivalent work: an analysis they led from question to recommendation and defended.
- **Prerequisites:** DS-310 Problem Framing and Analytical Review; Has reviewed an analysis written by someone else and written comments the author acted on; Uses version control for analysis code; Setup: a laptop processor with uv, or Google Colab. Nothing downloads a model; a free hosted model key is optional (every assistant and tutor cell has a stand-in). Run 00_setup_check before Day 1; see labs/README.md.
- **Case study:** Ras Sahil Ports Authority: Ras Sahil Ports Authority is a fictional Gulf-coast port authority whose analytics unit of twelve analysts serves marine operations, commercial affairs, finance and staffing, with more and more work starting as a draft by Musawwada, the unit's drafting assistant. Participants, as the unit's head, write the assurance standard from a log of 30 requests, adapt a published checklist, re-run a colleague's cargo-dwell repository, set rules for assisted work and audit five assisted analyses, calibrate severity with a second reviewer on a seeded-flaw berth-delay analysis, write feedback and a review rota, and negotiate scope, evidence and a pressured subgroup finding with two role-played sponsors. The capstone is the quality-assurance pack for the marine pilot staffing analysis. All data is synthetic and generated with a fixed seed.

## Outcomes

- LO1 (Performance): Design a proportionate quality-assurance standard for analytical work, with assurance levels, a review checklist and sign-off rules, given the unit's log of 30 requests with their uses and risks
- LO2 (Performance): Review analyses by others, including assistant-drafted ones, rank findings by their effect on the decision and calibrate severity with a second reviewer, given three seeded-flaw analysis repositories
- LO3 (Performance): Design rules for AI-assisted analysis covering verification, disclosure and the process evidence each analyst keeps, and audit the unit's work against them, given the national generative AI guidelines and a log of the unit's assisted analyses
- LO4 (Applied): Prepare feedback and a development plan for an analyst from review findings, given a reviewed notebook and the analyst's skills profile
- LO5 (Performance): Lead a negotiation with a sponsor on scope, deadline and evidence threshold and record the agreement, given a role-played sponsor whose constraints change during the meeting
- LO6 (Performance): Decide how to respond to pressure to change or suppress a finding, and record the reasons, given a scripted request to remove an unfavourable subgroup result

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

## Day 2: Review and develop

Calibrated reviewers, audits of assisted work, feedback and a review rota

#### [day2#title] Review and develop

*SDAIA Academy · Leading Analytical Work: Review, Standards and Stakeholders*

Day 2: Calibrated reviewers, audits of assisted work, feedback and a review rota

Data Science Track · 3 teaching days + capstone day · 4 sessions · 4 labs · DS-407

#### [day2#agenda] Review and develop

*Today*

- **Session 1 · Calibrating reviewers**: Severity by effect on the decision, rated alone, then compared and turned into clearer wording
- **Session 2 · Auditing assisted work**: An audit checks the evidence a rule asks for, recomputes what it can and records each breach with its rule
- **Session 3 · Feedback that builds skill**: From findings to feedback that names the reasoning, and a plan that keeps unaided practice in the work
- **Session 4 · Review capacity and mentoring**: Review hours follow assurance levels; senior reviewers are the bottleneck; pairings develop analysts

#### [day2#review-day1] Which request is graded right under yesterday's standard?

*Review of Day 1*

**Question:** Four requests and the level an analyst gave each, with the unit's matrix and escalators. Which one is graded right?

- A. A model that sets night pilot numbers: level 2, it is a simple regression
- B. A staff survey summary with personal data: level 3
- C. A dwell figure for the ministry's indicators: level 2
- D. A tariff revenue estimate for the board: level 3

### Session 1: Calibrating reviewers

#### [day2#s1] Calibrating reviewers

*Session 1*

- Rate review findings by their effect on the decision
- Measure agreement between two reviewers, beyond chance
- Turn disagreements into clearer checklist wording

#### [day2#the-draft] "Slot booking has halved waiting at T2. Extend it to all terminals."

*The draft*

```text
# file: analysis.py output
mean wait, months 13 to 24:
  T2 7.5 h, other terminals 12.9 h
reduction at T2: 42%
T2 before 10.7 h, after 7.5 h
```

- The berth-allocation pilot: slot booking at T2 from month 13
- The director of marine operations wants it extended
- Two reviewers review it alone: you and Faleh Al-Musharraf

#### [day2#severity-scale] Rate a finding by what it does to the decision, not by how you found it

*Severity*

- **3 · Critical.** The decision changes, or the output cannot leave the unit
- **2 · Major.** The size or the confidence of the result changes, not the decision
- **1 · Minor.** Presentation: a label, a chart, a name

> **Recap from DS-310.** Ranking flaws by consequence is the individual reviewer's skill. Today two reviewers must reach the same rating, and the unit's standard (S-5) writes the scale down.

#### [day2#six-flaws] Six findings, two of them critical

*The reference review*

| Finding | Severity |
| --- | --- |
| C1 · T2 compared with others after the change only; T2 was already fastest | 3 |
| P1 · Vessel masters' names and mobile numbers in table 5 | 3 |
| C2 · Diverted calls dropped; at T2 they rose from 17 to 35 | 2 |
| M1 · "Halved" in the text; 42% in the output | 2 |
| M2 · Weather closures in T2's before period | 1 |
| m1 · Table 4 labelled minutes; the values are hours | 1 |

#### [day2#fix-one-at-a-time] Fix a flaw and re-run: the decision flips on C1

*Measuring the effect*

| Item | Value |
| --- | --- |
| As written | -5.36 h |
| C1 fixed | -1.37 h |
| C1 and C2 fixed | -0.94 h |
| C1, C2 and M2 fixed | -0.78 h |

Effect of slot booking on waiting at T2, hours per call (Lab 2.1 stretch). The draft recommends extending at -2 hours or more; after C1 it does not.

#### [day2#alone-then-compare] Review alone, then compare, then discuss only the big gaps

*The method*

1. **1 · Alone** re-run, list findings, rate, AI-off
2. **2 · Compare** one table, both ratings, the gap
3. **3 · Discuss** gaps of two levels only
4. **4 · Revise** the checklist sentence that allowed the gap

#### [day2#agreement-table] Half the ratings agree; the biggest gap is the privacy finding

*Two reviewers*

| Finding | You | Faleh | Gap |
| --- | --- | --- | --- |
| C1 | 3 | 3 | 0 |
| C2 | 2 | 3 | 1 |
| M1 | 2 | 2 | 0 |
| M2 | 1 | 2 | 1 |
| P1 | 3 | 1 | 2 |
| m1 | 1 | 1 | 0 |

#### [day2#kappa] 50% agreement is a weighted kappa of 0.25

*Beyond chance*

**0.25** weighted kappa, six findings (Lab 2.1)

- Kappa removes the agreement two reviewers reach by chance
- Weighted kappa counts a gap of two as worse than a gap of one
- 1 is perfect agreement; 0 is no better than chance
- Track it each quarter on a shared analysis

#### [day2#disagreement-to-wording] Each big gap becomes a sentence in the checklist

*The output of calibration*

- **P1, before.** Is the output free of personal data, and is its classification marked?
- **P1, after.** The same question, plus the anchor: a breach is critical whatever its effect on the decision, because the output cannot leave the unit.

#### [day2#check-kappa] High agreement, low kappa: what happened?

*Checkpoint*

**Question:** Two reviewers rate 20 findings and agree on 16 of them, 80%. Their weighted kappa is 0.3. Which explanation fits?

- A. The kappa was computed wrongly
- B. Most findings were rated minor by both, so much of the agreement was expected by chance
- C. Four disagreements are too many for any team
- D. Twenty findings are too few to compute kappa

#### [day2#lab-2-1] Two reviewers, one analysis

Lab 2.1 · 25 min

Review a seeded-flaw berth-delay analysis independently with a partner (AI-off), compare severity ratings in an agreement table, and revise the checklist where you disagree.

[D2_1_calibrate_reviewers.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D2_1_calibrate_reviewers.ipynb)

- [ ] Re-run and review alone (9 min)
- [ ] Rate each finding by its effect on the decision (5 min)
- [ ] Agreement table and weighted kappa (6 min)
- [ ] Revise the checklist where you disagreed (5 min)
- [ ] ✱ Stretch: Measure what each flaw does to the headline by fixing it alone

### Session 2: Auditing assisted work

#### [day2#s2] Auditing assisted work

*Session 2*

- Audit work against rules from its evidence, not its claims
- Recompute a number an assistant drafted
- Record each breach with the rule it breaks

#### [day2#audit-not-review] A review asks if the analysis is right; an audit asks if the rules were followed

*Audit or review*

- **Review.** One analysis, all five areas, before release. The reviewer re-runs and rates findings.
- **Audit.** A sample of released work, against the rules for assisted analysis. The auditor checks the evidence each rule asks for.

> **The rule of thumb.** No evidence, no compliance. "I checked the numbers" is a claim; a verification record is evidence.

#### [day2#five-records] Five assisted analyses from the unit's log

*The sample*

| Id | Analysis | What the record shows |
| --- | --- | --- |
| A1 | Tug fuel use per call | Disclosed, prompts kept, figures re-run |
| A2 | Fatigue risk in the night pilot roster | Data sent: names and shifts of pilots |
| A3 | Share of T1 calls waiting over 12 hours | 18.4%; no verification record |
| A4 | Storage-fee scenarios for the board | No disclosure line on the paper |
| A5 | Gate no-show patterns | No prompts, no record; "I checked" |

#### [day2#recompute] A3 says 18.4%; the authority's own data say 47.7%

*Recompute what you can*

```python
# file: recompute A3
t1 = calls[(calls.terminal == "T1")
           & (calls.month >= 13)]
recorded = t1.dropna(subset=["wait_h"])
(recorded.wait_h > 12).mean()   # 0.477
```

- 1,387 calls with a recorded wait; 35 diverted
- The record showed the number was not verified
- Only the recomputation showed how wrong it was

#### [day2#breach-table] Each breach is recorded with the rule it breaks and the action it needs

*The audit table*

| Id | Rules | Action |
| --- | --- | --- |
| A1 | none | none |
| A2 | C1 data | Tell the data protection officer; redo on anonymised data |
| A3 | V1 verify, K2 keep | Withdraw the figure; re-run and re-review |
| A4 | D1 disclose | Disclosure note to the board secretary |
| A5 | K1, K2 keep | Re-run and keep the record before reuse |

#### [day2#audit-to-rule] Two of five had no verification record: change the process, not just the analyses

*What the audit teaches*

- The rule existed; nothing made it visible before review
- Proposed: no review of assisted work starts without its verification record
- The checklist item C2 asks for it at every level

- **How often.** Five analyses a quarter, chosen at random from the assisted log, plus any the reviewers flag.

#### [day2#audit-fairly] An audit finds breaches of rules, not bad analysts

*Tone*

- **Record facts.** What the file shows, which rule, which action
- **Fix the process.** Two missing records point at the process, not two people
- **Feed development.** A pattern for one analyst goes into feedback, the next session

#### [day2#check-audit-evidence] "I checked the numbers"

*Checkpoint*

**Question:** An analyst's assisted analysis has a disclosure line and correct figures when you recompute them, but no prompts and no verification record. He says he checked everything. What does the audit record?

- A. No breach: the figures are right
- B. A breach of the disclosure rule
- C. A breach of the keep rules: no prompts and no record
- D. A breach of the verify rule only

#### [day2#lab-2-2] Audit five assisted analyses

Lab 2.2 · 25 min

Check five assistant-drafted analyses from the unit's log against the rules for AI-assisted work, recompute the one headline that can be recomputed, and record each breach with its rule.

[D2_2_audit_assisted.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D2_2_audit_assisted.ipynb)

- [ ] Read the rules and the log (4 min)
- [ ] Check each record against the rules (9 min)
- [ ] Recompute one headline number (7 min)
- [ ] Write the audit table (5 min)
- [ ] ✱ Stretch: Propose the one rule change the audit suggests

### Session 3: Feedback that builds skill

#### [day2#s3] Feedback that builds skill

*Session 3*

- Choose the findings worth raising with an analyst
- Write feedback that names the reasoning, not only the error
- Plan development with goals, evidence and unaided practice

#### [day2#seven-to-three] Seven findings is a review; three is feedback

*From review to feedback*

- Shaden Al-Ruwayshid joined six months ago; Faleh found seven things in her notebook
- The review notes go to the analysis; the feedback goes to the analyst
- Choose the three findings that show a pattern in her reasoning
- Name one strength, specifically

- **Her three.** No comparison group (F2), the wrong population in an average (F1), assisted cells not verified (F7)

#### [day2#four-parts] Observation, effect, reasoning, next step

*One note*

| Part | Shaden, F2 |
| --- | --- |
| **Observation** | In cell 5 waiting at T2 is compared before and after, with no other terminal |
| **Effect** | Waiting fell everywhere in month 13, so most of the fall would have happened anyway |
| **Reasoning** | Before claiming a cause, ask what would have happened without it |
| **Next** | In your next comparison, write the comparison group in the first cell |

#### [day2#vague-feedback] "Be more careful with comparisons" tells her nothing she can do

*Specific*

- **Vague.** Be more careful. Improve your rigour. Pay attention to the data. Good job on the charts.
- **Specific.** Cell 3 averages imports with transshipment, 5.2 days. Print the counts by move type before every average.

> **The peer test.** Would a colleague reading the note know what Shaden should do differently next week? That is the evidence of outcome 4.

#### [day2#skills-profile] Her lowest skills are methods, inference and checking assisted work

*The plan starts from the profile*

| Item | Value |
| --- | --- |
| Communication | 3 |
| Framing | 2 |
| Data handling | 2 |
| Reproducibility | 2 |
| Methods | 1 |
| Inference | 1 |
| Assisted-work verification | 1 |

Shaden's skills profile, 1 to 4 (synthetic, Lab 2.3).

#### [day2#three-months] Three months, each with a goal, the evidence and the support

*The plan*

| Month | Goal | Evidence |
| --- | --- | --- |
| 1 | A comparison group every time | Two analyses passed on checklist item M1 |
| 2 | Verify every assisted number before review | Three complete verification records |
| 3 | State uncertainty, working unaided | An unaided analysis that passes level 2 review |

#### [day2#unaided-in-plan] An analyst who checks assistants must still do the work alone

*Keeping the skill*

- Her verification skill is 1 of 4: she cannot check what she cannot do
- Month 3 is unaided: no assistant, the full analysis, a normal review
- The rule set's U1 makes this a quarterly habit for everyone

> **From the catalog.** Keeping unaided practice in the work is a topic of this course, not an option.

#### [day2#check-specific-note] Which note will change what she does next week?

*Checkpoint*

**Question:** Four feedback notes on the same finding: an average that mixed imports with transshipment.

- A. Cell 3 averages imports with transshipment (5.2 days); print counts by move type before every average
- B. Be more careful with the populations you average over
- C. Your dwell figure was wrong because of transshipment
- D. Read the unit's data-handling guide again this month

#### [day2#lab-2-3] Feedback and a three-month plan

Lab 2.3 · 25 min

Turn review findings on a new analyst's notebook into a feedback note that names the reasoning, and a three-month plan built on her skills profile.

[D2_3_feedback_plan.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D2_3_feedback_plan.ipynb)

- [ ] Choose three findings to raise (5 min)
- [ ] Write each note: observation, effect, reasoning, next step (9 min)
- [ ] A three-month plan from the skills profile (8 min)
- [ ] Check that every line is specific (3 min)
- [ ] ✱ Stretch: Write the two-line summary for the analyst's file

### Session 4: Review capacity and mentoring

#### [day2#s4] Review capacity and mentoring

*Session 4*

- Estimate a quarter's review hours from assurance levels
- Assign reviewers under separation and seniority rules
- Use review pairings to develop analysts

#### [day2#levels-to-hours] Assurance levels turn into review hours

*Capacity*

| Level | Analyses next quarter | Hours each | Who |
| --- | --- | --- | --- |
| 1 | 10 | 0 | the analyst |
| 2 | 14 | 4 | any non-junior peer |
| 3 | 12 | 10 | a senior |
| 4 | 4 | 16 + 8 | a senior and a second reviewer |

#### [day2#senior-bottleneck] Seniors are needed for 184 hours and have 150

*The bottleneck*

**34 h** short in senior review hours next quarter

- Three seniors, 60, 50 and 40 review hours
- Six mid-level analysts have hours to spare
- The rule keeps level 3 and 4 with seniors

#### [day2#close-the-gap] Close the gap without lowering a level

*Options*

- **Co-sign.** A mid-level analyst reviews a level 3 analysis; a senior checks the review in 2 hours. Saves 8 senior hours.
- **Defer.** Move a level 3 analysis whose decision can wait to the next quarter, with the sponsor's agreement.
- **Never.** Lower the level to fit the rota. The level comes from the risk, not the hours.

#### [day2#the-rota] Every rule kept: Faleh and Saleh end at full capacity

*The rota*

| Item | Value |
| --- | --- |
| Faleh (senior) | 60 of 60 h |
| Saleh (senior) | 50 of 50 h |
| Noor (senior) | 34 of 40 h |
| Lina (mid) | 32 of 70 h |
| Rakan (mid) | 32 of 70 h |

Review load from the reference rota of Lab 2.4; five co-signed level 3 reviews.

#### [day2#mentoring-pairs] Juniors shadow a mentor's reviews before they review

*Mentoring*

- Juniors do not review alone, but they watch reviews from their first month
- One junior per mentor; the mentor reviews some of the junior's work when the rota allows
- Shaden with Faleh; Turki with Lina; Dalia with Rakan

- **A trade-off to state.** Faleh is at full capacity and mentors Shaden. Either the shadowing fits inside his reviews, or one of his reviews moves.

#### [day2#check-shortfall] Senior hours run short: what do you do?

*Checkpoint*

**Question:** Next quarter's level 3 and 4 reviews need 184 senior hours; your seniors have 150. A director asks you to "just call some of them level 2".

- A. Lower five level 3 analyses to level 2
- B. Ask the seniors to absorb the extra hours
- C. Let mid-level analysts review level 3 alone
- D. Co-sign five level 3 reviews and defer what can wait

#### [day2#lab-2-4] A quarter's review rota

Lab 2.4 · 25 min

Plan a quarter's review load and pairings for a team of twelve: assign 40 planned analyses to reviewers under the separation and seniority rules, find the shortfall and choose how to close it.

[D2_4_review_capacity.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D2_4_review_capacity.ipynb)

- [ ] Review hours by level for the quarter (5 min)
- [ ] Assign reviewers under the rules (9 min)
- [ ] Find the overload and the shortfall (6 min)
- [ ] Pair the juniors with mentors (5 min)
- [ ] ✱ Stretch: Choose which mid-level analyst trains as a level 3 reviewer, and how

#### [day2#wrap-up] Three things to keep

*Day 2 · wrap-up*

- **Calibrate.** Review alone, compare, and turn each big gap into a sentence of the checklist.
- **Audit evidence.** No record, no compliance; recompute the headline where the record is missing.
- **Develop people.** Three findings with their reasoning, a plan with evidence and unaided practice, and a rota that trains.

#### [day2#next] Day 3: Work with sponsors

*Next*

Tomorrow the sponsors arrive: a deadline that moves, an evidence threshold to agree before the analysis, and a request to drop a finding. Read the slot-booking draft again tonight: you will defend what you found in it.

## Day 3: Work with sponsors

Scope, evidence agreed first, pressure on a finding, and quality reported honestly

#### [day3#title] Work with sponsors

*SDAIA Academy · Leading Analytical Work: Review, Standards and Stakeholders*

Day 3: Scope, evidence agreed first, pressure on a finding, and quality reported honestly

Data Science Track · 3 teaching days + capstone day · 4 sessions · 4 labs · DS-407

#### [day3#agenda] Work with sponsors

*Today*

- **Session 1 · Scope and deadline**: What can be answered by the deadline, offered as options and recorded when the constraints change
- **Session 2 · Agreeing the evidence first**: The decision rule and an evidence threshold the data can detect, written and signed before the analysis
- **Session 3 · Pressure on a finding**: Challenge or pressure: check the finding, weigh the options, decide and record the reasons
- **Session 4 · Reporting quality and correcting errors**: A quality statement says what was checked, by whom and what is uncertain; a correction says what changed, fast

#### [day3#review-day2] Two reviewers agree on half their ratings. What comes next?

*Review of Day 2*

**Question:** You and a colleague reviewed the same analysis alone. You agree on three of six severity ratings; the largest gap, two levels, is on a privacy finding.

- A. Record a severity of 2 for the privacy finding
- B. Use the senior reviewer's ratings
- C. Discuss the privacy gap and add the sentence to the checklist that prevents it
- D. Discuss all three disagreements in turn

### Session 1: Scope and deadline

#### [day3#s1] Scope and deadline

*Session 1*

- Size questions against a deadline, review time included
- Offer options when a request cannot be met as asked
- Record what was agreed and what was not

#### [day3#the-ask] "I need the slot-booking result for the board in a week"

*The request*

- Bader Al-Khayyal, director of marine operations, sponsors the berth-allocation pilot
- One analyst is free; the board papers close in five working days
- The draft he has seen says waiting "halved"; he has heard it has problems

- **The trap.** Say yes to everything and cut the review, or say no and lose the sponsor. Both are avoidable.

#### [day3#size-with-review] The review is part of the time, not something after it

*Size it first*

| Question | Level | Analyst days | With review |
| --- | --- | --- | --- |
| Q-a · Waiting at T2 against the other terminals | 3 | 1.5 | 2.5 |
| Q-b · The same by vessel type, feeders separate | 3 | 0.5 | 1.5 |
| Q-c · Diversions by terminal | 2 | 1 | 1.5 |
| Q-d · Forecast for all four terminals | 4 | 6 | 8 |
| Q-e · Cost to the shipping lines | 3 | 4 | 5 |

#### [day3#ask-before-offer] Ask four things before offering anything

*The meeting*

- **Decision.** Which decision will this inform, and who takes it?
- **Deadline.** When exactly, and is there time after it for a correction?
- **Evidence.** What would convince you, and what would make others object?
- **What exists.** Is there a draft, an earlier report, a number already quoted?

#### [day3#options] Two options fit five days; the full set needs a later board

*Options, not refusal*

- **A · 4.0 days.** Q-a and Q-c: the effect and diversions. Leaves out vessel types, the forecast and the cost to the lines.
- **B · 4.0 days.** Q-a and Q-b: the effect and vessel types. Leaves out diversions, the forecast and the cost.
- **C · 10.5 days.** Q-a, Q-b, Q-c, Q-e. Leaves out the forecast; goes to the following board.

#### [day3#constraint-changes] "Four days, not five. And the deputy CEO wants the feeder lines."

*Halfway through*

- **Do not.** Promise the same scope in fewer days. The day that disappears is the review.
- **Do.** Go back to the options: B fits four days and answers the feeder question. Diversions move to the next board.

#### [day3#scope-record] The scope agreement records what is out as clearly as what is in

*Write it down*

| Field | Recorded |
| --- | --- |
| Decision | Whether to extend slot booking to all four terminals next quarter |
| In scope | Q-a, Q-b · 4.0 of 4 working days |
| Out of scope | Q-c and Q-e for the following board; Q-d not before a decision to extend |
| After the change | Option B: answers the feeder question; diversions move |

#### [day3#observer] Five criteria, each scored 0 to 2

*The observer*

- Asked before offering
- Offered options, not a refusal
- The agreed scope fits the deadline
- Named what is out of scope
- Handled the change with an option

> **For the observer.** Write down the sentence that earned or lost each point. A score without the sentence teaches nothing.

#### [day3#check-deadline-cut] The deadline moves from five days to four

*Checkpoint*

**Question:** You agreed option A, 4.0 days with review. The sponsor now says four days, and adds a question on feeder vessels. What do you answer?

- A. Keep A and add the feeder question; the team will work longer
- B. Offer B in place of A: it fits four days and answers the feeder question
- C. Drop the review to level 2 so everything fits
- D. Say the deadline cannot be met and ask for a later board

#### [day3#lab-3-1] A result in a week

Lab 3.1 · 25 min

Role-play the director of marine operations, who wants the berth-allocation result in a week: agree what can be answered by the deadline, keep the agreement when his constraints change, and record it.

[D3_1_scope_deadline.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D3_1_scope_deadline.ipynb)

- [ ] Size the questions against the deadline (5 min)
- [ ] Open the meeting and ask (6 min)
- [ ] Respond when the constraints change (6 min)
- [ ] Record the scope agreement (5 min)
- [ ] The observer's score (3 min)
- [ ] ✱ Stretch: Play the sponsor for a peer, with the role card

### Session 2: Agreeing the evidence first

#### [day3#s2] Agreeing the evidence first

*Session 2*

- Write the decision rule before the analysis
- Check an evidence threshold against what the data can detect
- Record roles and sign-off in the agreement

#### [day3#rule-before-result] Agree what result would change the decision before anyone sees it

*Before the analysis*

- After the result, every threshold looks negotiable
- Before it, the sponsor says what matters to him
- The agreement turns "extend it if waiting falls" into a rule with numbers

> **From DS-310.** Pre-registering a decision rule for your own analysis is the analyst's habit. Here the head of unit agrees it with the sponsor and signs it.

#### [day3#agreement-parts] Five parts, one page

*The agreement*

1. **Question** as the board's choice
2. **Options** including not to act
3. **Rule** threshold and conditions
4. **Data** window and exclusions
5. **Roles** level and sign-off

#### [day3#mdc] With 12 months after the change, the data can detect 0.66 hours

*What the data can detect*

| Item | Value |
| --- | --- |
| 3 months after | 1.13 h |
| 6 months after | 0.84 h |
| 12 months after | 0.66 h |
| Threshold | 2.0 h |

Minimum detectable change of the difference in differences, about 2.8 standard errors (80% power, 5% test). Lab 3.2, synthetic berth calls.

#### [day3#decision-rule] Extend only if waiting falls by 2 hours and no vessel type loses more than 2

*The rule*

- **Before.** "Extend it if waiting falls at all."
- **Agreed.** Extend if waiting at T2 falls by at least 2.0 hours per call against the other terminals, and no vessel type waits more than 2.0 hours longer; otherwise keep at T2 and fix the slots for the type that lost.

#### [day3#roles-signoff] Level 3: three different people analyse, assure and approve

*Sign-off*

| Role | Person |
| --- | --- |
| Commissioner | Bader Al-Khayyal, director of marine operations |
| Analyst | Saleh Al-Ghamlas |
| Assurer | Faleh Al-Musharraf |
| Approver | Arjwan Al-Huqail, head of the unit |

#### [day3#the-estimate] Waiting fell 0.78 hours; feeders wait 6.32 hours longer

*Then, the result*

- **-0.78 h** all calls at T2, against the other terminals
- **+6.32 h** feeder vessels
- **-2.88 h** the other vessel types

Difference in differences, Lab 3.2 and 3.3, synthetic. Both conditions of the rule fail: keep at T2, fix the feeder slots.

#### [day3#check-threshold] A threshold the data cannot test

*Checkpoint*

**Question:** With three months of data after the change, the minimum detectable change is 1.13 hours. The sponsor wants to extend "if waiting falls by half an hour". What do you do?

- A. Sign it: the sponsor sets the threshold
- B. Use a looser test so half an hour can show
- C. Run the analysis first, then agree the threshold
- D. Show him the detectable change and agree a longer window or a threshold the data can test

#### [day3#lab-3-2] An analysis agreement

Lab 3.2 · 25 min

Write an analysis agreement for the pilot decision: question, decision rule and an evidence threshold the data can detect, with roles and sign-off.

[D3_2_analysis_agreement.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D3_2_analysis_agreement.ipynb)

- [ ] The decision and its options (5 min)
- [ ] Compute the change the data can detect (8 min)
- [ ] Set the decision rule and the threshold (7 min)
- [ ] Roles, level and sign-off (5 min)
- [ ] ✱ Stretch: Say in the agreement what happens when the result falls between the thresholds

### Session 3: Pressure on a finding

#### [day3#s3] Pressure on a finding

*Session 3*

- Tell a legitimate challenge from pressure to suppress
- Respond with options that keep the finding
- Record a decision with its reasons and references

#### [day3#the-email] "Please take the feeder table out of the paper"

*The request*

- Khaled Al-Kharji, deputy chief executive for commercial affairs
- Feeders are "small local operators, less than a quarter of calls"
- "The table will distract the board"; his team will handle the feeder lines
- He needs the final version by the end of tomorrow

- **Read it fairly.** The request is polite and gives reasons. Some of them could be right. Check before you decide.

#### [day3#challenge-or-pressure] Is it a challenge to the finding, or pressure on it?

*The first question*

- **A challenge.** Says the finding may be wrong: too few cases, noise, a coding error. Answered by checking, and the finding may change.
- **Pressure.** Accepts the finding but wants it unseen: "distracting", "handled elsewhere". Answered by a decision, recorded.

#### [day3#recompute-subgroup] 278 feeder calls at T2 after the change: not noise

*Check it*

```python
# file: Lab 3.3
U.subgroup_did("feeder")           # +6.32 h
U.subgroup_did(exclude="feeder")   # -2.88 h
# feeder calls at T2 after: 278, diverted 33
```

- Hundreds of calls; the effect is many times its noise
- 33 of the 35 diverted T2 calls after the change were feeders
- The feeder condition is in the signed rule

#### [day3#three-options] Remove, keep, or keep with context

*Options*

| Option | What it does |
| --- | --- |
| Remove the table | The board may extend a scheme that adds hours of waiting for local lines; the signed rule is not applied |
| Keep it as it is | The rule is applied; the commercial team may feel ambushed |
| Keep it with context | State the feeder share of calls and revenue; invite the commercial team's plan for the feeder slots |

#### [day3#decision-record] Record the decision the same day, with its reasons and references

*The record*

- **S-7.** Findings are not removed from a paper after review; a disagreement is recorded beside the finding
- **S-8.** Pressure on a finding is recorded the same day; if repeated, escalated to the chief executive's office
- The signed rule includes the vessel-type condition

- **SDAIA AI Ethics Principles.** Fairness · Transparency & Explainability · Accountability & Responsibility

#### [day3#the-reply] Keep the relationship and the finding

*The reply*

1. **Acknowledge** the concern, in his words
2. **Decide** the table stays
3. **Why** the signed rule, the size
4. **Offer** context and his team's plan

#### [day3#check-pressure] A senior asks to remove an unfavourable subgroup

*Checkpoint*

**Question:** You checked the subgroup: hundreds of cases, a large effect, and its condition is in the signed decision rule. The deputy chief executive asks again to remove it. What do you do?

- A. Remove it and mention it in a footnote
- B. Remove it, since he outranks you
- C. Keep it, record the repeated request and escalate with the record
- D. Keep it, but leave the request out of the record

#### [day3#lab-3-3] Drop the feeder result?

Lab 3.3 · 25 min

Handle a scripted request to drop an unfavourable subgroup (feeder vessels) from the pilot evaluation: recompute it, weigh the options, decide, and record the decision citing the unit's standard and the ethics principles.

[D3_3_pressure_finding.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D3_3_pressure_finding.ipynb)

- [ ] Read the request and recompute the subgroup (6 min)
- [ ] Weigh the options (5 min)
- [ ] Decide and write the decision record (8 min)
- [ ] Draft the reply (6 min)
- [ ] ✱ Stretch: Write the escalation note for a repeated request

### Session 4: Reporting quality and correcting errors

#### [day3#s4] Reporting quality and correcting errors

*Session 4*

- Write a quality statement a board can read
- Correct a released figure quickly and openly
- Link a correction to the change in process

#### [day3#quality-statement] A quality statement a board reads in a minute

*For the board*

| Part | Slot-booking paper |
| --- | --- |
| Level | 3: independent review, approved by the head of unit |
| Checked | Re-run to the same figures; every number traced; no personal data |
| By whom | Saleh Al-Ghamlas; reviewed by Faleh Al-Musharraf; approved by Arjwan Al-Huqail |
| Uncertain | The fall is 0.78 hours per call, likely between 0.3 and 1.3 |
| Assisted | Method draft written with the approved assistant, verified line by line |
| Classification | Internal |

#### [day3#uncertainty-number] "Results may vary" cannot be weighed; "between 0.3 and 1.3 hours" can

*Uncertainty*

- **Vague.** The results are subject to some uncertainty and should be interpreted with care.
- **Usable.** The fall is likely between 0.3 and 1.3 hours, below the 2-hour threshold agreed with the sponsor.

#### [day3#q2-error] Q2 dwell was released as 4.07 days; it is 4.32

*After release*

**1,080** rows loaded twice, weeks 5 and 6

- The terminal system re-sent two weeks; the load accepted them
- The duplicated weeks had short dwell, so the mean was understated
- The figure went to the board and to the ministry's indicator team

#### [day3#correction-notice] A correction names the process, not the person

*The notice*

- Released and corrected values, side by side
- The cause in the process: a load that accepted duplicates, a check that did not exist
- Decisions affected: quoted in the storage-fee discussion; no fee changed on it
- The change: a duplicate check on every extract, from level 1 for published figures
- Who is told: the board secretary, the ministry team, the quarterly note's readers

> **S-10.** Within five working days of finding the error.

#### [day3#who-first] Tell the people who acted on the figure before the people who read it

*Order matters*

1. **1 · Board secretary** the paper of record quoted it
2. **2 · Ministry team** it went into a national indicator
3. **3 · Note readers** internal readers

#### [day3#check-correction] The corrected figure is better news

*Checkpoint*

**Question:** A released figure is found to be wrong; the corrected value is higher and more favourable to the authority. No decision changed on the old one. What do you do?

- A. Use the corrected figure from now on, without a notice
- B. Issue a notice within five working days, with both values and the cause in the process
- C. Correct it in next quarter's paper
- D. Issue a notice naming the analyst who released it

#### [day3#lab-3-4] A quality statement and a correction

Lab 3.4 · 25 min

Draft a board-paper quality statement for the pilot evaluation (what was checked, by whom, what remains uncertain) and a correction notice for the Q2 cargo-dwell figure found wrong after release.

[D3_4_quality_correction.ipynb](https://sdaiaacademy.github.io/ds-407/labs/D3_4_quality_correction.ipynb)

- [ ] Write the quality statement (8 min)
- [ ] Find and size the Q2 error (7 min)
- [ ] Write the correction notice (7 min)
- [ ] Check both against the standard (3 min)
- [ ] ✱ Stretch: Decide who is told of the correction, and in which order

#### [day3#wrap-up] Three things to keep

*Day 3 · wrap-up*

- **Options.** Size with the review included, ask before offering, record what is out.
- **Rule first.** Agree a testable threshold and sign it before the result exists.
- **Keep findings.** Check a challenge, record pressure, correct errors openly.

#### [day3#next] Day 4: The capstone

*Next*

You receive one high-risk analysis: the one that sets night pilot numbers. Apply your standard, review it, agree the evidence with its sponsor, write the board's quality statement, and chair the review meeting.

## Capstone: Capstone: the staffing pack and the review meeting

A quality-assurance pack for the marine pilot staffing analysis, and the review meeting you chair

#### [capstone#title] Capstone: the staffing pack and the review meeting

*SDAIA Academy · Leading Analytical Work: Review, Standards and Stakeholders*

Capstone: A quality-assurance pack for the marine pilot staffing analysis, and the review meeting you chair

Data Science Track · 3 teaching days + capstone day · DS-407

#### [capstone#agenda] Review alone, build the pack, then chair the meeting

*Capstone day*

- **Supervised check**: one short seeded-flaw analysis, reviewed without AI assistance
- **Build and publish the pack**: standard, review report, agreement and quality statement, in a public repository by the deadline
- **Chaired review meetings**: each with a role-played analyst and sponsor, observed
- **Review and closing**: what the room learned, the follow-up task

#### [capstone#supervised-check] The supervised check: one analysis, 40 minutes, no AI

*20% of the result*

- A short analysis you have not seen, with seeded flaws
- Re-run it, list the findings and rate each by its effect on the decision
- Marked against the trainer's key: the findings that change the decision count most

#### [capstone#the-brief] Night pilots: cut the shift from six to four?

*The case*

**Bader Al-Khayyal, director of marine operations:** Saleh's analysis says four night pilots are enough. I want it on the board's agenda this month.

**Saleh Al-Ghamlas, analyst:** The mean is 10.7 jobs a night and a pilot does three. Four is plenty.

- `labs/capstone/data/pilot_jobs.csv`: a year of synthetic night pilotage jobs
- `labs/capstone/data/staffing.py`: the analysis to assure
- A safety use: pilot numbers decide whether ships wait for a pilot at night

#### [capstone#hand-in] Four documents and their commit history, in a public repository

*The repository*

- **standard.md.** The level of this analysis: effect, complexity, escalators, and the roles
- **review.md.** The re-run log and the findings, rated by effect on the decision
- **agreement.md.** Question, options, decision rule, a threshold the data can detect, sign-off
- **quality_statement.md.** For the board, at most 160 words, with uncertainty as a number

#### [capstone#own-variant] Each participant assures a variant of the staffing analysis of their own

*Authenticity*

- The repository holds one version, for practice
- The trainer gives you your own variant this morning, with its own data and flaws
- Your review report is matched against your variant's key

- **As in Lab 2.1.** The same severity scale, the same method: re-run first, then rate by what each finding does to the decision.

#### [capstone#rubric] Five criteria, 100 points

*The pack*

| Item | Value |
| --- | --- |
| Standard applied and roles | 20% |
| Review findings ranked by effect | 30% |
| Analysis agreement | 20% |
| Board quality statement | 20% |
| Clarity | 10% |

#### [capstone#weights] Three parts make the result, each with its own floor

*The result*

| Part | Weight |
| --- | --- |
| Supervised check, without AI | 20% |
| The pack, on the rubric | 50% |
| The chaired review meeting, observed | 30% |

> **To pass:** 70% overall, and at least 60% on each part.

#### [capstone#meeting-format] You chair; the analyst defends; the sponsor wants it on the agenda

*Fifteen minutes*

- **Open · 2 min.** Purpose, the level, what the meeting must decide
- **Findings · 8 min.** The findings that change the decision first; hear the analyst on each
- **Close · 5 min.** The decision, what changes before the board, who does what, the record

> **During the meeting** the sponsor presses: a date, a finding he wants softened, or a reason to skip a step. Chair through it.

#### [capstone#meeting-rubric] The observer scores five things, 0 to 2 each

*30% of the result*

| Criterion | Full marks |
| --- | --- |
| Opening | States the purpose, the level and the decision the meeting must reach |
| Findings | Puts the decision-changing findings first, with the evidence |
| The analyst | Hears the defence, accepts what is right, holds what is not |
| The sponsor's pressure | Answers with options; keeps the finding and the level |
| Close | A decision, actions with owners, and what goes in the record |

#### [capstone#practice-pressure] A practice push from the sponsor: what do you say?

*Practise it now*

**Bader Al-Khayyal:** The board meets this month. Can we take the recommendation as it is and fix the details afterwards?

- Which finding makes "as it is" impossible, and why?
- What can go to this month's board, and at which level?
- What goes in the record of the meeting?

#### [capstone#running-order] Who chairs when

*Running order*

| # | Participant | Repository |
| --- | --- | --- |
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |
| 5 |  |  |
| 6 |  |  |

#### [capstone#final-prep] Fifteen minutes: open your repository as a stranger would

*Before the first meeting*

Open the public link in a private window. Are the four documents there, and could the board read your statement alone?

#### [capstone#now-presenting] Review meeting

*Now chairing*

#### [capstone#review] What the room learned

*After the meetings*

- **The clearest pack.** Whose quality statement could the board read without a question?
- **The flaw most missed.** Which seeded flaw went unrated or rated low most often?
- **The best chairing.** Who held a finding under pressure and still left the sponsor with a way forward?

#### [capstone#what-next] The follow-up task, and what comes next

*After the course*

- **Follow-up task.** Within six weeks, apply your checklist to one real analysis in your unit with a second reviewer, and bring the agreement table and the sentence you changed; keep personal and restricted data out of anything you share.
- **Keep the repository.** It is evidence for the DS Expert badge.
- **Back to the start.** Reviewing one analysis in depth is DS-310; send your new analysts there.

#### [capstone#thanks] Thank you

*SDAIA Academy*

Leading Analytical Work: Review, Standards and Stakeholders
