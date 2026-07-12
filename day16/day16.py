import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency


print(" SCENARIO 1: LOYALTY PROGRAMME PERFORMANCE AUDIT (PAIRED T-TEST)     ")

# 1.1 Ingest paired baseline spending logs for the SAME 12 accounts (Before vs After)
spending_before = [4200, 5100, 3800, 6200, 4900, 5500, 3100, 4800, 5300, 4400, 6000, 5200]
spending_after  = [4800, 5600, 4100, 6900, 5000, 6100, 3300, 5400, 5900, 4500, 6700, 5800]

# 1.2 Execute Paired t-Test (controls for distinct account variation)
t_stat_1, p_val_1 = stats.ttest_rel(spending_before, spending_after)

print(f"Hypotheses formulated -> H0: Spending is unchanged | H1: Spending significantly shifted")
print(f"Calculated t-statistic: {t_stat_1:.3f}")
print(f"Extracted p-value:     {p_val_1:.6f}")

# 1.3 Trigger Automated Decision Rule Matrix (Alpha = 0.05)
if p_val_1 < 0.05:
    print("Decision: REJECT H0 - The loyalty initiative drove statistically significant change.\n")
else:
    print("Decision: FAIL TO REJECT H0 - Changes fall within natural variation bounds.\n")


print(" SCENARIO 2: STORES REVENUE RECONCILIATION AUDIT (INDEPENDENT T-TEST)")

# 2.1 Ingest daily operational sales files across 10 separate days for two distinct stores
store_north_sales = [125000, 138000, 142000, 119000, 131000, 145000, 128000, 134000, 140000, 122000]
store_south_sales = [118000, 121000, 115000, 124000, 110000, 129000, 117000, 123000, 116000, 120000]

# 2.2 Execute Independent Two-Sample t-Test (unrelated groups comparison)
t_stat_2, p_val_2 = stats.ttest_ind(store_north_sales, store_south_sales)

print(f"Hypotheses formulated -> H0: Stores have equal means | H1: Stores have distinct mean volumes")
print(f"Calculated t-statistic: {t_stat_2:.3f}")
print(f"Extracted p-value:     {p_val_2:.6f}")

if p_val_2 < 0.05:
    print("Decision: REJECT H0 - The two retail spaces operate at fundamentally distinct levels.\n")
else:
    print("Decision: FAIL TO REJECT H0 - Performance gaps are statistically negligible.\n")



print(" SCENARIO 3: REGIONAL MARKET ASSORTMENT AUDIT (CHI-SQUARE TEST)      ")

# 3.1 Construct categorical Contingency frequency counts matrix
# Rows map to 3 Regions (West, South, East); Columns map to 3 Categories (Produce, Dairy, Bakery)
observed_preferences = np.array([
    [65, 40, 20],  # Region West
    [25, 55, 45],  # Region South
    [42, 30, 53]   # Region East
])

# 3.2 Execute Chi-Square Test of Independence
chi2_stat, p_val_3, dof, expected_matrix = chi2_contingency(observed_preferences)

print(f"Hypotheses formulated -> H0: Choice is Independent of Region | H1: Choice Covaries with Region")
print(f"Calculated Chi-Square:  {chi2_stat:.3f}")
print(f"Extracted p-value:      {p_val_3:.6f}")
print(f"System Degrees of Freedom: {dof}")

if p_val_3 < 0.05:
    print("Decision: REJECT H0 - Product preferences vary significantly across geographic locations.\n")
else:
    print("Decision: FAIL TO REJECT H0 - Regional distributions are statistically independent.\n")