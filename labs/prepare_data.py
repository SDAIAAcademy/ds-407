# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=2.0", "pandas>=2.2"]
# ///
"""Write the synthetic data of Ras Sahil Ports Authority into labs/data/ (seed 407).

Everything here is invented: the authority, its people, its vessels and every number. The same files come out on
every run. The planted problems and the numbers each lab's solution should print are in solutions/answer_key.md.

    uv run python prepare_data.py
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 407
LABS = Path(__file__).resolve().parent
DATA = LABS / "data"
REPOS = DATA / "repos"
REF = DATA / "reference"
CAP = LABS / "capstone" / "data"

MATRIX = {"low": {"low": 1, "medium": 1, "high": 2},
          "medium": {"low": 2, "medium": 2, "high": 3},
          "high": {"low": 3, "medium": 3, "high": 4}}


def required_level(effect: str, complexity: str, public: bool, safety: bool) -> int:
    lvl = MATRIX[effect][complexity]
    if public or safety:
        lvl += 1
    return min(lvl, 4)


def wjson(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def wtext(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


# ---------------------------------------------------------------------------------------------- 1 · request log
LOG = [
    # id, title, requester, use, effect, complexity, public, safety, personal, level_given, error_after_release
    ("R01", "Monthly berth occupancy by terminal", "Marine operations", "operations dashboard", "low", "low", False, False, False, 1, False),
    ("R02", "Tug fuel use per vessel call", "Marine services", "internal note", "low", "low", False, False, False, 1, False),
    ("R03", "Revenue effect of the storage-fee change", "Commercial affairs", "board paper", "high", "medium", False, False, False, 1, True),
    ("R04", "Quarterly cargo throughput for the public bulletin", "Communications", "public statistic", "medium", "low", True, False, False, 2, True),
    ("R05", "Pilot boarding delays by hour band", "Marine operations", "roster decision", "medium", "medium", False, True, False, 2, False),
    ("R06", "Staff overtime by department", "Human resources", "internal note", "low", "low", False, False, True, 1, False),
    ("R07", "Crane breakdown frequency by crane", "Engineering", "maintenance budget", "medium", "medium", False, False, False, 1, False),
    ("R08", "Forecast of container volumes for the new yard", "Planning", "capital investment", "high", "high", False, False, False, 4, False),
    ("R09", "Customer complaint themes", "Customer services", "internal note", "low", "medium", False, False, True, 1, False),
    ("R10", "Berth productivity league table for terminal operators", "Commercial affairs", "contract penalties", "high", "medium", False, False, False, 3, False),
    ("R11", "Average truck turnaround at the gates", "Gate operations", "public statistic", "medium", "low", True, False, False, 3, False),
    ("R12", "Tariff benchmark against three regional ports", "Commercial affairs", "board paper", "high", "medium", False, False, False, 3, False),
    ("R13", "Night-shift pilot workload", "Marine operations", "fatigue rule", "high", "medium", False, True, True, 2, True),
    ("R14", "Energy use of reefer stacks", "Engineering", "internal note", "low", "medium", False, False, False, 1, False),
    ("R15", "Vessel waiting time for the annual report", "Communications", "public statistic", "medium", "medium", True, False, False, 3, False),
    ("R16", "Dredging volumes against plan", "Engineering", "contract payment", "medium", "low", False, False, False, 2, False),
    ("R17", "Customs inspection rates by commodity", "Commercial affairs", "internal note", "low", "medium", False, False, False, 1, False),
    ("R18", "Safety incidents per million working hours", "Health and safety", "regulator return", "high", "low", True, True, True, 2, True),
    ("R19", "Crane downtime by crane and shift", "Engineering", "maintenance budget", "medium", "medium", False, False, False, 3, False),
    ("R20", "Ship-to-shore crane moves per hour", "Marine operations", "operations dashboard", "low", "low", False, False, False, 1, False),
    ("R21", "Model of berth demand for the next five years", "Planning", "capital investment", "high", "high", False, False, False, 3, True),
    ("R22", "Training hours per employee", "Human resources", "internal note", "low", "low", False, False, True, 1, False),
    ("R23", "Port dues collected against invoices", "Finance", "audit response", "high", "low", False, False, False, 3, False),
    ("R24", "Survey of shipping agents' satisfaction", "Customer services", "public statistic", "medium", "medium", True, False, True, 2, False),
    ("R25", "Tug allocation rule for large tankers", "Marine services", "safety procedure", "high", "medium", False, True, False, 4, False),
    ("R26", "Gate appointment no-show rates", "Gate operations", "internal note", "low", "low", False, False, False, 1, False),
    ("R27", "Fee waiver cost for the feeder service", "Commercial affairs", "board paper", "high", "low", False, False, False, 3, True),
    ("R28", "Yard occupancy heat map", "Terminal planning", "operations dashboard", "low", "medium", False, False, False, 1, False),
    ("R29", "Cargo dwell time for the ministry's indicators", "Planning", "public statistic", "medium", "low", True, False, False, 1, False),
    ("R30", "Water depth survey summary for pilots", "Marine services", "navigation notice", "medium", "medium", False, True, False, 2, False),
]

NEW = [
    {"id": "N1", "title": "Weekly berth occupancy for the tug roster meeting",
     "detail": "A count of berth hours by terminal, from the berth system. The tug supervisor uses it to set next week's roster.",
     "use": "roster decision", "personal_data": False},
    {"id": "N2", "title": "Revenue estimate of a proposed tariff change",
     "detail": "Applies the new tariff to last year's calls and adjusts for two shipping lines that may move. Goes to the board.",
     "use": "board paper", "personal_data": False},
    {"id": "N3", "title": "Arrival-delay model to allocate marine pilots at night",
     "detail": "A model of vessel arrival delays, from AIS and berth data, sets how many pilots stand by on the night shift.",
     "use": "safety staffing", "personal_data": False},
    {"id": "N4", "title": "Average cargo dwell for the annual public statistics",
     "detail": "Mean import dwell by quarter from the terminal operating system; published in the authority's statistics.",
     "use": "public statistic", "personal_data": False},
    {"id": "N5", "title": "Staff survey summary for human resources",
     "detail": "Counts and themes from the annual staff survey, 640 responses, with department and grade.",
     "use": "internal note", "personal_data": True},
    {"id": "N6", "title": "Evaluation of the berth-allocation pilot: continue or stop",
     "detail": "Compares waiting at terminal T2, where slot booking started in month 13, with the other terminals.",
     "use": "board decision", "personal_data": False},
]
# The second reviewer's (Faleh Al-Musharraf's) grades of the six new requests, made with the reference standard
FALEH_GRADES = {
    "N1": {"effect": "medium", "complexity": "low", "public": False, "safety": False},
    "N2": {"effect": "high", "complexity": "medium", "public": False, "safety": False},
    "N3": {"effect": "high", "complexity": "high", "public": False, "safety": True},
    "N4": {"effect": "medium", "complexity": "low", "public": True, "safety": False},
    "N5": {"effect": "low", "complexity": "medium", "public": False, "safety": False},
    "N6": {"effect": "high", "complexity": "medium", "public": False, "safety": False},
}

LEVELS = {
    "1": {"name": "Self-check", "assurer": "the analyst, with the checklist", "approver": "the requester's manager", "rerun": "by the analyst"},
    "2": {"name": "Peer review", "assurer": "another analyst of the unit", "approver": "a senior analyst", "rerun": "by the reviewer"},
    "3": {"name": "Independent review", "assurer": "a senior analyst who did not take part", "approver": "the head of the unit", "rerun": "by the reviewer, from the repository"},
    "4": {"name": "Independent review and second opinion", "assurer": "a senior analyst plus a second reviewer outside the team", "approver": "the head of the unit and the requesting director", "rerun": "by both reviewers"},
}


def write_requests():
    log = []
    for (rid, title, req, use, eff, cx, pub, saf, pers, given, err) in LOG:
        log.append({"id": rid, "title": title, "requester": req, "use": use, "effect": eff, "complexity": cx,
                    "public": pub, "safety": saf, "personal_data": pers, "level_given": given, "error_after_release": err})
    wjson(DATA / "requests.json", {"log": log, "new": NEW, "levels": LEVELS})
    wjson(DATA / "faleh_grades.json", FALEH_GRADES)
    under = [r for r in log if r["level_given"] < required_level(r["effect"], r["complexity"], r["public"], r["safety"])]
    wjson(REF / "assurance.json", {
        "matrix": MATRIX, "escalators": {"public": 1, "safety": 1}, "max_level": 4,
        "grades": FALEH_GRADES,
        "levels": {k: required_level(**v) for k, v in FALEH_GRADES.items()},
        "under_assured": [r["id"] for r in under],
    })
    return log, under


# ---------------------------------------------------------------------------------------------- 2 · REFORMS items
REFORMS = [  # our short paraphrase of each REFORMS item (Kapoor et al. 2024); module numbers as published
    ("1a", "Study goals", "The population or setting the claim is about"),
    ("1b", "Study goals", "Why that population or setting was chosen"),
    ("1c", "Study goals", "Why a machine-learning method is used at all"),
    ("2a", "Computational reproducibility", "The datasets used, with a way to identify the exact version"),
    ("2b", "Computational reproducibility", "The code that produces every result, with its exact version"),
    ("2c", "Computational reproducibility", "The computing environment: hardware, system, packages and versions"),
    ("2d", "Computational reproducibility", "A README that says how to produce the results"),
    ("2e", "Computational reproducibility", "One script that reproduces all reported results"),
    ("3a", "Data quality", "Where the data come from and when, and how labels were made"),
    ("3b", "Data quality", "The frame the data are drawn from"),
    ("3c", "Data quality", "Why the data suit the task"),
    ("3d", "Data quality", "How the outcome is defined, with its descriptive statistics"),
    ("3e", "Data quality", "How many records there are"),
    ("3f", "Data quality", "How much is missing, and where"),
    ("3g", "Data quality", "Why the data represent the population of the claim"),
    ("4a", "Data preprocessing", "Which records were excluded, and why"),
    ("4b", "Data preprocessing", "How impossible or corrupt records were handled"),
    ("4c", "Data preprocessing", "Every transformation from raw data to the analysed data"),
    ("5a", "Modelling", "Every model fitted, with its features and loss"),
    ("5b", "Modelling", "Why these kinds of model were chosen"),
    ("5c", "Modelling", "How models were evaluated: splits and validation"),
    ("5d", "Modelling", "How the reported model was selected"),
    ("5e", "Modelling", "How hyperparameters were tuned"),
    ("5f", "Modelling", "That comparisons are made against fair baselines"),
    ("6a", "Data leakage", "That preprocessing and modelling use only training information"),
    ("6b", "Data leakage", "How duplicates and dependencies between training and test data were handled"),
    ("6c", "Data leakage", "That every feature is legitimate for the task"),
    ("7a", "Metrics and uncertainty", "The metrics used, and why they fit the question"),
    ("7b", "Metrics and uncertainty", "Uncertainty estimates and how they were computed"),
    ("7c", "Metrics and uncertainty", "Why the statistical tests fit, with their assumptions checked"),
    ("8a", "Generalisability and limitations", "Evidence that the result holds outside the data"),
    ("8b", "Generalisability and limitations", "Where the result is not expected to hold"),
]

AREAS = ["question fit", "data", "method", "inference", "communication"]

CHECKLIST_REF = [
    {"id": "Q1", "area": "question fit", "from": ["1a"], "item": "Does the analysis answer the decision question in the agreement, for the population it names?", "evidence": "the agreement and the headline cell", "min_level": 1},
    {"id": "Q2", "area": "question fit", "from": [], "item": "Is the decision rule written down before the results, and is the result read against it?", "evidence": "the dated agreement", "min_level": 2},
    {"id": "D1", "area": "data", "from": ["2a", "3a"], "item": "Are the data sources and extract dates recorded, so the same files can be found again?", "evidence": "the data manifest", "min_level": 1},
    {"id": "D2", "area": "data", "from": ["4a", "3f"], "item": "Are excluded and missing records counted, with the reason for each exclusion?", "evidence": "a count per exclusion step", "min_level": 1},
    {"id": "D3", "area": "data", "from": ["6b"], "item": "Have duplicates been looked for, and removed or explained?", "evidence": "the duplicate count", "min_level": 2},
    {"id": "R1", "area": "data", "from": ["2b", "2c", "2d", "2e"], "item": "Does the analysis re-run from the repository, with the lock file and the README alone, to the reported numbers?", "evidence": "the re-run log", "min_level": 2},
    {"id": "M1", "area": "method", "from": ["5f"], "item": "Is the comparison fair: a baseline, a control group, the same period?", "evidence": "the comparison cell", "min_level": 1},
    {"id": "M2", "area": "method", "from": ["5c", "6a", "6c"], "item": "For a model: is it tested on data it never saw, with only legitimate features?", "evidence": "the split and the feature list", "min_level": 3},
    {"id": "I1", "area": "inference", "from": ["7b"], "item": "Is uncertainty stated for every number the decision depends on?", "evidence": "an interval or a range", "min_level": 2},
    {"id": "I2", "area": "inference", "from": ["3g", "8a", "8b"], "item": "Are the groups and conditions where the result does not hold named?", "evidence": "the subgroup table", "min_level": 2},
    {"id": "C1", "area": "communication", "from": [], "item": "Does every number in the text match the output it comes from?", "evidence": "each number traced to a cell", "min_level": 1},
    {"id": "C2", "area": "communication", "from": [], "item": "Is any part drafted by an assistant disclosed, and was each of its numbers re-run?", "evidence": "the disclosure line and the verification record", "min_level": 1},
    {"id": "P1", "area": "communication", "from": [], "item": "Before anything leaves the unit: is it free of personal data, and is its classification marked and respected?", "evidence": "the classification mark and a scan of the output", "min_level": 1, "privacy": True},
]


def write_reforms():
    wjson(DATA / "reforms_items.json", [{"id": i, "module": m, "item": t} for i, m, t in REFORMS])
    wjson(REF / "checklist.json", CHECKLIST_REF)


# ---------------------------------------------------------------------------------------------- 3 · berth calls
TERMINALS = ["T1", "T2", "T3", "T4"]
TYPES = ["container", "bulk", "tanker", "feeder", "ro-ro"]
FIRST = ["Abdullah", "Mohammed", "Omar", "Rashid", "Hamdan", "Juma", "Ali", "Yousef", "Ibrahim", "Salem", "Karim",
         "Daniel", "Arjun", "Mikhail", "Luca", "Chen", "Ravi", "Tomas"]
LAST = ["Al-Bahri", "Al-Marzouqi", "Al-Saadi", "Al-Hinai", "Al-Rumaithi", "Suleiman", "Haddad", "Novak", "Rossi",
        "Kumar", "Wei", "Petrov", "Santos", "Menon", "Farouk", "Al-Kaabi"]


def write_berth(rng):
    rows = []
    base = {"T1": 12.0, "T2": 8.0, "T3": 14.0, "T4": 11.0}
    tadj = {"container": 0.0, "bulk": 2.0, "tanker": 1.0, "feeder": -1.0, "ro-ro": -2.0}
    cid = 0
    for month in range(1, 25):
        n = 400
        terms = rng.choice(TERMINALS, size=n, p=[0.3, 0.25, 0.25, 0.2])
        types = rng.choice(TYPES, size=n, p=[0.38, 0.2, 0.15, 0.22, 0.05])
        noise = rng.gamma(2.0, 3.0, size=n)
        storm = rng.random(n) < (0.35 if month in (3, 4) else 0.0)
        for i in range(n):
            t, v = terms[i], types[i]
            w = base[t] + tadj[v] + noise[i] - 4.0
            if month >= 13:
                w -= 1.5
                if t == "T2":
                    w += 6.0 if v == "feeder" else -3.0
            if storm[i]:
                w += 10.0
            w = max(0.2, w)
            cid += 1
            rows.append({"call_id": f"C{cid:05d}", "month": month, "terminal": t, "vessel_type": v,
                         "wait_h": round(float(w), 1), "weather_closure": int(storm[i]),
                         "master_name": f"{FIRST[rng.integers(len(FIRST))]} {LAST[rng.integers(len(LAST))]}",
                         "master_mobile": f"+966-50-{rng.integers(100, 999)}-{rng.integers(1000, 9999)}"})
    df = pd.DataFrame(rows)
    # Long waits make a vessel divert to another port: its wait is never recorded
    small = df.vessel_type == "feeder"
    p_div = np.where(small, np.clip((df.wait_h - 14.0) / 12.0, 0, 0.8), np.clip((df.wait_h - 24.0) / 20.0, 0, 0.8))
    div = rng.random(len(df)) < p_div
    df["diverted"] = div.astype(int)
    df.loc[div, "wait_h"] = np.nan
    df.to_csv(DATA / "berth_calls.csv", index=False, lineterminator="\n")
    return df


def did(df, group_mask=None, exclude_storm=True, fill_diverted=None):
    d = df.copy()
    if group_mask is not None:
        d = d[group_mask(d)]
    if exclude_storm:
        d = d[d.weather_closure == 0]
    if fill_diverted is not None:
        d["wait_h"] = d.wait_h.fillna(fill_diverted)
    else:
        d = d.dropna(subset=["wait_h"])
    after = d.month >= 13
    t2 = d.terminal == "T2"
    m = lambda a, b: float(d[a & b].wait_h.mean())
    return (m(t2, after) - m(t2, ~after)) - (m(~t2, after) - m(~t2, ~after))


SEEDED_ANALYSIS = '''"""Berth waiting before and after slot booking at T2. Run: python analysis.py"""
import pandas as pd

calls = pd.read_csv("berth_calls.csv")

# cell 1: clean
calls = calls.dropna(subset=["wait_h"])          # drop calls without a waiting time

# cell 2: the effect of slot booking
after = calls[calls.month >= 13]
t2 = after[after.terminal == "T2"].wait_h.mean()
others = after[after.terminal != "T2"].wait_h.mean()
print(f"mean wait, months 13 to 24: T2 {t2:.1f} h, other terminals {others:.1f} h")
print(f"reduction at T2: {100 * (others - t2) / others:.0f}%")

# cell 3: before and after at T2
t2_all = calls[calls.terminal == "T2"]
before = t2_all[t2_all.month <= 12].wait_h.mean()
print(f"T2 before {before:.1f} h, after {t2:.1f} h, change {100 * (t2 - before) / before:.0f}%")

# cell 4: by vessel type at T2, months 13 to 24 (minutes)
print(after[after.terminal == "T2"].groupby("vessel_type").wait_h.mean().round(1).to_string())

# cell 5: the longest waits, for follow-up with the vessels
print(after.nlargest(5, "wait_h")[["call_id", "terminal", "wait_h", "master_name", "master_mobile"]].to_string(index=False))
'''


def write_berth_repo(df):
    repo = REPOS / "berth_delay"
    if repo.exists():
        shutil.rmtree(repo)
    repo.mkdir(parents=True)
    wtext(repo / "analysis.py", SEEDED_ANALYSIS)
    # the analysis's own numbers, computed the way it computes them
    d = df.dropna(subset=["wait_h"])
    after = d[d.month >= 13]
    t2 = after[after.terminal == "T2"].wait_h.mean()
    others = after[after.terminal != "T2"].wait_h.mean()
    red = 100 * (others - t2) / others
    before = d[(d.terminal == "T2") & (d.month <= 12)].wait_h.mean()
    wtext(repo / "REPORT.md", f"""# Slot booking at T2: effect on berth waiting

