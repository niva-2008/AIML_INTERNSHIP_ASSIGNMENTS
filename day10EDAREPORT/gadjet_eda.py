import pandas as pd
import numpy as np
import sqlite3

print(" PHASE 1 & 2: DATASETS UNDERSTANDING & CLEANING ")

# 1. GENERATE DATASET
raw_data = {
    "TransactionID": [5001, 5002, 5003, 5003, 5005, 5006, 5007, 5008],
    "Customer":      ["anil kumar", "SNEHA", "Rhea", "Rhea", "Vikram", "Neha Sharma", "Amit", "Rajesh"],
    "City":          ["Bengaluru", "mumbai", "Bengaluru", "Bengaluru", "Delhi", "Mumbai", "delhi", "Bengaluru"],
    "ProductType":   ["Smart Watch", "Wireless Pods", "Smart Watch", "Smart Watch", "Laptop", "Wireless Pods", "Laptop", "Smart Watch"],
    "SaleAmount":    [15000, np.nan, 12500, 12500, 85000, 999999, 78000, 14000],
    "UnitsOrdered":  [2, 1, 1, 1, 1, -3, 2, 5],
    "Date":          ["2026-06-01", "2026-06-01", "2026-06-02", "2026-06-02", "2026-06-03", "2026-06-03", "2026-06-04", "2026-06-05"]
}
df = pd.DataFrame(raw_data)
print(f"Initial Shape: {df.shape}")

# 2. DATA CLEANING WORKFLOW
df = df.drop_duplicates(subset=["TransactionID"]).reset_index(drop=True)
df['Date'] = pd.to_datetime(df['Date'])
df['Customer'] = df['Customer'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()

# FIX: Calculate median, round it, and explicitly convert it to a whole integer
raw_median = df.loc[df["UnitsOrdered"] > 0, "UnitsOrdered"].median()
median_units = int(np.round(raw_median)) 

# Now this safely replaces the negative values without type errors
df.loc[df["UnitsOrdered"] < 0, "UnitsOrdered"] = median_units

# Remove structural entry outlier (999999) and impute with robust median
df.loc[df["SaleAmount"] > 200000, "SaleAmount"] = np.nan
df["SaleAmount"] = df["SaleAmount"].fillna(df["SaleAmount"].median())
print("\nCleaned DataFrame Sample:")
print(df)

print("\n PHASE 3 & 4: STATISTICS & REPORT EXPORT ")

# Safely compute statistics for the trainer's report
prod_rev = df.groupby("ProductType")["SaleAmount"].sum().sort_values(ascending=False)

# Create text report file automatically
report_content = f"""======= OFFICIAL EDA REPORT =======
Dataset: E-Commerce Electronic Gadget Sales
Total Transactions Analyzed: {len(df)}
Total Revenue Generated: ₹{df['SaleAmount'].sum():,.2f}

Revenue Contribution by Product Type:
{prod_rev.to_string()}

City-wise Order Counts:
{df['City'].value_counts().to_string()}
=================================="""

with open("EDA_Report_Output.txt", "w", encoding="utf-8") as f:
    f.write(report_content)

print("[SUCCESS] Summary Text Report written to 'EDA_Report_Output.txt'")

print("\n PHASE 5: RDBMS SQL ANALYSIS VERIFICATION ")
conn = sqlite3.connect(":memory:")
df.to_sql("gadget_sales", conn, index=False, if_exists="replace")

sql_query = """
SELECT ProductType, SUM(SaleAmount) AS TotalRevenue 
FROM gadget_sales 
GROUP BY ProductType 
ORDER BY TotalRevenue DESC;
"""
print(pd.read_sql(sql_query, conn))
conn.close()
print("\nExecution Finished Successfully!")