import matplotlib.pyplot as plt
import numpy as np

print("--- Day 7: Data Visualization with Matplotlib ---")
print("-" * 50)

# --- 1. SIMULATING INTERNSHIP DATA ---
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [12000, 15000, 13000, 19000, 24000, 22000]
categories = ['Electronics', 'Clothing', 'Home Decor', 'Books']
shares = [40, 30, 15, 15]

# Generating random data for statistical plots (Histogram & Scatter)
np.random.seed(10)
customer_ages = np.random.normal(loc=30, scale=7, size=250)
advertising_budget = np.random.randint(200, 1000, size=50)
matching_revenue = advertising_budget * 1.5 + np.random.normal(0, 100, size=50)


# --- 2. MULTI-PLOT VISUALIZATION SETUP (USING SUBPLOTS) ---
# Creating a 2x3 grid to showcase all 6 major chart types in a single figure window
plt.figure(figsize=(15, 10))

# [Plot 1]: Line Chart (Showing Trends Over Time)
plt.subplot(2, 3, 1)
plt.plot(months, sales, marker='o', color='b', linestyle='--', linewidth=2)
plt.title("Sales Trend (Line Chart)")
plt.xlabel("Months")
plt.ylabel("Revenue ($)")
plt.grid(True, linestyle=':', alpha=0.6)

# [Plot 2]: Bar Chart (Comparing Categorical Values)
plt.subplot(2, 3, 2)
plt.bar(categories, shares, color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Category Share (Bar Chart)")
plt.xlabel("Categories")
plt.ylabel("Percentage (%)")

# [Plot 3]: Scatter Plot (Examining Relationship/Correlation)
plt.subplot(2, 3, 3)
plt.scatter(advertising_budget, matching_revenue, color='purple', alpha=0.7, edgecolors='black')
plt.title("Budget vs Revenue (Scatter Plot)")
plt.xlabel("Ad Budget ($)")
plt.ylabel("Revenue ($)")

# [Plot 4]: Pie Chart (Displaying Relative Proportions)
plt.subplot(2, 3, 4)
plt.pie(shares, labels=categories, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Market Share Distribution (Pie Chart)")

# [Plot 5]: Histogram (Displaying Frequency Distribution)
plt.subplot(2, 3, 5)
plt.hist(customer_ages, bins=15, color='teal', edgecolor='white', alpha=0.8)
plt.title("Customer Age Distribution (Histogram)")
plt.xlabel("Age Groups")
plt.ylabel("Frequency")

# [Plot 6]: Box Plot (Visualizing Summary Statistics & Outliers)
plt.subplot(2, 3, 6)
plt.boxplot(customer_ages, vert=True, patch_artist=True, boxprops=dict(facecolor='lightblue', color='blue'))
plt.title("Age Range Summary (Box Plot)")
plt.ylabel("Ages")

# --- 3. RENDERING AND SAVING THE VISUALIZATIONS ---
plt.tight_layout() # Adjusts spacing perfectly automatically

# Saving the figure layout as a standalone image file for report presentation
plt.savefig("./day7/matplotlib_assignment_output.png", dpi=300)
print("[Success] Replicated all 6 plot styles and compiled them inside 'matplotlib_assignment_output.png'.")

# Presenting the window to screen
plt.show()