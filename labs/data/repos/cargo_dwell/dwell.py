"""Mean import dwell for the quarterly note. Saleh Al-Ghamlas. Tested with pandas 1.5."""
import pandas as pd

DATA = r"C:\Users\saleh\Desktop\port\containers.csv"  # academy:example (the planted absolute path)

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
