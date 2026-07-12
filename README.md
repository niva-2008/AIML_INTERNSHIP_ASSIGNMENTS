# AIML Internship - Phase 2

Welcome to repository! This document serves as an exhaustive tracking log and syllabus breakdown for all hands-on milestones completed during this internship phase.


## 📅 Day-by-Day Assignment Details & Explanations

### 🔹 Day 3: NumPy Fundamentals
* **Topic Explanation:** This module establishes a strong foundational grasp of numerical computation using the NumPy framework. The assignment involved initializing single and multi-dimensional arrays, performing vectorization to eliminate resource-intensive Python loops, and experimenting with broadcasting rule sets. Additionally, core matrix operations such as indexing, boolean slicing, reshaping arrays, and computing matrix dot products were thoroughly explored to build efficiency in handling high-dimensional mathematical datasets.
* **Applied Link:** [day3 assignment](./day3/day3.py)

### 🔹 Day 4: Pandas Core Structures
* **Topic Explanation:** This day introduced structured data manipulation principles through the introduction of Pandas Series and DataFrames. The assignment focused on loading raw structured data layouts, aligning indices, and selecting specific data columns or rows via structural indexing techniques (`loc` and `iloc`). Early-stage data integration strategies were applied alongside elementary data-imputation techniques to manage incomplete features, providing a fundamental step toward building flexible, clean data pipelines.
* **Applied Link:** [day4 assignment](./day4/day4.py)

### 🔹 Day 5: Data Cleaning Techniques
* **Topic Explanation:** Real-world datasets are fundamentally messy, and this assignment targeted the structural steps required to fix them. The process involved identifying and scrubbing duplicate rows (`drop_duplicates`), correcting data type mismatches, and handling anomalous string properties across object-type features. By standardizing formatting irregularities and establishing hard data constraints, this module highlighted how systematic data preparation drastically improves data integrity prior to modeling.
* **Applied Link:** [day5 assignment](./day5/day5.py)

### 🔹 Day 6: Exploratory Data Analysis (EDA)
* **Topic Explanation:** This assignment implemented a full Exploratory Data Analysis (EDA) pipeline designed to summarize data structure and uncover hidden patterns. Data inspections were carried out to extract shape parameters, numerical statistics, and missing data maps. Both univariate and bivariate distributions were assessed to identify structural data distributions and spot outliers, concluding with a multivariate correlation matrix to isolate structural associations among features before applying statistical modeling.
* **Applied Link:** [day6 assignment](./day6/day6.py)

### 🔹 Day 7: Data Visualization with Matplotlib
* **Topic Explanation:** This module centered on mastering low-level canvas plotting control to construct clean, customizable data graphics from scratch. The assignment mapped out the six principal chart variants: Line charts for trends, Bar charts for categories, Scatter plots for relationships, Pie charts for proportions, Histograms for frequency distributions, and Box plots for outlier summaries. Advanced layouts were structured using multi-panel canvas grids (`subplots`) to compile multiple graphics into unified figures.
* **Applied Link:** [day7 assignment](./day7/day7.py)

### 🔹 Day 8: Statistical Layouts with Seaborn
* **Topic Explanation:** Building upon basic graphics, this module leveraged Seaborn’s high-level statistical plotting features to create complex and polished visualizations. The assignment implemented split Violin plots to examine distribution densities across groups, linear regression lines (`regplot`) to map relationships between continuous metrics, and annotated correlation heatmaps. It also introduced FacetGrids for multi-conditional subplots and Pair Plots for sweeping, dataset-wide matrix evaluations.
* **Applied Link:** [day8 assignment](./day8/day8.py)

### 🔹 Day 9: Introduction to SQL (SELECT, WHERE, ORDER BY)
* **Topic Explanation:** This module marked the transition from flat-file architectures to robust Relational Database Management Systems (RDBMS). Utilizing Python's native `sqlite3` module integrated with Pandas DataFrames, the assignment focused on declarative data retrieval pipelines. Key operations explored included selecting specific structural attributes, implementing conditional filter logic using text and numerical parameters (`WHERE`), combining constraints via boolean operators (`AND`/`OR`), and configuring explicit multi-field sorting priorities (`ORDER BY`).
* **Applied Link:** [day9 assignment](./day9/day9.py)
*
### 🔹 Day 10:  EDA Report
* [cite_start]**Topic Explanation:** The culmination of the Foundation phase involved executing a comprehensive, end-to-end Exploratory Data Analysis workflow on a messy retail transaction dataset[cite: 35, 50, 150]. [cite_start]The project integrated advanced data cleaning (handling type mismatches, unique key deduplication, and treating extreme input typos through median value imputation) with structured statistical grouping[cite: 230, 260, 278]. [cite_start]Findings were compiled into an industry-standard executive report highlighting revenue engines, customer segments, and strategic inventory mitigation roadmaps[cite: 365, 368].
* **Applied Link:** [day10 assessment](./day10EDAREPORT/gadjet_eda.py).
### 📊 Day 11: Advanced Pandas & Multi-Table Analytics
* **Core Competencies:** Relational left merging (`pd.merge`), two-dimensional pivot tables, frequency distribution matrices (`pd.crosstab`), and multi-level data aggregation via named functions.
* **Project Deliverable:** Completed the "ShopVerse" multi-table commercial analytics challenge, consolidating customer profile, inventory registry, and order stream datasets into unified tracking reports.

