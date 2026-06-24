import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("--- Day 8: Statistical Visualization with Seaborn ---")
print("-" * 60)

# --- 1. SETTING THE THEME ---
# Seaborn comes with built-in themes to make plots look attractive out-of-the-box
sns.set_theme(style="darkgrid", palette="muted")

# --- 2. LOADING BUILT-IN DATASETS ---
# Using the standard 'tips' dataset bundled with Seaborn for statistical demonstrations
tips = sns.load_dataset("tips")

print("[Dataset Overview] Sample rows from the 'tips' dataset:")
print(tips.head())
print("-" * 60)

# --- 3. GENERATING PLOTS & VISUALIZATIONS ---

# [Plot 1 & 2]: Distribution and Categorical Trends (Violin Plot & Bar Plot)
plt.figure(figsize=(12, 5))

# Subplot 1: Violin Plot (Shows data distribution density and summary statistics)
plt.subplot(1, 2, 1)
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True, palette="Pastel1")
plt.title("Total Bill Distribution by Day & Gender (Violin Plot)")

# Subplot 2: Bar Plot (Aggregates numerical values with confidence intervals)
plt.subplot(1, 2, 2)
sns.barplot(x="time", y="tip", data=tips, hue="smoker", palette="Set2")
plt.title("Average Tip: Lunch vs Dinner (Bar Plot)")

plt.tight_layout()
plt.show()


# [Plot 3 & 4]: Advanced Relational and Trend Analysis (Regression & Heatmap)
plt.figure(figsize=(14, 5))

# Subplot 1: Regression Plot (Scatter plot combined with a linear regression trendline)
plt.subplot(1, 2, 1)
sns.regplot(x="total_bill", y="tip", data=tips, scatter_kws={'s':15, 'alpha':0.7}, line_kws={'color':'red'})
plt.title("Bill Amount vs Tip Trend (Regression Plot)")

# Subplot 2: Heatmap Matrix (Visualizes linear correlations across numerical metrics)
plt.subplot(1, 2, 2)
# Selecting only numerical attributes to compute a clean correlation matrix
numerical_metrics = tips.select_dtypes(include=[np.number])
correlation_matrix = numerical_metrics.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=1.5)
plt.title("Attribute Multi-Correlation Matrix (Heatmap)")

plt.tight_layout()
plt.show()


# [Plot 5]: FacetGrid Plot (Splitting data views into sub-grids based on categories)
print("Generating categorical multi-plot FacetGrid...")
grid_layout = sns.FacetGrid(tips, col="time", row="sex")
grid_layout.map(sns.scatterplot, "total_bill", "tip", edgecolor="w", alpha=0.8)
plt.show()


# [Plot 6]: Pair Plot (Comprehensive pairwise relationships across the entire dataset)
print("Generating dataset-wide Pair Plot matrix (this may take a moment)...")
pair_plot_matrix = sns.pairplot(tips, hue="sex", palette="husl", diag_kind="kde")
pair_plot_matrix.fig.suptitle("Dataset Pairwise Feature Matrix Overview", y=1.02)
plt.show()

print("\nSeaborn Assignment execution completed successfully!")