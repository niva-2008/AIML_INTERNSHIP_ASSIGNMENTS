import pandas as pd

# STEP 1: INITIALIZE RELATION DATASETS & MERGE
#1.1 Load the transactional source tables

customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5],
    "Name": ["Asha", "Ravi", "Imran", "Divya", "Karan"],
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai"],
    "Segment": ["Premium", "Regular", "Premium", "Regular", "Premium"]
})

products = pd.DataFrame({
    "ProductID": ["P1", "P2", "P3"],
    "Product": ["Laptop", "Phone", "Headphones"],
    "Category": ["Electronics", "Electronics", "Accessories"],
    "Price": [60000, 30000, 3000]
})

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108],
    "CustomerID": [1, 2, 1, 3, 4, 5, 1, 3],   
    "ProductID": ["P1", "P2", "P3", "P1", "P2", "P1", "P2", "P3"],
    "Quantity": [1, 2, 3, 1, 1, 1, 2, 5]
})

# 1.2 Perform step-by-step Left Merge to build the full dataset
step1 = pd.merge(orders, customers, on="CustomerID", how="left")
full_dataset = pd.merge(step1, products, on="ProductID", how="left")

# 1.3 Vectorized computation for structural Revenue generation
full_dataset["Revenue"] = full_dataset["Quantity"] * full_dataset["Price"]

print("--- STEP 1: COMPLETED FULL ANALYSIS DATASET ---")
print(full_dataset.head(), "\n")

# STEP 2: MULTI-DIMENSIONAL PIVOT GRIDS

print("--- STEP 2A: PIVOT TABLE - REVENUE BY CITY AND CATEGORY ---")
city_category_pivot = pd.pivot_table(
    full_dataset, 
    index="City", 
    columns="Category", 
    values="Revenue", 
    aggfunc="sum", 
    fill_value=0, 
    margins=True
)
print(city_category_pivot, "\n")

print("--- STEP 2B: PIVOT TABLE - REVENUE BY SEGMENT AND PRODUCT ---")
segment_product_pivot = pd.pivot_table(
    full_dataset, 
    index="Segment", 
    columns="Product", 
    values="Revenue", 
    aggfunc="sum", 
    fill_value=0
)
print(segment_product_pivot, "\n")


# STEP 3: EXECUTIVE KPI REPORTS

print("--- STEP 3A: REVENUE BY CITY (RANKED) ---")
revenue_by_city = full_dataset.groupby("City")["Revenue"].sum().sort_values(ascending=False).reset_index()
print(revenue_by_city, "\n")

print("--- STEP 3B: REVENUE BY CUSTOMER SEGMENT ---")
revenue_by_segment = full_dataset.groupby("Segment")["Revenue"].sum().reset_index()
print(revenue_by_segment, "\n")

print("--- STEP 3C: TOP PERFORMING CUSTOMER ID DETECTED ---")
top_customer_name = full_dataset.groupby("Name")["Revenue"].sum().idxmax()
top_customer_val = full_dataset.groupby("Name")["Revenue"].sum().max()
print(f"Top Customer: {top_customer_name} (Total Spend: ₹{top_customer_val:,})\n")

print("--- STEP 3D: REVENUE BY PRODUCT CATEGORY ---")
revenue_by_category = full_dataset.groupby("Category")["Revenue"].sum().reset_index()
print(revenue_by_category, "\n")

# STEP 4: CATEGORICAL FREQUENCY ANALYSIS

print("--- STEP 4: CROSSTAB - ORDER COUNT BY CITY AND CATEGORY ---")
order_frequency_matrix = pd.crosstab(full_dataset["City"], full_dataset["Category"])
print(order_frequency_matrix, "\n")