---
course: "Leading Analytical Work: Review, Standards and Stakeholders"
code: "DS-407"
version: "2027.1.0"
deck: "capstone"
day: 4
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/ds-407/slides/capstone.html"
---

# Leading Analytical Work: Review, Standards and Stakeholders

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
