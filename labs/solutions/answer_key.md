# Answer key for trainers: DS-407 on the Ras Sahil case

All data is synthetic, written by `prepare_data.py` (seed 407; each data section has its own random stream, so a
change in one section leaves the others as they are). The numbers below are those of the solution runs.

## Day 1

**Lab 1.1 · Six requests, four levels** (`data/requests.json`, `data/faleh_grades.json`)
- Planted: 10 of 30 logged requests are under-assured by the reference matrix (R03, R04, R05, R07, R13, R18, R21, R24,
  R29, R30); 5 of them had an error after release, against 1 of the other 20. R07 and R19 have the same profile and
  got level 1 and level 3.
- Reference levels of the new requests: N1 2, N2 3, N3 4, N4 3, N5 1 (plus the data protection officer's check),
  N6 3. The solution reaches 6 of 6 with Faleh; the check passes at 5.
- Common trap: N4 graded level 2 (the public escalator forgotten); N5 graded 2 for personal data.

**Lab 1.2 · A checklist adapted from REFORMS** (`data/reforms_items.json`: our paraphrase, REFORMS ids kept)
- The 32 items map to data 15, method 9, inference 5, question fit 3, communication 0.
- Solution: 12 items (11 plus the privacy item), drawing on 18 REFORMS items; 6 apply at level 1, 11 from level 2,
  12 at level 3. The reference with the assisted-work item is `data/reference/checklist.json` (13 items).

**Lab 1.3 · Re-run Saleh's repository** (`data/repos/cargo_dwell/`)
- Planted failures, in the order they appear: an absolute path to a personal folder (path); README names
  `containers.csv`, the file is `containers_q3.csv` (documentation); `data/berth_lookup.csv` missing (missing input);
  `DataFrame.append`, removed in pandas 2, with no version pinned (library version); an unseeded sample of 2,000
  (randomness, two runs give two figures); transshipment kept with imports while the report removed it by hand
  (manual step).
- Re-run before the last fix: 5.18 days. After filtering imports in code: 4.60, the reported figure.

**Lab 1.4 · Rules for assisted work** (`data/guidelines_digest.json`, `data/scenarios.json`)
- Reference decisions: S1 allowed; S2 breach C1 (restricted roster); S3 breach D1 (no disclosure); S4 needs action
  K1, K2; S5 breach V1 (unchecked 18%); S6 allowed; S7 needs action U1 (the stretch rule); S8 breach C2 (unapproved
  tool). The reference rule set has 176 words.

## Day 2

**Lab 2.1 · Two reviewers, one analysis** (`data/repos/berth_delay/`)
- Seeded flaws and reference severities: C1 no baseline (3); C2 diverted calls dropped, 17 before and 35 after at T2,
  33 of them feeders (2); M1 "halved" against a printed 42% reduction (2); M2 weather closures in T2's before period
  (1); m1 minutes label on hours (1); P1 vessel masters' names and mobile numbers in table 5 (3, by the standard).
- Faleh's ratings: C1 3, C2 3, M1 2, M2 2, m1 1, P1 1. Agreement 50%, weighted kappa 0.25; the gap of two is P1.
- Headline by fixes: none -5.36 h (extend); C1 -1.37; C1 and C2 -0.94; C1, C2 and M2 -0.78 (do not extend as it is).

**Lab 2.2 · Audit five assisted analyses** (`data/assisted_log.json`)
- Breaches: A1 none; A2 C1 (restricted data); A3 V1 and K2 (claims 18.4%, the data give 47.7%); A4 D1 (no
  disclosure on a board paper); A5 K1 and K2 (no prompts, no record).

**Lab 2.3 · Feedback and a three-month plan** (`data/shaden_review.json`, `data/analysts.json`)
- Raise F2, F1, F7 (a missing comparison group, the wrong population in an average, unverified assisted cells).
  Her profile: methods, inference and assisted-work verification at 1 of 4. The plan keeps unaided work in month 3.

**Lab 2.4 · A quarter's review rota** (`data/pipeline_q1.json`)
- 40 analyses: 10 at level 1, 14 at level 2, 12 at level 3, 4 at level 4. Senior hours needed 184, available 150:
  short by 34. Five co-signed level 3 reviews (8 hours saved each) close it. The reference rota is in
  `data/reference/rota.json`; Faleh and Saleh end at 100% of their review hours.

## Day 3

**Lab 3.1 · A result in a week** (`data/inventory.json`, `data/roles.json`)
- Days with review: Q-a 2.5, Q-b 1.5, Q-c 1.5, Q-d 8, Q-e 5. The constraint changes on the fourth message: four
  working days and the feeder question. Option B (Q-a and Q-b, 4.0 days) answers both.

**Lab 3.2 · An analysis agreement**
- Minimum detectable change of the difference in differences: 1.13 h with 3 months after, 0.84 with 6, 0.66 with 12.
  Threshold 2.0 h. The estimate, shown only after signing: -0.78 h (standard error 0.236); feeders +6.32 h, other
  types -2.88 h. The rule's two conditions both fail: keep at T2, fix the feeder slots.

**Lab 3.3 · Drop the feeder result?** (`data/khaled_request.md`, `data/unit_standard.md`)
- 278 feeder calls at T2 after the change, 33 diverted. Decision: keep the table with context (S-7, S-8; Fairness,
  Transparency & Explainability, Accountability & Responsibility).

**Lab 3.4 · A quality statement and a correction** (`data/containers_q2_released.csv`)
- Weeks 5 and 6 loaded twice: 1,080 duplicated rows. Released Q2 mean import dwell 4.07 days; corrected 4.32.

## Capstone (`capstone/data/`, practice version)
- `staffing.py` divides the mean of 10.7 night jobs by 3 jobs a pilot and recommends 4 pilots in place of 6.
- Planted: the mean in place of the busy nights (95th percentile 18 jobs); the tanker season (nights 150 to 210,
  mean 15.4 jobs) averaged away; "3 jobs a pilot" with no regard to job hours (mean 2.7 hours a job); a safety use
  that needs level 4; no decision rule and no uncertainty. The assessed variants are the trainer's and are not
  published.
