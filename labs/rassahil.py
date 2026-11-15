"""Helpers shared by every lab of Leading Analytical Work: Review, Standards and Stakeholders (DS-407).

The case: Ras Sahil Ports Authority, a fictional port authority, and its analytics unit of twelve analysts. All data
is synthetic (prepare_data.py, seed 407).

    import rassahil as U
    U.js("requests")                      # data/requests.json
    U.check(cond, "what is true")         # prints a tick, or stops with what is not true yet
    U.sponsor("bader", "question?")       # the scripted stand-in for a role-played sponsor
    U.tutor(draft, "what to look at")     # AI-tutor questions: a free hosted model, or a stand-in that says so
"""

from __future__ import annotations

import json
import math
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

import pandas as pd

LABS = Path(__file__).resolve().parent
DATA = LABS / "data"
OUT = LABS / "out"
QUICK = os.getenv("RASSAHIL_QUICK", "0") == "1"
AREAS = ["question fit", "data", "method", "inference", "communication"]
EFFECTS = ["low", "medium", "high"]


def _load_env():
    env = LABS / ".env"
    if env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))
    try:  # Colab: the Secrets panel
        from google.colab import userdata  # type: ignore
        os.environ.setdefault("OPENROUTER_API_KEY", userdata.get("OPENROUTER_API_KEY") or "")
    except Exception:
        pass


_load_env()


# ------------------------------------------------------------------ files and checks
def pick(full, quick):
    """The small value in quick mode (RASSAHIL_QUICK=1), the full one otherwise."""
    return quick if QUICK else full


def csv(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA / f"{name}.csv")


def js(name: str):
    return json.loads((DATA / f"{name}.json").read_text(encoding="utf-8"))


def text(name: str) -> str:
    return (DATA / name).read_text(encoding="utf-8")


def reference(name: str):
    """A reference result, so later cells run when an exercise is not done yet."""
    return json.loads((DATA / "reference" / f"{name}.json").read_text(encoding="utf-8"))


def save(name: str, content: str) -> Path:
    p = OUT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8", newline="\n")
    print("saved", p.relative_to(LABS).as_posix())
    return p


def check(cond: bool, what: str):
    if not cond:
        raise AssertionError("not yet: " + what)
    print("✅", what)


def words(s: str) -> int:
    return len(re.findall(r"[\w'%.,-]+", s))


VAGUE = ["be more careful", "improve", "better", "more rigorous", "pay attention", "be careful", "good job", "nice work",
         "work on", "try harder", "sloppy", "as appropriate", "where possible", "should consider"]


def vague_words(s: str) -> list[str]:
    low = s.lower()
    return [w for w in VAGUE if w in low]


# ------------------------------------------------------------------ Lab 1.1: the assurance standard
def level_for(standard: dict, grade: dict) -> int:
    """Apply a written standard to one request's grades, the way a peer would: matrix, then escalators."""
    lvl = int(standard["matrix"][grade["effect"]][grade["complexity"]])
    for flag, add in standard.get("escalators", {}).items():
        if grade.get(flag):
            lvl += int(add)
    return min(lvl, int(standard.get("max_level", 4)))


def apply_standard(standard: dict, grades: dict) -> dict:
    return {k: level_for(standard, g) for k, g in grades.items()}


def log_table(standard: dict) -> pd.DataFrame:
    """The request log with the level the standard requires, and whether each request was under-assured."""
    log = pd.DataFrame(js("requests")["log"])
    log["required"] = [level_for(standard, r) for r in log.to_dict("records")]
    log["under_assured"] = log.level_given < log.required
    return log


