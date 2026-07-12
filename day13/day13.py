import sqlite3
import pandas as pd


# STEP 1: ESTABLISH DATABASE CONFIGURATION

# Establish an optimized in-memory relational environment for validation
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()


# STEP 2: DDL DEFINITIONS (RELATIONAL SCHEMAS)

cursor.execute("""
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    CustomerName TEXT NOT NULL,
    City TEXT NOT NULL,
    Segment TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE Products (
    ProductID TEXT PRIMARY KEY,
    ProductName TEXT NOT NULL,
    Category TEXT NOT NULL,
    Price INTEGER NOT NULL
);
""")

cursor.execute("""
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    ProductID TEXT,
    Quantity INTEGER NOT NULL,
    OrderAmount INTEGER NOT NULL,
    OrderDate TEXT NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
""")


# STEP 3: DATA INGESTION ENGINE

# Load 8 customers, 5 cross-category products, and 15 targeted transactions
dataset_customers = [
    (1, "Asha Sharma", "Pune", "Premium"),
    (2, "Ravi Kumar", "Mumbai", "Regular"),
    (3, "Imran Khan", "Pune", "Premium"),
    (4, "Divya Rao", "Delhi", "Regular"),
    (5, "Karan Mehta", "Mumbai", "Premium"),
    (6, "Sneha Reddy", "Hyderabad", "Regular"),
    (7, "Amit Mishra", "Delhi", "Premium"),
    (8, "Priya Nair", "Bengaluru", "Regular")
]

dataset_products = [
    ("P1", "Laptop", "Electronics", 60000),
    ("P2", "Phone", "Electronics", 30000),
    ("P3", "Headphones", "Accessories", 3000),
    ("P4", "Smartwatch", "Electronics", 15000),
    ("P5", "Mouse", "Accessories", 1200)
]

dataset_orders = [
    (101, 1, "P1", 1, 60000, "2026-05-01"),
    (102, 2, "P2", 2, 60000, "2026-05-02"),
    (103, 1, "P3", 3, 9000,  "2026-05-03"),
    (104, 3, "P1", 1, 60000, "2026-05-05"),
    (105, 4, "P2", 1, 30000, "2026-05-07"),
    (106, 5, "P1", 1, 60000, "2026-05-08"),
    (107, 1, "P2", 2, 60000, "2026-05-09"),
    (108, 3, "P3", 5, 15000, "2026-05-10"),
    (109, 6, "P4", 1, 15000, "2026-05-12"),
    (110, 7, "P1", 2, 120000,"2026-05-15"),
    (111, 2, "P5", 4, 4800,  "2026-05-16"),
    (112, 8, "P2", 1, 30000, "2026-05-18"),
    (113, 4, "P3", 2, 6000,  "2026-05-20"),
    (114, 5, "P5", 2, 2400,  "2026-05-22"),
    (115, 1, "P4", 1, 15000, "2026-05-25")
]

cursor.executemany("INSERT INTO Customers VALUES (?,?,?,?)", dataset_customers)
cursor.executemany("INSERT INTO Products VALUES (?,?,?,?)", dataset_products)
cursor.executemany("INSERT INTO Orders VALUES (?,?,?,?,?,?)", dataset_orders)
conn.commit()
print("--- RELATIONAL DATABASE INSTANTIATED AND POPULATED ---")


# STEP 4: MASTER TRANSACTON JOIN REPORT

print("\n[REPORT 1: MASTER MULTI-TABLE DATASET]")
sql_master = """
SELECT o.OrderID, c.CustomerName, c.City, p.ProductName, p.Category, o.Quantity, o.OrderAmount
FROM Orders o
INNER JOIN Customers c ON o.CustomerID = c.CustomerID
INNER JOIN Products p ON o.ProductID = p.ProductID;
"""
print(pd.read_sql(sql_master, conn).head(5))


# STEP 5: CORPORATE LEVEL KPI METRICS

print("\n[REPORT 2: CORPORATE KEY PERFORMANCE INDICATORS]")
sql_kpis = """
SELECT COUNT(*) AS total_orders,
       COUNT(DISTINCT CustomerID) AS unique_customers,
       SUM(OrderAmount) AS total_revenue,
       AVG(OrderAmount) AS average_order_value
FROM Orders;
"""
print(pd.read_sql(sql_kpis, conn))


# STEP 6: BUSINESS REPORT GENERATION (CONT.)

print("\n[REPORT 5: GEOGRAPHIC PERFORMANCE BREAKDOWN]")
sql_city = """
SELECT c.City, 
       COUNT(o.OrderID) AS order_count, 
       SUM(o.OrderAmount) AS total_revenue
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.City
ORDER BY total_revenue DESC;
"""
print(pd.read_sql(sql_city, conn))

# Cleanly close the transactional session memory connection
conn.close()
print("\n--- MASTER ANALYSIS ENGINE SHUTDOWN CLEANLY ---")