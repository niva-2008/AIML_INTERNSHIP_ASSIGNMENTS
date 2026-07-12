import sqlite3
import pandas as pd

# =====================================================================
# PHASE 1: INITIALIZE CAPSTONE DATABASE & RELATION SCHEMAS (DDL)
# =====================================================================
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.executescript("""
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    CustomerName TEXT NOT NULL,
    City TEXT NOT NULL,
    State TEXT NOT NULL,
    Segment TEXT NOT NULL,
    SignupDate TEXT NOT NULL
);

CREATE TABLE Products (
    ProductID TEXT PRIMARY KEY,
    ProductName TEXT NOT NULL,
    Category TEXT NOT NULL,
    Price INTEGER NOT NULL,
    Cost INTEGER NOT NULL
);

CREATE TABLE Orders (
    OrderID TEXT PRIMARY KEY,
    CustomerID INTEGER,
    OrderDate TEXT NOT NULL,
    Status TEXT NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderItems (
    OrderItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderID TEXT,
    ProductID TEXT,
    Quantity INTEGER NOT NULL,
    UnitPrice INTEGER NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE Payments (
    PaymentID TEXT PRIMARY KEY,
    OrderID TEXT,
    PaymentMode TEXT NOT NULL,
    PaidAmount INTEGER NOT NULL,
    PaymentDate TEXT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
""")

# =====================================================================
# PHASE 2: DATA INGESTION MATRIX
# =====================================================================
customers_data = [
    (1, "Asha Sharma", "Pune", "Maharashtra", "Premium", "2024-02-10"),
    (2, "Ravi Kumar", "Mumbai", "Maharashtra", "Regular", "2024-05-15"),
    (3, "Imran Khan", "Pune", "Maharashtra", "Premium", "2023-11-20"),
    (4, "Divya Rao", "Delhi", "Delhi", "Regular", "2025-01-05"),
    (5, "Karan Mehta", "Mumbai", "Maharashtra", "Premium", "2024-08-30"),
    (6, "Sneha Reddy", "Hyderabad", "Telangana", "Regular", "2024-03-12"),
    (7, "Amit Mishra", "Delhi", "Delhi", "Premium", "2025-03-01"),
    (8, "Priya Nair", "Bengaluru", "Karnataka", "Regular", "2024-09-25")
]

products_data = [
    ("P1", "Organic Avocado Box", "Produce", 1500, 900),
    ("P2", "Premium Almond Milk", "Dairy", 400, 250),
    ("P3", "Artisan Sourdough", "Bakery", 300, 180),
    ("P4", "Gourmet Cheese Platter", "Dairy", 2500, 1600),
    ("P5", "Cold Pressed Juice Pack", "Produce", 1200, 800)
]

orders_data = [
    ("O-1001", 1, "2026-01-12", "Completed"),
    ("O-1002", 2, "2026-01-20", "Completed"),
    ("O-1003", 3, "2026-02-05", "Completed"),
    ("O-1004", 1, "2026-02-18", "Completed"),
    ("O-1005", 4, "2026-03-02", "Completed"),
    ("O-1006", 5, "2026-03-15", "Completed"),
    ("O-1007", 3, "2026-04-10", "Completed"),
    ("O-1008", 6, "2026-04-22", "Cancelled"),
    ("O-1009", 1, "2026-05-08", "Completed"),
    ("O-1010", 7, "2026-05-19", "Completed"),
    ("O-1011", 2, "2026-06-03", "Completed"),
    ("O-1012", 5, "2026-06-14", "Completed"),
    ("O-1013", 1, "2026-06-18", "Completed"),
    ("O-1014", 3, "2026-06-22", "Completed"),
    ("O-1015", 4, "2026-06-25", "Completed")
]

order_items_data = [
    (1, "O-1001", "P1", 10, 1500), (2, "O-1001", "P3", 5, 300),
    (3, "O-1002", "P2", 20, 400),
    (4, "O-1003", "P1", 8, 1500),  (5, "O-1003", "P4", 4, 2500),
    (6, "O-1004", "P5", 15, 1200),
    (7, "O-1005", "P2", 10, 400),  (8, "O-1005", "P3", 10, 300),
    (9, "O-1006", "P1", 12, 1500),
    (10, "O-1007", "P4", 6, 2500),
    (11, "O-1008", "P3", 2, 300),
    (12, "O-1009", "P2", 25, 400), (13, "O-1009", "P5", 5, 1200),
    (14, "O-1010", "P1", 20, 1500), (15, "O-1010", "P4", 8, 2500),
    (16, "O-1011", "P4", 2, 2500),  (17, "O-1011", "P3", 5, 300),
    (18, "O-1012", "P5", 10, 1200),
    (19, "O-1013", "P1", 4, 1500),
    (20, "O-1014", "P2", 15, 400),
    (21, "O-1015", "P4", 3, 2500)
]

payments_data = [
    ("PAY-1", "O-1001", "Card", 16500, "2026-01-12"),
    ("PAY-2", "O-1002", "UPI", 8000, "2026-01-20"),
    ("PAY-3", "O-1003", "Card", 22000, "2026-02-05"),
    ("PAY-4", "O-1004", "UPI", 18000, "2026-02-18"),
    ("PAY-5", "O-1005", "Card", 7000, "2026-03-02"),
    ("PAY-6", "O-1006", "NetBanking", 18000, "2026-03-15"),
    ("PAY-7", "O-1007", "UPI", 15000, "2026-04-10"),
    ("PAY-8", "O-1009", "Card", 16000, "2026-05-08"),
    ("PAY-9", "O-1010", "UPI", 42000, "2026-05-19"),
    ("PAY-10", "O-1011", "Card", 6500, "2026-06-03"),
    ("PAY-11", "O-1013", "Card", 6000, "2026-06-18"),
    ("PAY-12", "O-1014", "UPI", 6000, "2026-06-22"),
    ("PAY-13", "O-1015", "Card", 7500, "2026-06-25")
]