# ------------------------------------------------------------------ Lab 1.2: the checklist
def checklist_problems(items: list[dict]) -> list[str]:
    """What a team would trip over when using this checklist."""
    probs = []
    if len(items) > 18:
        probs.append(f"{len(items)} items: a checklist a team uses on every analysis has at most 18")
    for a in AREAS:
        n = sum(1 for i in items if i.get("area") == a)
        if n < 2 and a != "communication":
            probs.append(f"area '{a}' has {n} item(s); it needs at least two")
    if not any(i.get("privacy") and int(i.get("min_level", 9)) == 1 for i in items):
        probs.append("no privacy and classification item that applies from level 1")
    if not any(re.search(r"re-?run", i.get("item", ""), re.I) for i in items):
        probs.append("no item asks for a re-run")
    for i in items:
        if not i.get("item", "").strip().endswith("?"):
            probs.append(f"{i.get('id')}: write the item as a question")
        if not str(i.get("evidence", "")).strip():
            probs.append(f"{i.get('id')}: name the evidence that answers it")
        if int(i.get("min_level", 0)) not in (1, 2, 3, 4):
            probs.append(f"{i.get('id')}: set min_level to 1, 2, 3 or 4")
    if sum(1 for i in items if i.get("from")) < 5:
        probs.append("fewer than five items adapted from REFORMS: say which items each one comes from")
    return probs


def items_at_level(items: list[dict], level: int) -> list[str]:
    return [i["id"] for i in items if int(i["min_level"]) <= level]


# ------------------------------------------------------------------ Lab 1.3: re-running a repository
def copy_repo(name: str) -> Path:
    """A fresh working copy of a repository from data/repos/, in out/rerun/."""
    src, dst = DATA / "repos" / name, OUT / "rerun" / name
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst)
    return dst


def patch(repo: Path, file: str, old: str, new: str):
    p = repo / file
    s = p.read_text(encoding="utf-8")
    if old not in s:
        raise ValueError(f"'{old}' is not in {file}")
    p.write_text(s.replace(old, new, 1), encoding="utf-8", newline="\n")


def rerun(repo: Path, script: str, full: bool = False) -> tuple[bool, str]:
    """Run a script of the repository as its README says, in its own folder. Returns (ran, last lines of output),
    or the whole output with full=True."""
    env = dict(os.environ, PYTHONUTF8="1")
    r = subprocess.run([sys.executable, script], cwd=repo, capture_output=True, text=True, env=env, timeout=120)
    out = (r.stdout + r.stderr).strip().splitlines()
    if full:
        return r.returncode == 0, "\n".join(out)
    tail = "\n".join(out[-3:]) if r.returncode else "\n".join(out[-6:])
    return r.returncode == 0, tail


def headline(output: str, label: str) -> float | None:
    m = re.search(label + r"\s+([0-9.]+)", output)
    return float(m.group(1)) if m else None


FAILURE_KINDS = ["path", "documentation", "missing input", "library version", "randomness", "manual step"]


# ------------------------------------------------------------------ Lab 1.4: rules for assisted work
def rules_problems(rules: dict) -> list[str]:
    probs = []
    for part, need in (("verify", 2), ("disclose", 1), ("keep", 2), ("data", 1)):
        if len(rules.get(part, [])) < need:
            probs.append(f"'{part}' needs at least {need} rule(s)")
    alltext = " ".join(r["rule"] for part in rules.values() for r in part).lower()
    if "public" not in alltext:
        probs.append("no rule limits what data may go to a hosted assistant (the guideline: public data only)")
    if not re.search(r"re-?run|recomput", alltext):
        probs.append("no rule says assisted numbers are re-run")
    if not re.search(r"prompt", alltext):
        probs.append("no rule keeps the prompts")
    n = words(alltext)
    if n > 350:
        probs.append(f"{n} words: a one-page rule set has at most 350")
    for part in rules.values():
        for r in part:
            if vague_words(r["rule"]):
                probs.append(f"{r['id']}: vague words {vague_words(r['rule'])}")
    return probs


def score_scenarios(decisions: dict) -> tuple[int, list[str]]:
    ref = reference("scenarios")
    wrong = [k for k, v in ref.items() if decisions.get(k, {}).get("decision") != v["decision"]]
    return len(ref) - len(wrong), wrong


