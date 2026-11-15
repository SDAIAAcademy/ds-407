<!-- academy:title -->
# Leading Analytical Work: Review, Standards and Stakeholders

قيادة العمل التحليلي: المراجعة والمعايير وأصحاب المصلحة

Data Science Track · SDAIA Academy · DS-407 · Level 400

REPLACE: one line under the title: what participants can do after the course

Participants lead the analytics unit of the fictional Ras Sahil Ports Authority: twelve analysts whose work increasingly starts as an assistant's draft. They write a proportionate quality-assurance standard and review checklist, re-run and review colleagues' analyses, set the unit's rules for AI-assisted work, turn review findings into feedback, and negotiate scope, deadline and evidence with role-played sponsors, one of whom asks for an unfavourable result to be dropped. DS-310 teaches reviewing one analysis; this course sets the standards and runs the system.

**Format:** Intensive: 3 teaching days of four sessions and a capstone day, with guided pre-work and a tracked follow-up task

**Course page:** https://sdaiaacademy.github.io/ds-407/
<!-- /academy:title -->

## Outcomes

| | Outcomes | Level | Evidence |
|---|---|---|---|
| LO1 | Design a proportionate quality-assurance standard for analytical work, with assurance levels, a review checklist and sign-off rules, given the unit's log of 30 requests with their uses and risks | Performance | a standard with which a peer, working independently, assigns the same assurance levels to six new requests |
| LO2 | Review analyses by others, including assistant-drafted ones, rank findings by their effect on the decision and calibrate severity with a second reviewer, given three seeded-flaw analysis repositories | Performance | review notes that find the seeded critical flaws, and a severity agreement table with the second reviewer |
| LO3 | Design rules for AI-assisted analysis covering verification, disclosure and the process evidence each analyst keeps, and audit the unit's work against them, given the national generative AI guidelines and a log of the unit's assisted analyses | Performance | a one-page rule set and an audit of five assisted analyses against it |
| LO4 | Prepare feedback and a development plan for an analyst from review findings, given a reviewed notebook and the analyst's skills profile | Applied | a feedback note and three-month plan that a peer judges specific |
| LO5 | Lead a negotiation with a sponsor on scope, deadline and evidence threshold and record the agreement, given a role-played sponsor whose constraints change during the meeting | Performance | an analysis agreement and an observer's rubric score |
| LO6 | Decide how to respond to pressure to change or suppress a finding, and record the reasons, given a scripted request to remove an unfavourable subgroup result | Performance | a decision record citing the unit's standard and the ethics principles |

<!-- academy:units -->
## Units

| Unit | Title | Sessions | Slides |
|---|---|---|---|
| Day 1 | Set the standard | Assurance proportionate to risk; A team review checklist; Reproducibility as a team rule; Rules for AI-assisted analysis | [`slides/day1.html`](slides/day1.html) |
| Day 2 | Review and develop | Calibrating reviewers; Auditing assisted work; Feedback that builds skill; Review capacity and mentoring | [`slides/day2.html`](slides/day2.html) |
| Day 3 | Work with sponsors | Scope and deadline; Agreeing the evidence first; Pressure on a finding; Reporting quality and correcting errors | [`slides/day3.html`](slides/day3.html) |
| Capstone | Capstone project presentations |  | [`slides/capstone.html`](slides/capstone.html) |
<!-- /academy:units -->

## Case study

**REPLACE: the name of the fictional organisation every lab works on.** REPLACE: two sentences on the case study and its synthetic data

<!-- academy:labs -->
## Labs

Every lab is a notebook in `labs/`. Open it in Google Colab from the course page, or run it locally with `uv`. Exercises raise `NotImplementedError` until they are done; the reference versions are in `labs/solutions/`.