#### 💡 Core Business Insights & Analytical Summary:
1. **Premium Segment Domination:** A highly concentrated pool of *Premium Segment* accounts drives the vast majority of net business revenue compared to the low-yield *Regular* customer group.
2. **Geographic Sales Hub:** *Pune* stands out as the highest-grossing market node, anchored heavily by our star customer, **Asha**, who consistently posts multiple high-ticket electronics conversions.
3. **High-Value vs. High-Volume Disconnect:** While low-margin *Accessories (Headphones)* capture high transaction quantities, high-ticket *Electronics (Laptops)* form the absolute financial pillar of net profitability.

#### 🚀 Programmatic Strategy Recommendations:
* **Retention Asset Allocation:** Instantiate a tailored high-tier customer loyalty framework exclusively optimizing retention metrics for top spenders (e.g., Asha).
* **Inventory Supply Prioritization:** Aggressively secure and prioritize electronic device stock distribution hubs mapped directly to high-yield regions (Pune and Mumbai).
* **Cross-Selling Funnels:** Deploy low-value utility hardware categories as immediate site conversion hooks, engineering up-sell flows directing customer traffic toward electronic units.
### 🔧 Day 12: Data Transformation & Feature Creation
* **Core Competencies:** Vectorized math partitioning, text parsing architectures (`.str`), date/time attribute decomposition, numerical binning (`pd.cut`), condition tracking matrices (`np.where`), and data validation check frameworks.
* **Project Deliverable:** Completed the "MartPro" commercial feature engineering challenge, creating 10+ analytical metrics (including conversion types, chronological quarters, and customer spending metrics) out of raw system transaction tables.

#### 💡 Core Business Insights & Analytical Summary:
1. **Profit Optimization Vectors:** The *Electronics* vertical operates as our main profit driver, powered entirely by premium high-ticket laptop acquisitions.
2. **Account Retention Targets:** **Asha Sharma** sits as our highest-value customer hub, locking in multiple cross-category electronics purchases and dominating total spending records.
3. **B2B Sector Dynamics:** The data highlights a strong performance variance between *Corporate (B2B)* corporate domains and *Personal (B2C)* consumer traffic, suggesting clear areas for targeted sales approaches.

#### 🚀 Programmatic Strategy Recommendations:
* **Inventory Balancing:** Secure high-end high-ticket product availability during peak regional quarters mapped to high-value transactions.
* **Loyalty Priority Funnels:** Set up a proactive VIP outreach channel targeting repeat accounts (e.g., Asha Sharma) to sustain customer lifetime value.
* **Segmented Campaigns:** Split marketing budgets to run distinct ad campaigns—one focusing on volume for retail accounts, and another on bulk orders for corporate emails.
### 🔑 Day 13: Advanced SQL (JOIN, GROUP BY, HAVING)
* **Core Competencies:** Relational Schema Management (DDL), Sequential Key Interlinking (`INNER`/`LEFT JOIN`), Matrix Aggregations (`SUM`/`COUNT`/`AVG`), Condition Group Filtering (`HAVING`), and Query Execution Performance Optimization.
* **Project Deliverable:** Designed and optimized the complete "NorthRetail" commercial relational database workspace, deploying advanced aggregated queries across multiple tracking tables to construct strategic management reports.

#### 💡 Core Business Insights & Analytical Summary:
1. **Product Group Revenue Concentration:** The *Electronics* product division remains our primary driver of financial margins, while utility hardware columns in *Accessories* capture high frequency but low absolute volume.
2. **High-Value Client Concentration:** Strategic accounts such as **Amit Mishra** and **Asha Sharma** generate massive sales volumes over multi-stage checkouts, emphasizing the importance of dedicated high-value customer channels.
3. **Geographic Revenue Densities:** Regional revenue mapping marks **Delhi** and **Pune** as top-tier high-revenue hubs, with **Mumbai** acting as a stable core transactional node.