# ------------------------------------------------------------------ Lab 2.1: the berth-delay review
def berth_run(fix: set[str] | None = None) -> dict:
    """The seeded analysis's headline with some flaws fixed. 'C1': a difference in differences in place of a
    comparison after the change only; 'C2': diverted calls kept, with 24 hours as a lower bound of their wait;
    'M2': weather-closure calls left out. Returns the headline effect in hours and the decision it supports."""
    fix = set(fix or [])
    d = csv("berth_calls")
    if "M2" in fix:
        d = d[d.weather_closure == 0]
    if "C2" in fix:
        d = d.assign(wait_h=d.wait_h.fillna(24.0))
    else:
        d = d.dropna(subset=["wait_h"])
    after, t2 = d.month >= 13, d.terminal == "T2"
    m = lambda a, b: float(d[a & b].wait_h.mean())
    if "C1" in fix:
        effect = (m(t2, after) - m(t2, ~after)) - (m(~t2, after) - m(~t2, ~after))
    else:
        effect = m(t2, after) - m(~t2, after)
    return {"effect_h": round(effect, 2), "decision": "extend" if effect <= -2.0 else "do not extend as it is"}


def weighted_kappa(a: list[int], b: list[int], k: int = 3) -> float:
    """Cohen's weighted kappa with linear weights, for ratings 1..k."""
    n = len(a)
    obs = [[0.0] * k for _ in range(k)]
    for x, y in zip(a, b):
        obs[x - 1][y - 1] += 1 / n
    pa = [sum(obs[i]) for i in range(k)]
    pb = [sum(obs[i][j] for i in range(k)) for j in range(k)]
    w = lambda i, j: abs(i - j) / (k - 1)
    do = sum(w(i, j) * obs[i][j] for i in range(k) for j in range(k))
    de = sum(w(i, j) * pa[i] * pb[j] for i in range(k) for j in range(k))
    return 1 - do / de if de else 1.0


def agreement_table(mine: dict, theirs: dict) -> pd.DataFrame:
    keys = sorted(set(mine) | set(theirs))
    t = pd.DataFrame({"finding": keys, "me": [mine.get(k) for k in keys], "second reviewer": [theirs.get(k) for k in keys]})
    t["gap"] = (t["me"] - t["second reviewer"]).abs()
    return t


# ------------------------------------------------------------------ Lab 2.3: feedback and plans
def note_problems(note: dict) -> list[str]:
    probs = []
    for f in ("observation", "effect", "reasoning", "next"):
        if words(str(note.get(f, ""))) < 6:
            probs.append(f"{note.get('id')}: '{f}' is too short to act on")
    if not re.search(r"cell|\d", str(note.get("observation", ""))):
        probs.append(f"{note.get('id')}: the observation names no cell and no number")
    for f in ("observation", "effect", "reasoning", "next"):
        v = vague_words(str(note.get(f, "")))
        if v:
            probs.append(f"{note.get('id')}: vague words in '{f}': {v}")
    return probs


def plan_problems(plan: list[dict]) -> list[str]:
    probs = []
    if len(plan) != 3:
        probs.append("a three-month plan has three months")
    for m in plan:
        for f in ("goal", "activity", "evidence", "support"):
            if words(str(m.get(f, ""))) < 4:
                probs.append(f"month {m.get('month')}: '{f}' is missing or too short")
        if vague_words(" ".join(str(v) for v in m.values())):
            probs.append(f"month {m.get('month')}: vague words")
    if not any(re.search(r"unaided|without (the |an )?assistant", " ".join(str(v) for v in m.values()), re.I) for m in plan):
        probs.append("no unaided practice in the plan")
    return probs


# ------------------------------------------------------------------ Lab 2.4: the review rota
def review_hours() -> dict:
    return {1: 0, 2: 4, 3: 10, 4: 16}


