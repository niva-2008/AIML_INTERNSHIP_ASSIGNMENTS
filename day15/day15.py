import numpy as np
import pandas as pd


# STEP 1: DATA SYNTHESIS & INGESTION (MINIMUM 15 TRANSACTING ACCOUNTS)

# Constructing a 15-customer matrix with an intentional high-value outlier (Customer 15)
data_matrix = {
    "CustomerID": [f"C-{i:02d}" for i in range(1, 16)],
    "Age": [25, 32, 28, 45, 31, 52, 29, 38, 41, 27, 35, 48, 22, 50, 43],
    "AnnualSpending": [12000, 25000, 8000, 30000, 18000, 10000, 22000, 15000, 28000, 19000, 24000, 31000, 9500, 33000, 250000],
    "Visits": [5, 12, 3, 15, 8, 4, 11, 7, 13, 9, 10, 14, 4, 16, 25],
    "AvgBasketValue": [2400, 2083, 2667, 2000, 2250, 2500, 2000, 2143, 2154, 2111, 2400, 2214, 2375, 2063, 10000]
}

df = pd.DataFrame(data_matrix)
print("--- STEP 1: METROMART CUSTOMER REPOSITORY SCHEMATIZED ---")
print(df.head(3), "\n")


# STEP 2 & 3: CENTRAL TENDENCY, DISPERSION, & DISTRIBUTION PROFILING

print("--- STEPS 2 & 3: DESCRIPTIVE METRIC ANALYSIS ---")
mean_spend = df["AnnualSpending"].mean()
median_spend = df["AnnualSpending"].median()
# Mode calculation for continuous/discrete columns can yield multi-value series, extract first
mode_spend = df["AnnualSpending"].mode()[0]

range_spend = df["AnnualSpending"].max() - df["AnnualSpending"].min()
std_spend = df["AnnualSpending"].std() # Pandas defaults to sample standard deviation (n-1)
q1_spend = df["AnnualSpending"].quantile(0.25)
q3_spend = df["AnnualSpending"].quantile(0.75)
iqr_spend = q3_spend - q1_spend

print(f"Mean Spending:           ₹{mean_spend:,.2f}")
print(f"Median Spending:         ₹{median_spend:,.2f}")
print(f"Mode Spending:           ₹{mode_spend:,.2f}")
print(f"Absolute Range:          ₹{range_spend:,.2f}")
print(f"Standard Deviation (s):  ₹{std_spend:,.2f}")
print(f"Interquartile Range(IQR): ₹{iqr_spend:,.2f}")

# Distribution Classification via Mean-Median Diagnostic
if mean_spend > median_spend:
    distribution_shape = "Right-Skewed (Positive Skew)"
elif mean_spend < median_spend:
    distribution_shape = "Left-Skewed (Negative Skew)"
else:
    distribution_shape = "Symmetric (Normal / Bell-Shaped)"
print(f"Classified Distribution:  {distribution_shape}\n")

# STEP 4: PERCENTILE RANKING THRESHOLDS

print("--- STEP 4: PREMIUM CUSTOMER SEGMENTATION THRESHOLD ---")
top_10_percent_threshold = df["AnnualSpending"].quantile(0.90)
print(f"Top 10% Spending Cutoff: ₹{top_10_percent_threshold:,.2f}")
print(f"Accounts exceeding threshold: {df[df['AnnualSpending'] >= top_10_percent_threshold]['CustomerID'].tolist()}\n")


# STEP 5: PAIRWISE CORRELATION MATRIX

print("--- STEP 5: CORRELATION INTERLINKING MATRICES ---")
correlation_matrix = df[["Age", "AnnualSpending", "Visits", "AvgBasketValue"]].corr()
print(correlation_matrix.round(3), "\n")


# STEP 6: ADVANCED OUTLIER CROSS-VALIDATION CRITERIA

print("--- STEP 6: ANOMALY AUDIT AND OUTLIER CROSS-VALIDATION ---")
# 6.1 IQR Anomaly Detection Rule
lower_iqr_bound = q1_spend - 1.5 * iqr_spend
upper_iqr_bound = q3_spend + 1.5 * iqr_spend
iqr_outliers = df[(df["AnnualSpending"] < lower_iqr_bound) | (df["AnnualSpending"] > upper_iqr_bound)]

# 6.2 Z-Score / Standard Deviation Anomaly Detection Rule (Threshold = 2.0 due to sample scale)
mean_s = df["AnnualSpending"].mean()
std_s = df["AnnualSpending"].std()
df["Z_Score"] = (df["AnnualSpending"] - mean_s) / std_s
z_outliers = df[df["Z_Score"].abs() > 2.0]

print(f"IQR Method Flagged Outliers (Bounds: ₹{lower_iqr_bound} - ₹{upper_iqr_bound}):")
print(iqr_outliers[["CustomerID", "AnnualSpending"]])

print(f"\nZ-Score Method Flagged Outliers (Threshold > 2.0 standard deviations):")
print(z_outliers[["CustomerID", "AnnualSpending", "Z_Score"]])


# STEP 7: CORPORATE STRATEGIC SUMMARY LOG

print("\n--- STEP 7: EXECUTIVE FINDINGS EXECUTIVE REPORT ---")
print(f"1. TYPICAL ACCOUNT PROFILE: The arithmetic mean (₹{mean_spend:,.0f}) is mathematically pulled upwards due to intense positive skew.")
print(f"   Therefore, the robust median value of ₹{median_spend:,.0f} serves as the honest indicator of standard performance.")
print("2. KEY RELATIONSHIPS: A strong positive correlation exists between 'Visits' and 'AnnualSpending'.")
print("   *Caveat*: This indicates strong linear covariance, but does not mathematically confirm direct causality.")
print(f"3. ANOMALY TREATMENT: Both filtering architectures successfully isolated account '{iqr_outliers.iloc[0]['CustomerID']}' as an extreme outlier.")
print("   Action: Maintain separate tracking logs for this extreme B2B hub to avoid distorting corporate baselines.")