cur.executemany("INSERT INTO Customers VALUES (?,?,?,?,?,?)", customers_data)
cur.executemany("INSERT INTO Products VALUES (?,?,?,?,?)", products_data)
cur.executemany("INSERT INTO Orders VALUES (?,?,?,?)", orders_data)
cur.executemany("INSERT INTO OrderItems VALUES (?,?,?,?,?)", order_items_data)
cur.executemany("INSERT INTO Payments VALUES (?,?,?,?,?)", payments_data)
conn.commit()
print("--- URBAN_GROCER RELATIONAL CAPSTONE INSTANTIATED SUCCESSFULLY ---")

def run(sql_query):
    return pd.read_sql(sql_query, conn)

# =====================================================================
# DATA CAPSTONE SUMMARY REPORTS
# =====================================================================
print("\n[TASK 1: MASTER REVENUE CORE BASELINE KPIs]")
print(run("""
SELECT COUNT(DISTINCT o.OrderID) AS completed_orders,
       COUNT(DISTINCT o.CustomerID) AS active_customers,
       SUM(oi.Quantity * oi.UnitPrice) AS total_gross_revenue,
       ROUND(SUM(oi.Quantity * oi.UnitPrice) * 1.0 / COUNT(DISTINCT o.OrderID), 2) AS average_order_value
FROM Orders o
INNER JOIN OrderItems oi ON o.OrderID = oi.OrderID
WHERE o.Status = 'Completed';
"""))

print("\n[TASK 2: PROFITABILITY & PROFIT MARGIN PER PRODUCT CATEGORY]")
print(run("""
SELECT p.Category,
       SUM(oi.Quantity * oi.UnitPrice) AS category_revenue,
       SUM(oi.Quantity * (oi.UnitPrice - p.Cost)) AS category_net_profit,
       ROUND(SUM(oi.Quantity * (oi.UnitPrice - p.Cost)) * 100.0 / SUM(oi.Quantity * oi.UnitPrice), 1) AS margin_percentage
FROM Orders o
INNER JOIN OrderItems oi ON o.OrderID = oi.OrderID
INNER JOIN Products p ON oi.ProductID = p.ProductID
WHERE o.Status = 'Completed'
GROUP BY p.Category
ORDER BY category_net_profit DESC;
"""))

print("\n[TASK 3: TOP 5 ACCOUNT LEADERBOARD BY REVENUE]")
print(run("""
SELECT c.CustomerName, c.City, SUM(oi.Quantity * oi.UnitPrice) AS total_spending, COUNT(DISTINCT o.OrderID) AS order_frequency
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
INNER JOIN OrderItems oi ON o.OrderID = oi.OrderID
WHERE o.Status = 'Completed'
GROUP BY c.CustomerName, c.City
ORDER BY total_spending DESC
LIMIT 5;
"""))

print("\n[TASK 4: INACTIVE ACCOUNTS ARCHIVE]")
print(run("""
SELECT c.CustomerName, c.City, c.Segment
FROM Customers c
LEFT JOIN (
    SELECT DISTINCT CustomerID FROM Orders WHERE Status = 'Completed'
) active ON c.CustomerID = active.CustomerID
WHERE active.CustomerID IS NULL;
"""))

print("\n[TASK 5: GEOGRAPHIC PERFORMANCE MATRIX BY REGIONAL NODE]")
print(run("""
SELECT c.State, COUNT(DISTINCT o.OrderID) AS order_volume, SUM(oi.Quantity * oi.UnitPrice) AS localized_revenue
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
INNER JOIN OrderItems oi ON o.OrderID = oi.OrderID
WHERE o.Status = 'Completed'
GROUP BY c.State
ORDER BY localized_revenue DESC;
"""))

print("\n[TASK 6: REVENUE LEAKAGE AUDIT - MISSING & UNRECONCILED PAYMENTS]")
print("\n>> 6A: Completed Order Nodes with Missing Payments Completely:")
print(run("""
SELECT o.OrderID, SUM(oi.Quantity * oi.UnitPrice) AS unpaid_billed_total
FROM Orders o
INNER JOIN OrderItems oi ON o.OrderID = oi.OrderID
LEFT JOIN Payments pay ON o.OrderID = pay.OrderID
WHERE o.Status = 'Completed' AND pay.PaymentID IS NULL
GROUP BY o.OrderID;
"""))

print("\n>> 6B: Orders with Shortfall/Underpayment Discrepancies:")
print(run("""
SELECT o.OrderID, 
       SUM(oi.Quantity * oi.UnitPrice) AS aggregate_billed_amount, 
       pay.PaidAmount,
       (SUM(oi.Quantity * oi.UnitPrice) - pay.PaidAmount) AS leakage_shortfall
FROM Orders o
INNER JOIN OrderItems oi ON o.OrderID = oi.OrderID
INNER JOIN Payments pay ON o.OrderID = pay.OrderID
WHERE o.Status = 'Completed'
GROUP BY o.OrderID, pay.PaidAmount
HAVING aggregate_billed_amount <> pay.PaidAmount;
"""))

conn.close()
print("\n--- MASTER ANALYSIS ENGINE SHUTDOWN CLEANLY ---")