COSIGN_HOURS = 2
SECOND_HOURS = 8


def _split(r: str) -> tuple[str, str | None]:
    """'A04' is a reviewer; 'A04+A01' is a mid-level reviewer whose level 3 review a senior co-signs."""
    a, _, b = r.partition("+")
    return a, (b or None)


def rota_violations(assign: dict, second: dict | None = None) -> list[str]:
    """assign: analysis id -> reviewer id, or 'mid+senior' for a co-signed level 3 review;
    second: level-4 analysis id -> second reviewer id (a senior or mid-level analyst)."""
    pipe = {p["id"]: p for p in js("pipeline_q1")}
    ana = {a["id"]: a for a in js("analysts")}
    second = second or {}
    v = []
    for pid, p in pipe.items():
        if p["level"] == 1:
            continue
        r = assign.get(pid)
        if r is None:
            v.append(f"{pid}: no reviewer")
            continue
        rev, cosign = _split(r)
        if p["author"] in (rev, cosign):
            v.append(f"{pid}: the author reviews their own work")
        if ana[rev]["seniority"] == "junior":
            v.append(f"{pid}: a junior analyst does not review alone")
        if cosign:
            if p["level"] != 3 or ana[rev]["seniority"] != "mid" or ana[cosign]["seniority"] != "senior":
                v.append(f"{pid}: a co-signed review is a level 3 analysis, a mid-level reviewer and a senior co-signer")
        elif p["level"] >= 3 and ana[rev]["seniority"] != "senior":
            v.append(f"{pid}: level {p['level']} needs a senior reviewer, {ana[rev]['name']} is {ana[rev]['seniority']}")
        if p["level"] == 4:
            s = second.get(pid)
            if s is None or s in (rev, p["author"]) or ana[s]["seniority"] == "junior":
                v.append(f"{pid}: level 4 needs a second reviewer, not junior, other than the first and the author")
    for rid, h in loads(assign, second).items():
        if h > ana[rid]["review_hours"]:
            v.append(f"{ana[rid]['name']}: {h} h assigned, {ana[rid]['review_hours']} h available")
    return v


def loads(assign: dict, second: dict | None = None) -> dict:
    """Review hours per analyst: the level's hours to the reviewer, 2 hours to a co-signer, 8 to a second reviewer."""
    pipe = {p["id"]: p for p in js("pipeline_q1")}
    hrs = review_hours()
    out: dict = {}
    for pid, r in assign.items():
        rev, cosign = _split(r)
        out[rev] = out.get(rev, 0) + hrs[pipe[pid]["level"]]
        if cosign:
            out[cosign] = out.get(cosign, 0) + COSIGN_HOURS
    for pid, s in (second or {}).items():
        out[s] = out.get(s, 0) + SECOND_HOURS
    return out


# ------------------------------------------------------------------ Lab 3.1 and the role-plays
_TURNS: dict[str, int] = {}
_HEARD: dict[str, set] = {}


def reset_role(role: str):
    _TURNS[role] = 0
    _HEARD[role] = set()


def sponsor(role: str, question: str) -> str:
    """The scripted stand-in answers by topic, and changes a constraint after a set number of turns. The trainer,
    or a peer with the role card, is better: use this to practise."""
    r = js("roles")[role]
    _TURNS[role] = _TURNS.get(role, 0) + 1
    q = question.lower()
    hits = [t for t in r["topics"] if any(k in q for k in t["keys"])]
    _HEARD.setdefault(role, set()).update(t["id"] for t in hits)
    ans = " ".join(t["answer"] for t in hits[:2]) or "I am not sure what you are asking. What do you need from me?"
    if _TURNS[role] == r["change_after"]:
        ans += "\n  [the constraint changes] " + r["change"]
    return f"{r['name']}: {ans}"


