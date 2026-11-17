---
course: "Leading Analytical Work: Review, Standards and Stakeholders"
code: "DS-407"
version: "2027.1.0"
deck: "day3"
day: 3
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/ds-407/slides/day3.html"
---

# Leading Analytical Work: Review, Standards and Stakeholders

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
