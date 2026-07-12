import pandas as pd
import numpy as np


# STEP 1: INITIALIZE RAW MESSSY DATASET

raw = pd.DataFrame({
    "OrderID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Customer": ["  asha sharma", "RAVI KUMAR", "imran khan", "asha sharma",
                 "DIVYA rao", "ravi kumar", "Karan MEHTA", "asha sharma"],
    "Email": ["asha@gmail.com", "ravi@company.com", "imran@yahoo.com", "asha@gmail.com",
              "divya@company.com", "ravi@company.com", "karan@gmail.com", "asha@gmail.com"],
    "OrderDate": ["2026-01-12", "2026-02-18", "2026-03-22", "2026-04-15",
                  "2026-05-20", "2026-06-01", "2026-06-08", "2026-06-15"],
    "Category": ["Electronics", "Grocery", "Electronics", "Clothing",
                 "Grocery", "Electronics", "Clothing", "Electronics"],
    "Units": [2, 12, 1, 5, 9, 3, 4, 1],
    "UnitPrice": [30000, 200, 60000, 1500, 250, 25000, 1200, 45000],
    "UnitCost": [22000, 150, 45000, 900, 180, 18000, 800, 33000]
})

print("--- STEP 1: RAW DATA LOADED ---")


# STEP 2 & 3: CLEAN TEXT & DERIVED METRICS

# 2.1 Standardize names to Title Case and strip white spaces
raw["Customer"] = raw["Customer"].str.strip().str.title()

# 2.2 Convert order date strings to real datetime elements
raw["OrderDate"] = pd.to_datetime(raw["OrderDate"])

# 3.1 Vectorized calculations for Revenue, Cost, Profit, and Margins
raw["Revenue"] = raw["Units"] * raw["UnitPrice"]
raw["Cost"] = raw["Units"] * raw["UnitCost"]
raw["Profit"] = raw["Revenue"] - raw["Cost"]
raw["Margin%"] = (raw["Profit"] / raw["Revenue"] * 100).round(1)


# STEP 4 & 5: EXTRACT DATE & STRINGS & BINNING

# 4.1 Chronological feature partitioning
raw["Month"] = raw["OrderDate"].dt.month_name()
raw["Quarter"] = raw["OrderDate"].dt.quarter

# 4.2 Text extraction processing (First Names & Email Domains)
raw["FirstName"] = raw["Customer"].str.split(" ").str[0]
raw["EmailDomain"] = raw["Email"].str.split("@").str[1]

# 4.3 B2B Corporate vs B2C Personal Segmentation Flag
raw["CustomerType"] = np.where(raw["EmailDomain"] == "company.com", "Corporate", "Personal")

# 5.1 Continuous feature bucketing using fixed bounds
raw["OrderSize"] = pd.cut(raw["Revenue"], bins=[0, 5000, 50000, 1000000],
                          labels=["Small", "Medium", "Large"])

# 5.2 Conditional categorization matrix
raw["HighMargin"] = np.where(raw["Margin%"] >= 25, "Yes", "No")

# STEP 6: WINDOW AGGREGATIONS (BROADCASTING KPIs)

# Broadcast cumulative customer spend profile per transaction row without collapsing matrix rows
raw["TotalSpend"] = raw.groupby("Customer")["Revenue"].transform("sum")
raw["OrderCount"] = raw.groupby("Customer")["OrderID"].transform("count")

print("\n--- TRANSLATED ANALYTICAL REPOSITORY SCHEMA ---")
print(raw.head(3))


# STEP 7: COMPREHENSIVE DATA VALIDATION CHECK

print("\n--- STEP 7: REPOSITORY STRUCTURAL VALIDATION ---")
missing_count = raw.isnull().sum().sum()
neg_profit_count = (raw["Profit"] < 0).sum()
invalid_margin_count = raw[(raw["Margin%"] < 0) | (raw["Margin%"] > 100)].shape[0]

print(f"Missing Values Discovered: {missing_count}")
print(f"Negative Profit Rows Flagged: {neg_profit_count}")
print(f"Invalid Out-of-Range Margins Flagged: {invalid_margin_count}")

# STEP 8: BUSINESS INTELLIGENCE COMPILATION

print("\n--- STEP 8: METRIC GENERATION EXTRACTION ---")
print("\n[Net Profit Contribution Ranked by Product Category]")
print(raw.groupby("Category")["Profit"].sum().sort_values(ascending=False))

top_customer = raw.groupby("Customer")["Revenue"].sum().idxmax()
print(f"\n[Top Performing Account Node]: {top_customer}")

print("\n[Revenue Generation Matrix by Account Classification]")
print(raw.groupby("CustomerType")["Revenue"].sum())