def role_coverage(role: str) -> tuple[int, int, list[str]]:
    r = js("roles")[role]
    cons = [t["id"] for t in r["topics"] if t.get("constraint")]
    heard = _HEARD.get(role, set())
    return len([c for c in cons if c in heard]), len(cons), [c for c in cons if c not in heard]


def days_needed(qids: list[str]) -> float:
    inv = js("inventory")
    q = {x["id"]: x for x in inv["questions"]}
    rd = {int(k): v for k, v in inv["review_days"].items()}
    return sum(q[i]["analyst_days"] + rd[q[i]["level"]] for i in qids)


def observer_score(record: dict, coverage: tuple[int, int, list[str]]) -> dict:
    """The observer's rubric, scored by rule: each criterion 0, 1 or 2. A person observes too."""
    s = {}
    found, total, _ = coverage
    s["asked before offering"] = 2 if found >= total - 1 else 1 if found >= 2 else 0
    s["options, not refusal"] = 2 if len(record.get("options_offered", [])) >= 2 else 1 if record.get("options_offered") else 0
    s["fits the deadline"] = 2 if days_needed(record.get("in_scope", [])) <= record.get("working_days", 0) else 0
    s["out of scope named"] = 2 if record.get("out_of_scope") else 0
    s["change handled"] = 2 if words(str(record.get("after_change", ""))) >= 12 else 1 if record.get("after_change") else 0
    s["total"] = sum(s.values())
    return s


# ------------------------------------------------------------------ Lab 3.2: evidence threshold
def did_by_month(data: pd.DataFrame, months_after: int) -> dict:
    """The difference-in-differences estimate and its standard error, with months_after months of data after the
    change (months 13 onwards), weather-closure calls left out, diverted calls counted at 24 hours."""
    d = data[(data.weather_closure == 0) & (data.month <= 12 + months_after)].assign(wait_h=data.wait_h.fillna(24.0))
    after, t2 = d.month >= 13, d.terminal == "T2"
    cells = [d[a & b].wait_h for a in (after, ~after) for b in (t2, ~t2)]
    est = (cells[0].mean() - cells[2].mean()) - (cells[1].mean() - cells[3].mean())
    se = math.sqrt(sum(c.var(ddof=1) / len(c) for c in cells))
    return {"months_after": months_after, "estimate_h": round(float(est), 2), "se_h": round(se, 3), "mdc_h": round(2.8 * se, 2)}


def agreement_problems(agr: dict) -> list[str]:
    probs = []
    for f in ("question", "decision", "options", "decision_rule", "evidence_threshold_h", "data", "level", "analyst", "assurer", "approver", "signed_before"):
        if f not in agr or agr[f] in (None, "", []):
            probs.append(f"missing: {f}")
    if agr.get("analyst") and agr.get("analyst") in (agr.get("assurer"), agr.get("approver")):
        probs.append("the analyst cannot also be the assurer or the approver")
    if not re.search(r"\d", str(agr.get("decision_rule", ""))):
        probs.append("the decision rule has no number")
    if len(agr.get("options", [])) < 2:
        probs.append("at least two options, one of them not to extend")
    return probs


# ------------------------------------------------------------------ Lab 3.3: subgroups and decision records
def subgroup_did(vessel_type: str | None = None, exclude: str | None = None) -> float:
    d = csv("berth_calls")
    d = d[d.weather_closure == 0].assign(wait_h=lambda x: x.wait_h.fillna(24.0))
    if vessel_type:
        d = d[d.vessel_type == vessel_type]
    if exclude:
        d = d[d.vessel_type != exclude]
    after, t2 = d.month >= 13, d.terminal == "T2"
    m = lambda a, b: float(d[a & b].wait_h.mean())
    return round((m(t2, after) - m(t2, ~after)) - (m(~t2, after) - m(~t2, ~after)), 2)


PRINCIPLES = ["Fairness", "Privacy & Security", "Humanity", "Social & Environmental Benefits", "Reliability & Safety",
              "Transparency & Explainability", "Accountability & Responsibility"]


