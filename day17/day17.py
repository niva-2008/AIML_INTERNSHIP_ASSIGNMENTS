import numpy as np
import pandas as pd

# STEP 1: DATA SYNTHESIS WITH CHROMATIC INDEXING (730 DAYS MATRIX)

np.random.seed(42)
# Generate a continuous 2-year daily chronological timeline (2024 & 2025)
date_index = pd.date_range(start="2024-01-01", end="2025-12-30", freq="D")
n_days = len(date_index)

# Engineering structural timeline variables: Upward Trend + Q4 Seasonal Spike + Noise
linear_trend = np.linspace(5000, 9000, n_days)
random_noise = np.random.normal(loc=0, scale=300, size=n_days)

df = pd.DataFrame({"Sales": linear_trend + random_noise}, index=date_index)

# Injecting the annual Q4 (October, November, December) retail surge pattern
df["Month_Num"] = df.index.month
df.loc[df["Month_Num"].isin([10, 11, 12]), "Sales"] += 2500

# Final clean up of metric data values
df["Sales"] = df["Sales"].round(0)
df.drop(columns=["Month_Num"], inplace=True)

print("--- STEP 1 & 2: TIMELINE REPOSITORY GENERATED & DATETIME VERIFIED ---")
print(f"Index Datatype: {df.index.dtype}")
print(f"Total Logged Timeline Rows: {len(df)} days")
print(df.head(3), "\n")


# STEP 3: TEMPORAL COMPONENT ATTRIBUTE EXTRACTION

# Extracting explicit properties utilizing the datetime index accessor attributes
df["Year"] = df.index.year
df["Quarter"] = df.index.quarter
df["MonthName"] = df.index.month_name()
df["DayOfWeek"] = df.index.day_name()

print("--- STEP 3: TEMPORAL FEATURE ARRAYS EXTRACTED ---")
print(df[["Sales", "Year", "Quarter", "MonthName", "DayOfWeek"]].head(3), "\n")

# STEP 4: TIME-BASED ACCUMULATION & RESAMPLING

print("--- STEP 4: PERIODIC RESAMPLING SUMMARIES ---")
# FIXED: Utilizing "ME" and "QE" to support modern Pandas releases
monthly_summary = df["Sales"].resample("ME").sum().to_frame(name="TotalMonthlySales")
quarterly_summary = df["Sales"].resample("QE").sum().to_frame(name="TotalQuarterlySales")

print("[Monthly Aggregated Financial View - First 5 Months]")
print(monthly_summary.head(5))
print("\n[Quarterly Aggregated Financial View - Full Timeline]")
print(quarterly_summary)

# STEP 5: TREND SMOOTHING VIA ROLLING WINDOWS (NOISE ELIMINATION)

print("\n--- STEP 5: TREND SMOOTHING OPERATORS ---")
# Apply a 30-day simple moving average window to erase daily transactional noise
df["SmoothedTrend_30D"] = df["Sales"].rolling(window=30).mean()
print(df[["Sales", "SmoothedTrend_30D"]].dropna().head(5))


# STEP 6: SEASONALITY DETECTION LOGS

print("\n--- STEP 6: SEASONALITY PATTERN CROSS-VALIDATION ---")
# Group by Year and Quarter to explicitly check if the Q4 pattern repeats perfectly
seasonal_audit = df.groupby(["Year", "Quarter"])["Sales"].mean().unstack(level=0)
print("[Mean Daily Sales Volumes Partitioned by Year and Quarter]")
print(seasonal_audit.round(0))

# STEP 7: COMPUTE CORE MOM & YOY GROWTH STRATEGIC KPIs

print("\n--- STEP 7: STRATEGIC MOM & YOY TRACKING METRICS ---")
# Calculate Month-over-Month percentage momentum changes
monthly_summary["MoM_Growth%"] = monthly_summary["TotalMonthlySales"].pct_change() * 100

# Calculate Year-over-Year changes comparing current month to exactly 12 intervals prior
monthly_summary["YoY_Growth%"] = monthly_summary["TotalMonthlySales"].pct_change(periods=12) * 100

print(monthly_summary.dropna().round(2))