# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Lab 1.3 · Re-run Saleh's repository
#
# Day 1 · Session 3 (Reproducibility as a team rule) · 25 min.
#
# Saleh Al-Ghamlas, a senior analyst, sent the quarterly cargo-dwell figure: **4.60 days** mean import dwell in Q3.
# Before anyone reads his report, the reviewer re-runs it from the repository, following the README and nothing
# else. You record every step that fails, its kind, and the fix, until the figure is reproduced or the gap is
# explained. The script really runs, in a copy under `out/rerun/`.
#
# **AI policy: AI-tutor.** A tutor may explain an error message; the log is yours.
#
# **Reference state.** `data/repos/cargo_dwell/` (the repository as Saleh sent it) and `data/berth_lookup.csv` (the
# file he sends when asked).
#
# **Tasks**
# - [ ] 1 · Follow the README exactly (5')
# - [ ] 2 · Log each failure with its kind (8')
# - [ ] 3 · Fix a copy until it runs (7')
# - [ ] 4 · Reproduce the reported figure or explain the gap (5')
# - [ ] ✱ Stretch · Write the repository rule that would have prevented each failure

# %%
import os, sys, subprocess, shutil
from pathlib import Path

IN_COLAB = "google.colab" in sys.modules
if IN_COLAB:
    REPO_URL = "https://github.com/SDAIAAcademy/ds-407.git"
    if not Path("/content/ds-407").exists():
        subprocess.run(["git", "clone", "-q", REPO_URL, "/content/ds-407"], check=True)
    os.chdir("/content/ds-407/labs")
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements-colab.txt"], check=True)
else:
    while not Path("rassahil.py").exists() and Path.cwd() != Path.cwd().parent:
        os.chdir("..")  # solutions/ notebooks run from labs/
sys.path.insert(0, os.getcwd())

import pandas as pd
import rassahil as U

repo = U.copy_repo("cargo_dwell")
print("working copy:", repo.relative_to(U.LABS).as_posix())
for p in sorted(repo.rglob("*")):
    if p.is_file():
        print("  ", p.relative_to(repo).as_posix())
print((repo / "README.md").read_text(encoding="utf-8"))

# %% [markdown]
# ## 1 · Follow the README exactly (5')
#
# The README says: put `containers.csv` in `data/`, install the requirements, run `python dwell.py`. The environment
# of this notebook already has pandas. Run the script as it is.

# %%
ok, out = U.rerun(repo, "dwell.py")
print("ran" if ok else "FAILED", "\n", out)
log = [{"step": 1, "what failed": out.splitlines()[-1] if not ok else "", "kind": None, "fix": None}]

# %% [markdown]
# ## 2 and 3 · Log each failure, fix a copy (8' + 7')
#
# ✏️ **Exercise** · Fix one failure at a time with `U.patch(repo, file, old, new)`, run again, and log what failed,
# its kind (`U.FAILURE_KINDS`) and the fix. Never edit Saleh's original in `data/repos/`: the working copy is yours.
# Expect five failures before the script runs to the end. Change as little as you can: a reviewer reproduces, she
# does not rewrite.

# %%
print("kinds:", U.FAILURE_KINDS)


def fix_and_log(repo: Path) -> list[dict]:
    steps = []
    # BEGIN SOLUTION
    U.patch(repo, "dwell.py", 'r"C:\\Users\\saleh\\Desktop\\port\\containers.csv"', '"data/containers.csv"')  # academy:example
    ok, out = U.rerun(repo, "dwell.py")
    steps.append({"what failed": "absolute path to Saleh's desktop", "kind": "path", "fix": "relative path data/containers.csv, as the README says", "after": out.splitlines()[-1]})
    (repo / "data" / "containers_q3.csv").rename(repo / "data" / "containers.csv")
    ok, out = U.rerun(repo, "dwell.py")
    steps.append({"what failed": "the README names containers.csv; the repository holds containers_q3.csv", "kind": "documentation", "fix": "renamed the file in the copy", "after": out.splitlines()[-1]})
    shutil.copy(U.DATA / "berth_lookup.csv", repo / "data" / "berth_lookup.csv")
    ok, out = U.rerun(repo, "dwell.py")
    steps.append({"what failed": "data/berth_lookup.csv is read but not in the repository", "kind": "missing input", "fix": "asked Saleh for the file; added it to the copy", "after": out.splitlines()[-1]})
    U.patch(repo, "dwell.py", 'summary = summary.append({"terminal": t, "mean_dwell": round(g.dwell_days.mean(), 2)}, ignore_index=True)',
            'summary.loc[len(summary)] = [t, round(g.dwell_days.mean(), 2)]')
    ok, out = U.rerun(repo, "dwell.py")
    steps.append({"what failed": "DataFrame.append no longer exists in pandas 2; requirements.txt does not pin a version", "kind": "library version", "fix": "the same row added with .loc", "after": out.splitlines()[-1]})
    first, second = out, U.rerun(repo, "dwell.py")[1]
    steps.append({"what failed": f"two runs give two figures ({U.headline(first, 'MEAN IMPORT DWELL')} and {U.headline(second, 'MEAN IMPORT DWELL')}): an unseeded sample of 2,000", "kind": "randomness", "fix": "removed the sample: the full file runs in a second", "after": ""})
    U.patch(repo, "dwell.py", "boxes = boxes.sample(2000)", "# sample removed by the reviewer")
    # END SOLUTION
    return steps


