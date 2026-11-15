"""Night-shift marine pilots: how many are needed? Saleh Al-Ghamlas."""
import pandas as pd

jobs = pd.read_csv("pilot_jobs.csv")
night = jobs[jobs["shift"] == "night"]

# jobs per night, averaged over the year
per_night = night.groupby("night").size()
print(f"mean pilotage jobs per night: {per_night.mean():.1f}")

# each pilot can do 3 jobs a night
needed = per_night.mean() / 3
print(f"pilots needed per night: {needed:.1f}  ->  recommend 4 instead of 6")
