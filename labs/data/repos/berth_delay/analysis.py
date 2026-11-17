"""Berth waiting before and after slot booking at T2. Run: python analysis.py"""
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