Prepared by the analytics unit for the director of marine operations. Draft for review.

## Finding

Slot booking has **halved** waiting at T2. In months 13 to 24, vessels at T2 waited {t2:.1f} hours on average against
{others:.1f} hours at the other terminals. Waiting at T2 also fell from {before:.1f} to {t2:.1f} hours after slot booking started.

## Recommendation

Extend slot booking to all four terminals from next quarter.

## Method

Berth calls of months 1 to 24 (berth_calls.csv). Calls without a waiting time were removed as incomplete records.
Table 4 gives the waiting time by vessel type at T2, in minutes. Table 5 lists the longest waits for follow-up.
""")
    wtext(repo / "README.md", "# berth_delay\n\nRun `python analysis.py` from this folder. It reads `berth_calls.csv` (copied from the unit's extract).\n")
    shutil.copy(DATA / "berth_calls.csv", repo / "berth_calls.csv")
    return {"reported_reduction_pct": round(float(red), 1), "t2_after": round(float(t2), 1),
            "others_after": round(float(others), 1), "t2_before": round(float(before), 1)}


FLAWS = {
    "C1": {"title": "No baseline: T2 is compared with the other terminals after the change only; T2 already had the shortest waits before", "severity_ref": 3, "faleh": 3},
    "C2": {"title": "Diverted calls dropped: vessels that left after a long wait are removed, and they rose at T2 after the change", "severity_ref": 2, "faleh": 3},
    "M1": {"title": "The text says 'halved'; the printed reduction is smaller", "severity_ref": 2, "faleh": 2},
    "M2": {"title": "The before period at T2 includes the weather closures of months 3 and 4", "severity_ref": 1, "faleh": 2},
    "m1": {"title": "Table 4 is labelled minutes; the values are hours", "severity_ref": 1, "faleh": 1},
    "P1": {"title": "Table 5 prints vessel masters' names and mobile numbers: personal data in an output", "severity_ref": 3, "faleh": 1},
}


# ---------------------------------------------------------------------------------------------- 4 · cargo dwell
def make_containers(rng, weeks, n_per_week, call_offset):
    rows = []
    k = 0
    for w in range(1, weeks + 1):
        for _ in range(n_per_week):
            k += 1
            mt = rng.choice(["import", "export", "transshipment"], p=[0.55, 0.30, 0.15])
            mean = {"import": 4.6, "export": 3.0, "transshipment": 7.5}[mt]
            dwell = rng.gamma(4.0, mean / 4.0)
            call = f"V{call_offset + w * 10 + rng.integers(0, 8):04d}"
            rows.append({"container_id": f"{'Q' if call_offset else 'K'}{k:06d}", "week": w, "vessel_call": call,
                         "move_type": mt, "dwell_days": round(float(dwell), 2)})
    return pd.DataFrame(rows)


DWELL_PY = '''"""Mean import dwell for the quarterly note. Saleh Al-Ghamlas. Tested with pandas 1.5."""
import pandas as pd

DATA = r"C:\\Users\\saleh\\Desktop\\port\\containers.csv"  # academy:example (the planted absolute path)

boxes = pd.read_csv(DATA)
lookup = pd.read_csv("data/berth_lookup.csv")      # vessel call to terminal
boxes = boxes.merge(lookup, on="vessel_call")

boxes = boxes.sample(2000)                          # a sample, to run faster

imports = boxes[boxes.move_type != "export"]        # imports
summary = pd.DataFrame(columns=["terminal", "mean_dwell"])
for t, g in imports.groupby("terminal"):
    summary = summary.append({"terminal": t, "mean_dwell": round(g.dwell_days.mean(), 2)}, ignore_index=True)
print(summary.to_string(index=False))
print(f"MEAN IMPORT DWELL {imports.dwell_days.mean():.2f}")
'''


def write_cargo(rng):
    q3 = make_containers(rng, 13, 540, 1000)
    calls = sorted(q3.vessel_call.unique())
    lookup = pd.DataFrame({"vessel_call": calls, "terminal": [TERMINALS[i % 4] for i in range(len(calls))]})
    repo = REPOS / "cargo_dwell"
    if repo.exists():
        shutil.rmtree(repo)
    (repo / "data").mkdir(parents=True)
    q3.to_csv(repo / "data" / "containers_q3.csv", index=False, lineterminator="\n")
    wtext(repo / "dwell.py", DWELL_PY)
    wtext(repo / "requirements.txt", "pandas\n")
    true_import = float(q3[q3.move_type == "import"].dwell_days.mean())
    with_trans = float(q3[q3.move_type != "export"].dwell_days.mean())
    wtext(repo / "README.md", "# cargo_dwell\n\nMean import dwell for the quarterly note.\n\n1. Put `containers.csv` in `data/`.\n"
          "2. `pip install -r requirements.txt`\n3. `python dwell.py`\n\nThe Q3 result is in `report.md`.\n")
    wtext(repo / "report.md", f"# Cargo dwell, Q3\n\nMean import dwell: **{true_import:.2f} days** ({(q3.move_type == 'import').sum():,} import containers).\n")
    lookup.to_csv(DATA / "berth_lookup.csv", index=False, lineterminator="\n")   # the file Saleh sends when asked
    wjson(REF / "rerun.json", {
        "patches": [
            ["dwell.py", 'summary = summary.append({"terminal": t, "mean_dwell": round(g.dwell_days.mean(), 2)}, ignore_index=True)',
             'summary.loc[len(summary)] = [t, round(g.dwell_days.mean(), 2)]'],
            ["dwell.py", "boxes = boxes.sample(2000)", "# sample removed by the reviewer"],
        ],
        "steps": [
            {"what failed": "absolute path to the analyst's desktop", "kind": "path", "fix": "relative path data/containers.csv"},
            {"what failed": "the README names containers.csv; the repository holds containers_q3.csv", "kind": "documentation", "fix": "renamed the file in the copy"},
            {"what failed": "data/berth_lookup.csv is read but not in the repository", "kind": "missing input", "fix": "asked for the file; added it"},
            {"what failed": "DataFrame.append no longer exists in pandas 2; no version pinned", "kind": "library version", "fix": "the same row added with .loc"},
            {"what failed": "two runs give two figures: an unseeded sample", "kind": "randomness", "fix": "removed the sample"},
        ],
        "gap": {"what failed": "the script keeps transshipment with imports; the report removed it by hand", "kind": "manual step", "fix": "filter move_type == 'import' in the script"},
        "reported": round(true_import, 2), "with_transshipment": round(with_trans, 2),
    })

    # Q2: the extract behind the released board figure loaded weeks 5 and 6 twice
    q2 = make_containers(rng, 13, 540, 0)
    short = q2.week.isin([5, 6])
    q2.loc[short, "dwell_days"] = (q2.loc[short, "dwell_days"] * 0.55).round(2)   # Eid weeks: fast clearance
    released = pd.concat([q2, q2[short]], ignore_index=True)
    released.to_csv(DATA / "containers_q2_released.csv", index=False, lineterminator="\n")
    imp = released[released.move_type == "import"]
    imp_ok = q2[q2.move_type == "import"]
    return {"q3_reported": round(true_import, 2), "q3_with_transshipment": round(with_trans, 2),
            "q2_released": round(float(imp.dwell_days.mean()), 2), "q2_corrected": round(float(imp_ok.dwell_days.mean()), 2),
            "q2_duplicates": int(short.sum()), "q2_rows_released": len(released)}


# ---------------------------------------------------------------------------------------------- 5 · AI rules
GUIDE = [
    {"id": "G1", "section": "3.2 Reliability and Safety", "duty": "Mark content generated with generative AI, so its reliability can be checked against other sources."},
    {"id": "G2", "section": "3.2 Reliability and Safety", "duty": "Check generated content for factual accuracy and relevance before it is used."},
    {"id": "G3", "section": "3.3 Transparency and Interpretability", "duty": "Tell the people who receive content when it was created with generative AI."},
    {"id": "G4", "section": "3.5 Privacy and Security", "duty": "Do not enter data classified restricted or higher into generative AI tools; limit their use to public data."},
    {"id": "G5", "section": "Practical guidelines: analysing data", "duty": "Restrict analysis by generative AI to public or open datasets, anonymise first, and keep a clear record of the analysis process."},
    {"id": "G6", "section": "Appendix 2: checklist, outputs", "duty": "Verify outputs, especially for official reports, and verify generated code before it is used or run."},
    {"id": "G7", "section": "Appendix 2: checklist, disclosure", "duty": "Limit tool use to authorised staff, and keep records of how staff use the tool."},
]

RULES_REF = {
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
    "unaided": [
        {"id": "U1", "rule": "Each analyst does one analysis a quarter without an assistant, reviewed like any other."},
    ],
}

SCENARIOS = [
    {"id": "S1", "text": "An analyst asks a hosted assistant to explain a pandas error message, pasting the traceback only.", "key": "allowed", "rules": []},
    {"id": "S2", "text": "An analyst pastes the pilot roster with pilots' names and shifts into a hosted assistant to find fatigue risks.", "key": "breach", "rules": ["C1"]},
    {"id": "S3", "text": "The assistant drafts the summary of a board paper; the analyst edits the wording and sends it without a disclosure line.", "key": "breach", "rules": ["D1"]},
    {"id": "S4", "text": "The assistant writes the code of a dwell-time analysis; the analyst runs it, checks three numbers by hand and keeps the run.", "key": "needs action", "rules": ["K1", "K2"]},
    {"id": "S5", "text": "The assistant gives a waiting-time reduction of 18%; the analyst copies it into the draft and plans to check it after the review.", "key": "breach", "rules": ["V1"]},
    {"id": "S6", "text": "An analyst uses the authority's approved assistant on the public cargo statistics and keeps prompts and outputs in the repository.", "key": "allowed", "rules": []},
    {"id": "S7", "text": "A new analyst has used the assistant for every analysis for six months and never worked a problem unaided.", "key": "needs action", "rules": ["U1"]},
    {"id": "S8", "text": "An analyst tries a new free chatbot found online on anonymised berth data.", "key": "breach", "rules": ["C2"]},
]


def write_ai(df):
    wjson(DATA / "guidelines_digest.json", GUIDE)
    wjson(DATA / "rules_reference.json", RULES_REF)
    wjson(DATA / "scenarios.json", [{"id": s["id"], "text": s["text"]} for s in SCENARIOS])
    wjson(REF / "rules.json", RULES_REF)
    wjson(REF / "scenarios.json", {s["id"]: {"decision": s["key"], "rules": s["rules"]} for s in SCENARIOS})

    # five assisted analyses from the unit's log; A3's headline can be recomputed from berth_calls.csv
    d = df[(df.month >= 13) & (df.terminal == "T1")].dropna(subset=["wait_h"])
    share = float((d.wait_h > 12).mean() * 100)
    log = [
        {"id": "A1", "title": "Tug fuel use per call, Q3", "analyst": "Rakan", "tool": "approved assistant", "data_class": "public",
         "disclosure": "Code drafted with the approved assistant; all figures re-run by the analyst; reviewed by Faleh Al-Musharraf.",
         "prompts_kept": True, "verification": [{"number": "fuel per call 412 litres", "rerun": "412 litres", "by": "Rakan"}], "reviewer": "Faleh Al-Musharraf"},
        {"id": "A2", "title": "Fatigue risk in the night pilot roster", "analyst": "Shaden Al-Ruwayshid", "tool": "approved assistant", "data_class": "restricted (names and shifts of pilots)",
         "disclosure": "Drafted with the approved assistant; figures re-run.", "prompts_kept": True,
         "verification": [{"number": "11 shifts above the fatigue limit", "rerun": "11 shifts", "by": "Shaden Al-Ruwayshid"}], "reviewer": "Saleh Al-Ghamlas"},
        {"id": "A3", "title": "Share of T1 calls waiting more than 12 hours, months 13 to 24", "analyst": "Saleh Al-Ghamlas", "tool": "approved assistant", "data_class": "public (aggregated berth data)",
         "disclosure": "Summary drafted with the approved assistant.", "prompts_kept": True,
         "verification": [], "headline": "18.4% of calls at T1 waited more than 12 hours", "reviewer": "Faleh Al-Musharraf"},
        {"id": "A4", "title": "Storage-fee scenarios for the board", "analyst": "Lina", "tool": "approved assistant", "data_class": "public",
         "disclosure": "", "prompts_kept": True,
         "verification": [{"number": "revenue +6.2%", "rerun": "+6.2%", "by": "Lina"}], "reviewer": "Faleh Al-Musharraf", "note": "board paper sent without a disclosure line"},
        {"id": "A5", "title": "Gate no-show patterns", "analyst": "Majid", "tool": "approved assistant", "data_class": "public",
         "disclosure": "Analysis drafted with the approved assistant; figures re-run.", "prompts_kept": False,
         "verification": [], "reviewer": "Saleh Al-Ghamlas", "note": "the analyst says he checked the numbers; no record kept"},
    ]
    wjson(DATA / "assisted_log.json", log)
    key = {"A1": [], "A2": ["C1"], "A3": ["V1", "K2"], "A4": ["D1"], "A5": ["K1", "K2"]}
    wjson(REF / "audit.json", {"breaches": key, "a3_recomputed_pct": round(share, 1)})
    return round(share, 1)


# ---------------------------------------------------------------------------------------------- 6 · feedback, capacity
SHADEN_REVIEW = [
    {"id": "F1", "cell": "cell 3", "finding": "Mean dwell computed over imports and transshipment together", "severity": 3, "area": "data"},
    {"id": "F2", "cell": "cell 5", "finding": "Before-and-after comparison at T2 with no comparison terminal", "severity": 3, "area": "method"},
    {"id": "F3", "cell": "cell 6", "finding": "'Waiting fell sharply' with no interval; the change is 0.9 hours on 610 calls", "severity": 2, "area": "inference"},
    {"id": "F4", "cell": "cell 2", "finding": "1,214 rows dropped with no count of why", "severity": 2, "area": "data"},
    {"id": "F5", "cell": "cell 7", "finding": "Chart axis starts at 6 hours, so a small change looks large", "severity": 1, "area": "communication"},
    {"id": "F6", "cell": "cell 1", "finding": "Variable names d1, d2, tmp", "severity": 1, "area": "communication"},
    {"id": "F7", "cell": "whole notebook", "finding": "Assistant-drafted cells 3 to 6 are not disclosed; no verification record", "severity": 2, "area": "communication"},
]
SKILLS = ["framing", "data handling", "methods", "inference", "communication", "reproducibility", "assisted-work verification"]


def write_people(rng):
    wjson(DATA / "shaden_review.json", SHADEN_REVIEW)
    analysts = [
        ("A01", "Faleh Al-Musharraf", "senior", 60), ("A02", "Saleh Al-Ghamlas", "senior", 50), ("A03", "Noor", "senior", 40),
        ("A04", "Lina", "mid", 70), ("A05", "Rakan", "mid", 70), ("A06", "Majid", "mid", 60), ("A07", "Huda", "mid", 60),
        ("A08", "Omar", "mid", 60), ("A09", "Reema", "mid", 50),
        ("A10", "Shaden Al-Ruwayshid", "junior", 20), ("A11", "Turki", "junior", 20), ("A12", "Dalia", "junior", 20),
    ]
    profiles = {}
    for aid, name, sen, cap in analysts:
        base = {"senior": 3.4, "mid": 2.6, "junior": 1.6}[sen]
        profiles[aid] = {s: int(np.clip(round(base + rng.normal(0, 0.6)), 1, 4)) for s in SKILLS}
    profiles["A10"] = {"framing": 2, "data handling": 2, "methods": 1, "inference": 1, "communication": 3,
                       "reproducibility": 2, "assisted-work verification": 1}
    wjson(DATA / "analysts.json", [{"id": a, "name": n, "seniority": s, "review_hours": c, "skills": profiles[a]} for a, n, s, c in analysts])
    # 40 planned analyses next quarter
    authors = [a[0] for a in analysts]
    levels = [1] * 10 + [2] * 14 + [3] * 12 + [4] * 4
    rng.shuffle(levels)
    pipeline = []
    for i, lv in enumerate(levels):
        pipeline.append({"id": f"P{i + 1:02d}", "author": authors[int(rng.integers(0, 12))], "level": int(lv)})
    wjson(DATA / "pipeline_q1.json", pipeline)
    hours = {1: 0, 2: 4, 3: 10, 4: 16}
    demand_senior = sum(hours[p["level"]] for p in pipeline if p["level"] >= 3)
    return {"review_hours": hours, "senior_demand": demand_senior, "pipeline": pipeline, "analysts": analysts}


# ---------------------------------------------------------------------------------------------- 7 · sponsors
ROLES = {
    "bader": {
        "name": "Bader Al-Khayyal",
        "change_after": 4,
        "change": "The board meeting has moved forward: I need this in four working days, not five. And the deputy chief executive now also wants to know what slot booking does to the feeder lines.",
        "topics": [
            {"id": "offer", "keys": ["option", "propose", "fits"], "constraint": False,
             "answer": "If it answers the feeder question, that works for me. Put it in writing today."},
            {"id": "decision", "keys": ["decision", "decide", "for what"], "constraint": True,
             "answer": "The board decides whether slot booking goes to all four terminals next quarter. I present the recommendation."},
            {"id": "deadline", "keys": ["when", "deadline", "date", "week", "time"], "constraint": True,
             "answer": "The board papers close in a week, five working days from today."},
            {"id": "evidence", "keys": ["evidence", "convince", "believe", "trust", "number", "measure"], "constraint": True,
             "answer": "Average waiting matters, but I will not sign anything if the shipping lines can show it hurt them."},
            {"id": "already", "keys": ["already", "know", "draft", "existing", "report"], "constraint": True,
             "answer": "There is a draft that says waiting halved at T2. Someone told me it has problems."},
            {"id": "scope", "keys": ["which terminal", "scope", "include", "vessel type"], "constraint": False,
             "answer": "I care about T2 against the others. Feeders are a detail, in my view."},
            {"id": "risk", "keys": ["risk", "wrong", "worst", "if"], "constraint": False,
             "answer": "If we extend it and it fails, the lines will complain to the ministry. That is the risk."},
        ],
    },
    "faleh": {
        "name": "Faleh Al-Musharraf",
        "change_after": 99, "change": "",
        "topics": [
            {"id": "privacy", "keys": ["privacy", "personal", "p1", "names", "mobile"], "constraint": True,
             "answer": "I rated the names minor: they do not change the decision. But you are right that they cannot leave the unit."},
            {"id": "diverted", "keys": ["divert", "c2", "dropped", "missing"], "constraint": True,
             "answer": "I thought the diverted calls were few. I did not count them by terminal."},
            {"id": "storm", "keys": ["storm", "weather", "m2", "closure"], "constraint": False,
             "answer": "The closures are in the before period only for T2's comparison, so I called it minor."},
        ],
    },
}

INVENTORY = [
    {"id": "Q-a", "question": "How has mean waiting at T2 changed against the other terminals since slot booking? (difference in differences)", "analyst_days": 1.5, "level": 3},
    {"id": "Q-b", "question": "The same by vessel type, with feeders separate", "analyst_days": 0.5, "level": 3},
    {"id": "Q-c", "question": "How many calls diverted to other ports, by terminal, before and after", "analyst_days": 1, "level": 2},
    {"id": "Q-d", "question": "Forecast of waiting if slot booking reaches all four terminals", "analyst_days": 6, "level": 4},
    {"id": "Q-e", "question": "The cost to shipping lines of the change in waiting", "analyst_days": 4, "level": 3},
]
REVIEW_DAYS = {1: 0, 2: 0.5, 3: 1, 4: 2}

KHALED = """From: Khaled Al-Kharji, deputy chief executive for commercial affairs
To: Head of the analytics unit
Subject: Slot booking paper: the feeder table

