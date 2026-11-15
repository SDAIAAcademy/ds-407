<!-- academy:title -->
# Leading Analytical Work: Review, Standards and Stakeholders

قيادة العمل التحليلي: المراجعة والمعايير وأصحاب المصلحة

Data Science Track · SDAIA Academy · DS-407 · Level 400

Set the unit's quality standard, run review as a system, and hold the line on evidence with sponsors

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
| Capstone | Capstone: the staffing pack and the review meeting |  | [`slides/capstone.html`](slides/capstone.html) |
<!-- /academy:units -->

## Case study

**Ras Sahil Ports Authority.** Ras Sahil Ports Authority is a fictional Gulf-coast port authority whose analytics unit of twelve analysts serves marine operations, commercial affairs, finance and staffing, with more and more work starting as a draft by Musawwada, the unit's drafting assistant. Participants, as the unit's head, write the assurance standard from a log of 30 requests, adapt a published checklist, re-run a colleague's cargo-dwell repository, set rules for assisted work and audit five assisted analyses, calibrate severity with a second reviewer on a seeded-flaw berth-delay analysis, write feedback and a review rota, and negotiate scope, evidence and a pressured subgroup finding with two role-played sponsors. The capstone is the quality-assurance pack for the marine pilot staffing analysis. All data is synthetic and generated with a fixed seed.

The people: Arjwan Al-Huqail, head of the analytics unit (the participant's role); Faleh Al-Musharraf and Saleh Al-Ghamlas, senior analysts; Shaden Al-Ruwayshid, a new analyst; Bader Al-Khayyal, director of marine operations, and Khaled Al-Kharji, deputy chief executive for commercial affairs, the two sponsors; Hanin Al-Mughira, data protection officer. All are invented.

<!-- academy:labs -->
## Labs

Every lab is a notebook in `labs/`. Open it in Google Colab from the course page, or run it locally with `uv`. Exercises raise `NotImplementedError` until they are done; the reference versions are in `labs/solutions/`.

| | Session | Lab | File |
|---|---|---|---|
| 1.1 | Day 1 · Session 1 | Six requests, four levels | [`D1_1_assurance_levels.ipynb`](labs/D1_1_assurance_levels.ipynb) |
| 1.2 | Day 1 · Session 2 | A checklist adapted from REFORMS | [`D1_2_team_checklist.ipynb`](labs/D1_2_team_checklist.ipynb) |
| 1.3 | Day 1 · Session 3 | Re-run Saleh's repository | [`D1_3_rerun_repository.ipynb`](labs/D1_3_rerun_repository.ipynb) |
| 1.4 | Day 1 · Session 4 | Rules for assisted work | [`D1_4_ai_rules.ipynb`](labs/D1_4_ai_rules.ipynb) |
| 2.1 | Day 2 · Session 1 | Two reviewers, one analysis | [`D2_1_calibrate_reviewers.ipynb`](labs/D2_1_calibrate_reviewers.ipynb) |
| 2.2 | Day 2 · Session 2 | Audit five assisted analyses | [`D2_2_audit_assisted.ipynb`](labs/D2_2_audit_assisted.ipynb) |
| 2.3 | Day 2 · Session 3 | Feedback and a three-month plan | [`D2_3_feedback_plan.ipynb`](labs/D2_3_feedback_plan.ipynb) |
| 2.4 | Day 2 · Session 4 | A quarter's review rota | [`D2_4_review_capacity.ipynb`](labs/D2_4_review_capacity.ipynb) |
| 3.1 | Day 3 · Session 1 | A result in a week | [`D3_1_scope_deadline.ipynb`](labs/D3_1_scope_deadline.ipynb) |
| 3.2 | Day 3 · Session 2 | An analysis agreement | [`D3_2_analysis_agreement.ipynb`](labs/D3_2_analysis_agreement.ipynb) |
| 3.3 | Day 3 · Session 3 | Drop the feeder result? | [`D3_3_pressure_finding.ipynb`](labs/D3_3_pressure_finding.ipynb) |
| 3.4 | Day 3 · Session 4 | A quality statement and a correction | [`D3_4_quality_correction.ipynb`](labs/D3_4_quality_correction.ipynb) |
<!-- /academy:labs -->

## Capstone

A quality-assurance pack for one high-risk analysis (applied standard, review report, analysis agreement, board quality statement), submitted as a repository, followed by a fifteen-minute review meeting the participant chairs with a role-played analyst and sponsor

**Submission:** A public GitHub repository link holding the pack (the applied standard, the review report, the analysis agreement and the board quality statement) with its commit history; then a fifteen-minute review meeting the participant chairs with a role-played analyst and sponsor, observed against a rubric.

The brief and the practice version of the analysis are in [`labs/capstone/`](labs/capstone/README.md). The capstone pack is 50% of the assessment, the chaired meeting 30% and a supervised review without AI assistance 20%; passing is 70% overall and at least 60% on each component.

## How the course runs

Three teaching days of four 50-minute sessions: about 20 minutes of concepts, a checkpoint, then a 25-minute lab that produces one part of the unit's quality system. Day 1 sets the standard, Day 2 runs review and develops analysts, Day 3 works with sponsors. Day 2's first-pass review is done without AI assistance, so that each reviewer forms a judgement before comparing it. The role-plays use the trainer or a peer, with scripted stand-ins for practice alone.

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

### Analytical quality assurance

- [HM Government Analysis Function: The AQuA Book, guidance on producing quality analysis for government (2025 edition)](https://www.gov.uk/guidance/the-aqua-book)
- [Kapoor et al. (2024): REFORMS, consensus-based recommendations for machine-learning-based science, Science Advances](https://doi.org/10.1126/sciadv.adk3452)
- [REFORMS checklist and guidelines](https://reforms.cs.princeton.edu/)

### Review and agreement

- [Cohen (1968): Weighted kappa, Psychological Bulletin 70(4)](https://doi.org/10.1037/h0026256)

### National references

- [SDAIA: Generative AI Guidelines for Government](https://sdaia.gov.sa/en/SDAIA/about/Files/GenAIGuidelinesForGovernmentENCompressed.pdf)
- [SDAIA: AI Ethics Principles](https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf)
- [Personal Data Protection Law](https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf)
- [Implementing Regulation of the Personal Data Protection Law](https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulationPersonalDataProtectionLaw.pdf)
- [NDMO: Data Classification Policy](https://sdaia.gov.sa/en/SDAIA/about/Documents/DataClassificationPolicy.pdf)
<!-- /academy:sources -->

### National references

- SDAIA Generative AI Guidelines for Government: <https://sdaia.gov.sa/en/SDAIA/about/Files/GenAIGuidelinesForGovernmentENCompressed.pdf>
- SDAIA AI Ethics Principles: <https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf>
- Personal Data Protection Law: <https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf>, and its Implementing Regulation: <https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulationPersonalDataProtectionLaw.pdf>
- NDMO Data Classification Policy: <https://sdaia.gov.sa/en/SDAIA/about/Documents/DataClassificationPolicy.pdf>

The official texts were opened for this course; the slides paraphrase them and name the section used. SDAIA lists all of its regulations and guidelines at <https://sdaia.gov.sa/en/SDAIA/about/Pages/RegulationsAndPolicies.aspx>.
