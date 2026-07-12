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