Thank you for the revised evaluation. It is clear and the board will welcome the overall result.

One request. Please take the feeder table out of the paper. Feeders are small local operators, less than a quarter
of calls and a small share of revenue, and the table will distract the board from the decision. The feeder lines can
be handled separately by my team. I would like the paper to go with the overall figure only.

I need the final version by the end of tomorrow.
"""


def write_sponsors():
    wjson(DATA / "roles.json", ROLES)
    wjson(DATA / "inventory.json", {"questions": INVENTORY, "review_days": REVIEW_DAYS, "working_days": 5, "analysts_available": 1})
    wtext(DATA / "khaled_request.md", KHALED)


# ---------------------------------------------------------------------------------------------- 8 · capstone
STAFF_PY = '''"""Night-shift marine pilots: how many are needed? Saleh Al-Ghamlas."""
import pandas as pd

jobs = pd.read_csv("pilot_jobs.csv")
night = jobs[jobs["shift"] == "night"]

# jobs per night, averaged over the year
per_night = night.groupby("night").size()
print(f"mean pilotage jobs per night: {per_night.mean():.1f}")

# each pilot can do 3 jobs a night
needed = per_night.mean() / 3
print(f"pilots needed per night: {needed:.1f}  ->  recommend 4 instead of 6")
'''


def write_capstone(rng):
    rows = []
    for night in range(1, 366):
        surge = 1.6 if 150 <= night <= 210 else 1.0          # tanker season
        n = int(rng.poisson(9.5 * surge))
        for j in range(n):
            rows.append({"night": night, "shift": "night", "job_id": f"J{night:03d}{j:02d}",
                         "vessel_type": rng.choice(["tanker", "container", "bulk", "feeder"], p=[0.35, 0.35, 0.15, 0.15]),
                         "job_hours": round(float(rng.gamma(3.0, 0.9)), 2)})
    jobs = pd.DataFrame(rows)
    CAP.mkdir(parents=True, exist_ok=True)
    jobs.to_csv(CAP / "pilot_jobs.csv", index=False, lineterminator="\n")
    wtext(CAP / "staffing.py", STAFF_PY)
    per = jobs.groupby("night").size()
    return {"mean_jobs": round(float(per.mean()), 1), "p95_jobs": int(per.quantile(0.95)),
            "surge_mean": round(float(per.loc[150:210].mean()), 1)}


# ---------------------------------------------------------------------------------------------- 9 · unit standard, references
UNIT_STANDARD = """# Analytical quality standard, Ras Sahil analytics unit (reference version)

