import pandas as pd
import numpy as np

print("--- Day 4: Pandas Core Structures ---")
# 1D Series Layout
sports = pd.Series(["Cricket", "Football", "Tennis"], name="Sports")
print(sports)

print("\n--- Day 4: Data Preprocessing ---")
# 2D DataFrame Layout with missing data
raw_data = {
    "Name": ["Aryan", "Harsh", "Kunal"],
    "Age": [25, np.nan, 30],
    "Salary_Amount": [np.nan, 5000, 7000]
}
df = pd.DataFrame(raw_data)
# Handling missing data using fillna
df["Salary_Amount"] = df["Salary_Amount"].fillna(0)
print(df)