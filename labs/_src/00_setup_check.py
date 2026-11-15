# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///

# %% [markdown]
# # Setup check
#
# Run this before Day 1. It finds the labs folder, imports every library the labs use, reads one data file of the case
# study, and says whether a free hosted model answers. Every lab runs without a model: the tutor cells then use a
# stand-in that says so.

# %%
import os, sys, subprocess
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

# %%
missing = []
for lib in ("pandas", "numpy"):
    try:
        __import__(lib)
    except ImportError:
        missing.append(lib)
print("missing libraries:", missing or "none")
assert not missing, missing

import rassahil as U

calls = U.csv("berth_calls")
print(f"berth_calls.csv: {len(calls):,} vessel calls, {calls.terminal.nunique()} terminals, {calls.month.nunique()} months")
assert len(calls) == 9_600

# %%
reply = U._call([{"role": "user", "content": "Answer with one word: ready"}], timeout=30)
print("hosted model:", "answered" if reply else "none; labs use stand-ins")
print("setup complete")
