---
course: "Leading Analytical Work: Review, Standards and Stakeholders"
code: "DS-407"
version: "2027.1.0"
deck: "day2"
day: 2
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/ds-407/slides/day2.html"
---

# Leading Analytical Work: Review, Standards and Stakeholders

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