| | Session | Lab | File |
|---|---|---|---|
| 1.1 | Day 1 · Session 1 | Grade six requests by risk and complexity and assign an assurance level to each | [`D1_1_grade_six_requests.ipynb`](labs/D1_1_grade_six_requests.ipynb) |
| 1.2 | Day 1 · Session 2 | Draft a checklist from question to conclusion by adapting a published reproducibility checklist | [`D1_2_draft_checklist_from.ipynb`](labs/D1_2_draft_checklist_from.ipynb) |
| 1.3 | Day 1 · Session 3 | Re-run a colleague's analysis from its repository and record every step that failed | [`D1_3_re_run_colleague.ipynb`](labs/D1_3_re_run_colleague.ipynb) |
| 1.4 | Day 1 · Session 4 | Write what analysts must verify, disclose and keep as evidence when an assistant drafts work | [`D1_4_write_what_analysts.ipynb`](labs/D1_4_write_what_analysts.ipynb) |
| 2.1 | Day 2 · Session 1 | Review a seeded-flaw berth-delay analysis independently with a partner, compare severity ratings and revise the checklist where you disagree | [`D2_1_review_seeded_flaw.ipynb`](labs/D2_1_review_seeded_flaw.ipynb) |
| 2.2 | Day 2 · Session 2 | Check five assistant-drafted analyses from the unit's log against the rules for AI-assisted work and record each breach | [`D2_2_check_five_assistant.ipynb`](labs/D2_2_check_five_assistant.ipynb) |
| 2.3 | Day 2 · Session 3 | Turn review findings into feedback and a three-month plan for a new analyst | [`D2_3_turn_review_findings.ipynb`](labs/D2_3_turn_review_findings.ipynb) |
| 2.4 | Day 2 · Session 4 | Plan a quarter's review load and pairings for a team of twelve | [`D2_4_plan_quarter_s.ipynb`](labs/D2_4_plan_quarter_s.ipynb) |
| 3.1 | Day 3 · Session 1 | Role-play a sponsor who wants a result in a week and agree what can be answered | [`D3_1_role_play_sponsor.ipynb`](labs/D3_1_role_play_sponsor.ipynb) |
| 3.2 | Day 3 · Session 2 | Write an analysis agreement: question, decision rule and evidence threshold | [`D3_2_write_analysis_agreement.ipynb`](labs/D3_2_write_analysis_agreement.ipynb) |
| 3.3 | Day 3 · Session 3 | Handle a scripted request to drop an unfavourable subgroup and record the decision | [`D3_3_handle_scripted_request.ipynb`](labs/D3_3_handle_scripted_request.ipynb) |
| 3.4 | Day 3 · Session 4 | Draft a board-paper quality statement (what was checked, by whom, what remains uncertain) and a correction notice for an error found after release | [`D3_4_draft_board_paper.ipynb`](labs/D3_4_draft_board_paper.ipynb) |
<!-- /academy:labs -->

## Capstone

A quality-assurance pack for one high-risk analysis (applied standard, review report, analysis agreement, board quality statement), submitted as a repository, followed by a fifteen-minute review meeting the participant chairs with a role-played analyst and sponsor

**Submission:** REPLACE: what participants submit and how: a public repository link, or a shared folder for a course without code

## Prerequisites

- DS-310 Problem Framing and Analytical Review
- Has reviewed an analysis written by someone else and written comments the author acted on
- Uses version control for analysis code

<!-- academy:tools -->
## Tools

Each line is a capability; the examples are interchangeable.

- **Notebooks and reports:** Jupyter, marimo, Quarto
- **Code and document review:** pull or merge requests on GitHub or GitLab, comments in a shared document
- **Reproducible environments:** uv with a lock file, containers
- **Assistant whose output is reviewed:** a free hosted open-weight model, the assistant the participant's unit already uses
<!-- /academy:tools -->

<!-- academy:sources -->
## Sources

- REPLACE: every source the course cites, with its address, in course.json under "sources"; this list is written from there
<!-- /academy:sources -->

### National references

- SDAIA Generative AI Guidelines for Government: REPLACE: the address of the official text
- SDAIA AI Ethics Principles: REPLACE: the address of the official text
- Personal Data Protection Law and its implementing regulations: REPLACE: the address of the official text
- NDMO Data Classification Policy: REPLACE: the address of the official text