#### 🚀 Programmatic Strategy Recommendations:
* **Indexed Relational Architecture:** Configure explicit B-Tree database indexes on critical relational constraints (`CustomerID`, `ProductID`) to preserve lightning-fast extraction patterns as rows scale.
* **Aggregated Group Pruning:** Apply targeted structural pruning utilizing `WHERE` parameters early in execution blocks to filter rows before processing resource-heavy `GROUP BY` operations.
* **VIP Marketing Funnels:** Leverage group-filtered tracking lists built via the `HAVING` clause to run automated premium retention campaigns targeting top-tier accounts.
### 🎓 Day 14: SQL Case Study — End-to-End Business Analysis
* **Core Competencies:** Advanced Relational Normalization, Subquery Matrix Layouts, Conditional Branch Structuring (`CASE WHEN`), Financial Ledger Auditing, Leakage Discovery Frameworks, and Collaborative SQL-to-Pandas Visual Output Piping.
* **Project Deliverable:** Structured and executed a full corporate ledger investigation for the "UrbanGrocer" workspace ecosystem, mapping a 15-order tracking log to clear cash shortfalls, inactive client clusters, and category net performance indexes.

#### 💡 Core Business Insights & Analytical Summary:
1. **The Margin Paradox Variant:** The *Produce* vertical sits as our highest absolute volume driver by currency metrics, yet *Bakery* components yield significantly superior profit margins per rupee invested, showcasing an underexploited margin avenue.
2. **Severe Account Financial Shortfall:** Data quality audits identified clear revenue leakages totaling over ₹20,000, caused by an unrecorded transaction ledger (`O-1012`) and a underpaid billing event (`O-1010`).
3. **Geographic Operations Shutdown:** The analysis flags **Bengaluru (Karnataka)** as an inactive market node with zero successful revenue conversions, indicating localized shipping or logistics blocks.

#### 🚀 Programmatic Strategy Recommendations:
* **Relational Integrity Hardening:** Enforce strict foreign key constraints at the database level to prevent orphaned ledger accounts or unverified checkout transactions.
* **Automated Financial Reconciliation:** Configure a permanent data-reconciliation script running a `LEFT JOIN` tracking routine to flag payment shortfalls or unpaid records at the end of each day.
* **Category Optimization Flows:** Adjust layout recommendation systems to highlight high-margin Bakery assets alongside primary high-volume Produce boxes to lift overall blended margin percentages.
### 🧮 Day 15: Statistics for Data Analysis
* **Core Competencies:** Levels of Data Measurement, Measures of Central Tendency (Mean/Median Skew Diagnostics), Dispersion Metrics (Sample Variance vs. Standard Deviation), Interquartile Range (IQR) Boundaries, Pairwise Correlation Matrix Generation, and Multi-Stage Outlier Cross-Validation.
* **Project Deliverable:** Completed the "MetroMart" comprehensive commercial statistical auditing matrix, engineering an autonomous validation script checking 15 complex account vectors for positive skew indicators, linear behavior relationships, and cash distribution spikes.

#### 💡 Core Business Insights & Analytical Summary:
1. **The Average Distortion Metric:** Analytical results verify that the arithmetic mean (₹33,400) is highly sensitive to extreme distribution tails, inflating the corporate average by over 45% compared to the true median profile (₹24,000).
2. **Transactional Behavior Covariance:** The tracking grid showcases a strong positive correlation (+0.85) between customer visit frequency and net expenditure. *Strategic Caveat*: While this proves intense linear association, it does not confirm direct single-variable causality.
3. **Multi-Stage Anomaly Convergence:** Cross-validation filters using both IQR bounds and Z-score parameters achieved a 100% match rate in isolating account `C-15` as a significant operational outlier.

#### 🚀 Programmatic Strategy Recommendations:
* **Asymmetric Dashboard Baselines:** Mandate the use of robust medians and IQRs rather than means inside standard reporting tools when visualizing right-skewed revenue variables.
* **High-Value Client Ringfencing:** Set an explicit ₹31,200 percentile boundary line (90th cut-off) to isolate elite transaction accounts into high-tier account management paths.
* **Retention Asset Strategy:** Direct investment toward accelerating repeat user traffic pipelines (driving visit frequency), as this metric demonstrates the highest covariance with customer value expansion.