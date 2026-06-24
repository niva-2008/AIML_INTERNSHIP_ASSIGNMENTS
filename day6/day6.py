import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for visualizations
sns.set_theme(style="whitegrid")

print("--- Day 6: Exploratory Data Analysis (EDA) ---")
print("-" * 50)

# 1. Simulating an Internship Dataset for EDA
np.random.seed(42)
data_size = 100

eda_data = {
    "Age": np.random.randint(20, 40, size=data_size),
    "Experience_Years": np.random.randint(1, 15, size=data_size),
    "Salary": np.random.randint(30000, 120000, size=data_size),
    "Department": np.random.choice(["IT", "HR", "Marketing", "Sales"], size=data_size)
}

df = pd.DataFrame(eda_data)

# Injecting some artificial missing values to demonstrate data cleaning during EDA
df.loc[df["Age"] < 22, "Salary"] = np.nan 

# --- STEP 1: DATA INSPECTION ---
print("\n[Stage 1] Data Inspection:")
print(f"- Dataset Shape: {df.shape} (Rows, Columns)")
print("\n- Data Types & Structural Overview:")
print(df.info())
print("\n- Basic Descriptive Statistics:")
print(df.describe())
print("-" * 50)

# --- STEP 2: HANDLING MISSING DATA ---
print("\n[Stage 2] Checking and Handling Missing Values:")
print("Missing values per column before fix:")
print(df.isnull().sum())

# Imputing missing salaries with the median value
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print("\nMissing values per column after median imputation:")
print(df.isnull().sum())
print("-" * 50)

# --- STEP 3: UNIVARIATE ANALYSIS (Analyzing One Variable) ---
print("\n[Stage 3] Plotting Univariate Distributions...")
plt.figure(figsize=(12, 5))

# Subplot 1: Histogram for Age Distribution
plt.subplot(1, 2, 1)
sns.histplot(df["Age"], kde=True, color="skyblue")
plt.title("Age Distribution (Histogram)")

# Subplot 2: Box Plot for Salary Outliers
plt.subplot(1, 2, 2)
sns.boxplot(y=df["Salary"], color="salmon")
plt.title("Salary Spread (Box Plot)")

plt.tight_layout()
plt.show() # Closes window to continue script execution

# --- STEP 4: BIVARIATE ANALYSIS (Comparing Two Variables) ---
print("\n[Stage 4] Plotting Bivariate Relationships...")
plt.figure(figsize=(12, 5))

# Subplot 1: Scatter Plot (Experience vs Salary)
plt.subplot(1, 2, 1)
sns.scatterplot(x=df["Experience_Years"], y=df["Salary"], hue=df["Department"], palette="Set2")
plt.title("Experience vs Salary")

# Subplot 2: Bar Plot (Average Salary by Department)
plt.subplot(1, 2, 2)
sns.barplot(x="Department", y="Salary", data=df, estimator=np.mean, palette="Pastel1", hue="Department", legend=False)
plt.title("Average Salary by Department")

plt.tight_layout()
plt.show()

# --- STEP 5: MULTIVARIATE ANALYSIS (Interactions between multiple variables) ---
print("\n[Stage 5] Generating Multivariate Correlation Heatmap...")
plt.figure(figsize=(8, 6))

# Isolating numerical values to compute a correlation matrix
numerical_df = df[["Age", "Experience_Years", "Salary"]]
correlation_matrix = numerical_df.corr()

# Plotting Heatmap
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="Pastel2", linewidths=2)
plt.title("Correlation Heatmap Matrix")
plt.tight_layout()
plt.show()

print("\nEDA Assignment execution completed successfully!")