The reference version that Labs 3.3, 3.4 and the capstone cite. Your own draft from Day 1 may differ.

S-1. Every request gets an assurance level from the matrix of effect and complexity, raised by one for public release
or safety use, at most level 4. Personal data adds the data protection officer's check.
S-2. Four roles: commissioner, analyst, assurer, approver. Nobody assures or approves an analysis they worked on.
S-3. From level 2 the reviewer re-runs the analysis from its repository before reading it, and keeps a re-run log.
S-4. Every review uses the unit's checklist at the analysis's level. The privacy and classification item applies at
every level: an output with personal data, or a breach of its classification, does not leave the unit.
S-5. Severity is rated by the effect on the decision: critical if the decision changes or the output cannot leave the
unit, major if the size or the confidence changes, minor otherwise.
S-6. Assisted work follows the unit's rules for AI-assisted analysis: verified, disclosed, prompts and a verification
record kept, public or anonymised data only.
S-7. Findings are not removed from a paper after review. A disagreement is recorded beside the finding, with who
disagrees and why.
S-8. Pressure to change or remove a finding is recorded in the decision log the same day; if repeated, it is escalated
to the chief executive's office with the record.
S-9. Every paper at level 2 or above carries a quality statement: the level, what was checked, by whom, what remains
uncertain with a number, any assisted part, the classification.
S-10. An error found after release is corrected within five working days by a notice that gives the released and
corrected values, the cause in the process, the decisions affected, the process change and who is told.
"""


ROTA_ASSIGN = {"P01": "A04", "P02": "A04+A01", "P03": "A05", "P04": "A06", "P05": "A09", "P06": "A01", "P08": "A02", "P09": "A01", "P10": "A04", "P12": "A06",
               "P14": "A05+A02", "P15": "A04+A02", "P17": "A05+A03", "P18": "A06+A03", "P21": "A05", "P22": "A09", "P23": "A02", "P24": "A07",
               "P26": "A08", "P27": "A02", "P28": "A05", "P29": "A03", "P30": "A03", "P31": "A06", "P32": "A04", "P33": "A09", "P34": "A01",
               "P38": "A03", "P39": "A01", "P40": "A02"}
ROTA_SECOND = {"P09": "A07", "P34": "A08", "P39": "A07", "P40": "A08"}


def write_references(df, cargo, pipeline, analysts):
    wtext(DATA / "unit_standard.md", UNIT_STANDARD)
    assign, second = ROTA_ASSIGN, ROTA_SECOND
    wjson(REF / "rota.json", {"assign": assign, "second": second, "mentors": {"A10": "A01", "A11": "A04", "A12": "A05"}})
    wjson(REF / "feedback.json", {
        "notes": [
            {"id": "F2", "observation": "In cell 5 waiting at T2 is compared before and after, with no other terminal as a comparison.",
             "effect": "Waiting fell at every terminal in month 13, so most of the fall would have happened anyway.",
             "reasoning": "Before saying a change caused a difference, ask what would have happened without it.",
             "next": "Write the comparison group in the first cell of your next comparison."},
        ],
        "plan": [
            {"month": 1, "goal": "Choose a comparison group every time", "activity": "Two pair reviews with a senior analyst",
             "evidence": "Two analyses passed on item M1", "support": "A senior analyst, one hour a week"},
            {"month": 2, "goal": "Verify every assisted number before review", "activity": "A verification table in each assisted analysis",
             "evidence": "Three analyses with complete verification records", "support": "The audit checklist and a monthly check"},
            {"month": 3, "goal": "State uncertainty for decision numbers", "activity": "One analysis done unaided, without the assistant",
             "evidence": "An unaided analysis that passes a level 2 review", "support": "A worked example and a senior review"},
        ],
    })
    wjson(REF / "scope.json", {
        "options": {"A": {"questions": ["Q-a", "Q-c"], "leaves_out": "vessel types, forecast and cost"},
                    "B": {"questions": ["Q-a", "Q-b"], "leaves_out": "diversions, forecast and cost"}},
        "messages": ["Which decision will the board take with this?", "When do the board papers close?",
                     "What evidence would convince you?", "What exists already: is there a draft?",
                     "With four days, option B fits: the effect at T2 and the same by vessel type."],
        "record": {"decision": "Whether to extend slot booking to all four terminals", "in_scope": ["Q-a", "Q-b"],
                   "out_of_scope": ["Q-c and Q-e for the following board", "Q-d not before a decision to extend"],
                   "working_days": 4, "options_offered": ["A", "B"],
                   "after_change": "With four days, option B: it answers the feeder question that was added; diversions move to the next board."},
    })
    import math
    rows = []
    for m in (3, 6, 12):
        d = df[(df.weather_closure == 0) & (df.month <= 12 + m)].assign(wait_h=df.wait_h.fillna(24.0))
        after, t2 = d.month >= 13, d.terminal == "T2"
        cells = [d[a & b].wait_h for a in (after, ~after) for b in (t2, ~t2)]
        se = math.sqrt(sum(c.var(ddof=1) / len(c) for c in cells))
        rows.append({"months_after": m, "se_h": round(se, 3), "mdc_h": round(2.8 * se, 2)})
    wjson(REF / "agreement.json", {
        "decision": {"question": "Should slot booking be extended from T2 to all four terminals next quarter?",
                     "options": ["Extend to all terminals", "Keep at T2 only and fix the feeder slots", "Stop slot booking"]},
        "mdc": rows,
        "rule": {"decision_rule": "Extend if waiting at T2 falls by at least 2.0 hours per call against the other terminals, and no vessel type waits more than 2.0 hours longer.",
                 "evidence_threshold_h": 2.0, "data": "Months 1 to 24, weather closures left out, diverted calls at 24 hours"},
        "roles": {"level": 3, "analyst": "Saleh Al-Ghamlas", "assurer": "Faleh Al-Musharraf", "approver": "Arjwan Al-Huqail",
                  "commissioner": "Bader Al-Khayyal", "signed_before": "the analysis starts"},
    })
    t2 = df[df.terminal == "T2"]
    finding = {"feeder_h": round(did(df, lambda d: d.vessel_type == "feeder", fill_diverted=24.0), 2),
               "others_h": round(did(df, lambda d: d.vessel_type != "feeder", fill_diverted=24.0), 2),
               "all_h": round(did(df, fill_diverted=24.0), 2),
               "feeder_share_t2": round(100 * float((t2.vessel_type == "feeder").mean()), 1),
               "feeder_calls_t2_after": int(((t2.vessel_type == "feeder") & (t2.month >= 13)).sum()),
               "feeder_diverted_t2_after": int(t2[(t2.vessel_type == "feeder") & (t2.month >= 13)].diverted.sum())}
    wjson(REF / "pressure.json", {
        "finding": finding,
        "options": [{"option": "Remove the feeder table", "effect": "The board decides without the condition it agreed."},
                    {"option": "Keep the table as it is", "effect": "The finding stays; the sponsor may feel ambushed."},
                    {"option": "Keep the table, add context and the commercial team's plan", "effect": "The finding stays, with a constructive role for the sponsor."}],
        "record": {"request": "Remove the feeder table", "finding_checked": f"Feeders +{finding['feeder_h']} h at T2",
                   "options": ["Remove", "Keep", "Keep with context"], "decision": "Keep the feeder table, with context",
                   "reasons": ["The signed agreement includes the vessel-type condition in the decision rule.",
                               "The result is large and rests on hundreds of calls.",
                               "The local feeder lines bear the cost and would be left out of the paper."],
                   "standard_clauses": ["S-7", "S-8"], "principles": ["Fairness", "Transparency & Explainability", "Accountability & Responsibility"],
                   "who_told": "The requester and the sponsor", "date_recorded": "the day of the request"},
        "reply": "Thank you for the note. I will keep the feeder table, because the signed agreement makes it part of the decision rule, and I will add the context your team asked for.",
    })
    wjson(REF / "quality.json", {
        "statement": {"level": "Level 3", "checked": ["re-run", "comparison", "numbers traced", "no personal data"],
                      "by_whom": "Analyst, independent reviewer, head of unit",
                      "uncertain": ["the fall in waiting is between 0.3 and 1.3 hours per call"],
                      "assisted": "Method section drafted with the approved assistant and verified", "classification": "Internal"},
        "error": {"released": cargo["q2_released"], "corrected": cargo["q2_corrected"], "duplicates": cargo["q2_duplicates"], "weeks": [5, 6]},
        "notice": {"what_was_wrong": "Q2 mean import dwell", "released_value": f"{cargo['q2_released']} days",
                   "corrected_value": f"{cargo['q2_corrected']} days", "cause": "Two weeks loaded twice",
                   "decisions_affected": "None changed", "process_change": "Duplicate check on every extract",
                   "who_is_told": ["board secretary", "ministry indicator team", "quarterly note readers"]},
    })
    return assign, second


# ---------------------------------------------------------------------------------------------- main
def main():
    DATA.mkdir(exist_ok=True)
    REF.mkdir(parents=True, exist_ok=True)
    log, under = write_requests()
    write_reforms()
    df = write_berth(np.random.default_rng([SEED, 1]))
    seeded = write_berth_repo(df)
    wjson(REF / "flaws.json", {k: {"title": v["title"], "severity": v["severity_ref"]} for k, v in FLAWS.items()})
    wjson(DATA / "faleh_ratings.json", {k: v["faleh"] for k, v in FLAWS.items()})
    cargo = write_cargo(np.random.default_rng([SEED, 2]))
    a3 = write_ai(df)
    people = write_people(np.random.default_rng([SEED, 3]))
    write_sponsors()
    cap = write_capstone(np.random.default_rng([SEED, 4]))
    write_references(df, cargo, people.pop("pipeline"), people.pop("analysts"))

    est = {
        "did_clean": round(did(df), 2),
        "did_feeder": round(did(df, lambda d: d.vessel_type == "feeder"), 2),
        "did_other_types": round(did(df, lambda d: d.vessel_type != "feeder"), 2),
        "diverted_t2_before": int(df[(df.terminal == "T2") & (df.month <= 12)].diverted.sum()),
        "diverted_t2_after": int(df[(df.terminal == "T2") & (df.month >= 13)].diverted.sum()),
        "diverted_t2_feeder_after": int(df[(df.terminal == "T2") & (df.month >= 13) & (df.vessel_type == "feeder")].diverted.sum()),
    }
    summary = {"seeded": seeded, "estimates": est, "cargo": cargo, "a3_recomputed_pct": a3, "people": people, "capstone": cap,
               "under_assured": [r["id"] for r in under],
               "errors_under": sum(r["error_after_release"] for r in under),
               "errors_other": sum(r["error_after_release"] for r in log if r not in under)}
    wjson(REF / "summary.json", summary)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
