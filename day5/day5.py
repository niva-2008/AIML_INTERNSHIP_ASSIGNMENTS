import pandas as pd

print("--- Day 5: Data Cleaning Techniques ---")
# Dataset with duplicate rows and bad casing
noisy_data = {
    "Student_ID": [101, 102, 101],
    "Name": ["Ananya", "Amit", "Ananya"],
    "City": ["mumbai", "Delhi", "mumbai"]
}
df = pd.DataFrame(noisy_data)

# 1. Removing Duplicates
df = df.drop_duplicates()
# 2. Standardizing capitalization
df["City"] = df["City"].str.title()

print("Cleaned Dataset:")
print(df)