# %%
try:
    steps = fix_and_log(repo)
except NotImplementedError:
    steps = U.reference("rerun")["steps"]
    repo = U.copy_repo("cargo_dwell")
    U.patch(repo, "dwell.py", 'r"C:\\Users\\saleh\\Desktop\\port\\containers.csv"', '"data/containers.csv"')  # academy:example
    for f in U.reference("rerun")["patches"]:
        U.patch(repo, *f)
    (repo / "data" / "containers_q3.csv").rename(repo / "data" / "containers.csv")
    shutil.copy(U.DATA / "berth_lookup.csv", repo / "data" / "berth_lookup.csv")
ok, out = U.rerun(repo, "dwell.py")
print(out)
U.check(ok, "the script runs to the end")
U.check(len(steps) >= 5, "five failures logged")
U.check(len({s["kind"] for s in steps}) >= 5, "each failure has its kind, and they are of five kinds")

# %% [markdown]
# ## 4 · The reported figure (5')
#
# The script runs, but does it give **4.60**, the figure in `report.md`? If not, find the gap. Look at the filter that selects imports and at
# `data/containers.csv`: which move types does the filter keep? Saleh's report counts import containers only.
#
# ✏️ **Exercise** · Write the figure you get, the reported figure, and the cause of the gap. Then make the one change
# that reproduces the report and log it.

# %%
got = U.headline(out, "MEAN IMPORT DWELL")
boxes = pd.read_csv(repo / "data" / "containers.csv")
print("re-run gives", got, "| move types in the file:", boxes.move_type.value_counts().to_dict())


def explain_gap(repo: Path) -> dict:
    # BEGIN SOLUTION
    U.patch(repo, "dwell.py", 'boxes[boxes.move_type != "export"]', 'boxes[boxes.move_type == "import"]')
    return {"what failed": "the script keeps transshipment with imports; the report was made after removing transshipment by hand, a step no file records",
            "kind": "manual step", "fix": "filter move_type == 'import' in the script, so the step is in code"}
    # END SOLUTION


# %%
try:
    gap = explain_gap(repo)
except NotImplementedError:
    gap = U.reference("rerun")["gap"]
    U.patch(repo, "dwell.py", 'boxes[boxes.move_type != "export"]', 'boxes[boxes.move_type == "import"]')
steps.append(gap)
ok, out = U.rerun(repo, "dwell.py")
final = U.headline(out, "MEAN IMPORT DWELL")
reported = U.headline((repo / "report.md").read_text(encoding="utf-8").replace("**", ""), "Mean import dwell:")
print(f"before the last fix: {got}   after: {final}   reported: {reported}")
U.check(final == reported, "the reported figure is reproduced")
table = pd.DataFrame(steps)[["what failed", "kind", "fix"]]
print(table.to_string(index=True))
U.save("rerun_log.md", "# Re-run log: cargo_dwell (Q3 mean import dwell)\n\n" + "\n".join(
    f"{i + 1}. **{s['kind']}**: {s['what failed']}. Fix: {s['fix']}." for i, s in enumerate(steps)) +
    f"\n\nResult: reproduced {final} days against the reported {reported}.\n")

# %% [markdown]
# ## ✱ Stretch · Repository rules
#
# One rule per kind of failure, so the next re-run takes one command.

# %%
rules = {
    "path": "Paths are relative to the repository; nothing points to a personal folder.",
    "documentation": "The README names every input file exactly, and a data manifest lists them with their dates.",
    "missing input": "Every input is in the repository or named with where to get it and who owns it.",
    "library version": "A lock file pins every package (uv.lock); the README names the command that installs from it.",
    "randomness": "Every random step has a fixed seed, written in the code.",
    "manual step": "No step happens outside the code. A hand edit becomes a line of code, or it does not happen.",
}
for k, v in rules.items():
    print(f"- {k}: {v}")

# %% [markdown]
# ## Checkpoint
#
# 1. Which failure was the most dangerous, and why?
#    <details><summary>Answer</summary>The manual step: everything ran, and the figure was wrong by 0.58 days with no
#    error. The other failures stopped the script and announced themselves.</details>
# 2. Why re-run before reading the report?
#    <details><summary>Answer</summary>The report sets your expectations; the re-run tests whether the report can be
#    produced at all from what was handed over.</details>
# 3. Why log the failures instead of just fixing them?
#    <details><summary>Answer</summary>The log is the evidence of the review and the source of the team's repository
#    rules: the same failures recur across analysts.</details>
#
# **Carry forward.** `out/rerun_log.md`. Lab 1.4 starts from `data/guidelines_digest.json`.