def record_problems(rec: dict) -> list[str]:
    probs = []
    for f in ("request", "finding_checked", "options", "decision", "reasons", "standard_clauses", "principles", "who_told", "date_recorded"):
        if not rec.get(f):
            probs.append(f"missing: {f}")
    if any(p not in PRINCIPLES for p in rec.get("principles", [])):
        probs.append(f"principles are named as SDAIA names them: {PRINCIPLES}")
    if len(rec.get("options", [])) < 3:
        probs.append("weigh at least three options")
    if words(" ".join(rec.get("reasons", []))) < 25:
        probs.append("the reasons are too short for someone who was not there")
    return probs


# ------------------------------------------------------------------ Lab 3.4: quality statements and corrections
def statement_problems(st: dict) -> list[str]:
    probs = []
    for f in ("level", "checked", "by_whom", "uncertain", "assisted", "classification"):
        if not st.get(f):
            probs.append(f"missing: {f}")
    if not re.search(r"\d", " ".join(st.get("uncertain", []))):
        probs.append("state the uncertainty with a number")
    n = words(" ".join(str(v) if not isinstance(v, list) else " ".join(v) for v in st.values()))
    if n > 160:
        probs.append(f"{n} words: a board reads at most 160")
    return probs


def notice_problems(n: dict) -> list[str]:
    probs = []
    for f in ("what_was_wrong", "released_value", "corrected_value", "cause", "decisions_affected", "process_change", "who_is_told"):
        if n.get(f) in (None, "", []):
            probs.append(f"missing: {f}")
    blame = ["fault of", "careless", "mistake by", "blame"]
    if any(b in json.dumps(n).lower() for b in blame):
        probs.append("a correction names the cause in the process, not a person")
    return probs


# ------------------------------------------------------------------ the AI tutor
OPENROUTER = "https://openrouter.ai/api/v1/chat/completions"
MODEL = os.getenv("ASSISTANT_MODEL", "google/gemma-4-31b-it:free")
FALLBACKS = [m for m in os.getenv("ASSISTANT_FALLBACKS", "google/gemma-4-26b-a4b-it:free").split(",") if m]
TUTOR_RULES = ("You are a tutor for heads of analytics units writing standards, rules and feedback. Ask at most four "
               "short questions about the draft. Do not rewrite it and do not supply an answer.")


def _call(messages: list[dict], timeout: int = 60) -> str | None:
    key = os.getenv("OPENROUTER_API_KEY", "")
    if not key:
        return None
    body = {"model": MODEL, "models": [MODEL] + [m for m in FALLBACKS if m != MODEL], "messages": messages}
    req = urllib.request.Request(OPENROUTER, data=json.dumps(body).encode(), method="POST",
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())["choices"][0]["message"]["content"]
    except (urllib.error.URLError, KeyError, TimeoutError, json.JSONDecodeError):
        return None


def tutor(draft: str, focus: str) -> str:
    """AI-tutor questions on a draft: a free hosted model when OPENROUTER_API_KEY is set and answers, otherwise a
    rule-based stand-in that says so in its first line. Advice only: you decide."""
    reply = _call([{"role": "system", "content": TUTOR_RULES},
                   {"role": "user", "content": f"Focus: {focus}\n\nDraft:\n{draft}"}])
    if reply:
        return reply
    qs = []
    if vague_words(draft):
        qs.append(f"Which concrete action does '{vague_words(draft)[0]}' stand for?")
    if not re.search(r"\d", draft):
        qs.append("Which number would let someone check this was done?")
    if words(draft) > 300:
        qs.append(f"The draft has {words(draft)} words: which line could go?")
    qs.append(f"You asked about this: {focus.rstrip('?.')}. What would a sceptical colleague ask first?")
    return "[stand-in tutor (no model answered): rule checks, not a model's reading]\n- " + "\n- ".join(qs)
