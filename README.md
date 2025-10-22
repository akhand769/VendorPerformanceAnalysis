# 📊 Vendor Performance Data Analytics

### 🧭 *An End-to-End Data Analytics Project using Python, SQL, and Power BI*

This project provides a complete data analytics pipeline to process, analyze, and visualize **vendor performance** data from large-scale datasets (2 GB+). It involves building **ETL pipelines**, performing **exploratory data analysis (EDA)**, and developing a **Power BI dashboard** for reporting and decision-making.

---

## 📝 Table of Contents
- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Dataset Description](#-dataset-description)
- [Project Workflow](#-project-workflow)
- [Scripts & Notebooks](#-scripts--notebooks)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Installation & Setup](#-installation--setup)
- [Usage Guide](#-usage-guide)
- [Key Insights](#-key-insights)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 📌 Project Overview
Organizations often collaborate with multiple vendors, making it challenging to track **performance**, **profitability**, and **cost efficiency**. This project automates the process of:
- Ingesting large CSV files into a structured database,
- Generating performance KPIs using SQL + Python,
- Analyzing trends and metrics through EDA, and
- Visualizing insights using Power BI.

This ensures **data-driven decision-making** and **faster reporting cycles**.

---

## 🧭 Problem Statement
Traditional vendor performance tracking is often **manual, time-consuming**, and not scalable for large datasets. The goal of this project is to:
- Automate vendor data ingestion from raw CSVs
- Build a robust summary layer for key KPIs
- Enable analysts to explore data quickly
- Deliver interactive dashboards to business stakeholders

---

## 🧰 Tech Stack
- 🐍 Python — Data processing, ETL pipeline
- 🧮 SQL / SQLite — Data storage and transformation
- 📊 Power BI — Interactive dashboard and reporting
- 📓 Jupyter Notebook — Exploratory Data Analysis
- 📦 Libraries: Pandas, NumPy, Matplotlib, Seaborn, SQLAlchemy, sqlite3, logging

---

## 🏗️ Project Architecture

 - Raw Data (CSV)
 - ↓
 - Python ETL Pipeline (ingestion_db.py)
 - ↓
 - SQLite Database (inventory.db)
 - ↓
 - SQL Transformations + KPI Calculation (get_vendor_summary.py)
 - ↓
 - Exploratory Data Analysis (Jupyter Notebook)
 - ↓
 - Power BI Dashboard


---

## 🧾 Dataset Description
The dataset contains detailed vendor-level transactional information including:
- Vendor Details (name, number, brand, description)
- Purchases (price, quantity, dollars)
- Sales (sales amount, price, quantity, tax)
- Freight (logistics cost)

💾 Size: 2 GB+ (multiple CSV files)

---

## 🔄 Project Workflow
1. **Data Ingestion**
   - Load raw CSV files in chunks to handle large volumes efficiently.
   - Store them in a SQLite database (`inventory.db`).

2. **Data Transformation**
   - Use SQL queries with CTEs to merge and summarize freight, sales, and purchase data.
   - Compute derived KPIs like:
     - `grossprofit`
     - `profitmargin`
     - `stockturnover`
     - `sales/purchase_ratio`.

3. **Exploratory Data Analysis**
   - Analyze vendor performance metrics.
   - Identify top & bottom performing vendors.
   - Visualize distributions and trends.

4. **Dashboarding**
   - Build Power BI dashboard to visualize KPIs and trends for business users.

---

## 🧠 Scripts & Notebooks

| File Name                            | Description                                                                                           |
|---------------------------------------|-------------------------------------------------------------------------------------------------------|
| `ingestion_db.py`                    | Ingests raw CSV files into SQLite DB using chunking for large datasets. Logs process and execution time. |
| `get_vendor_summary.py`              | Generates vendor performance summary using SQL queries and KPI calculations. Saves clean data to DB.    |
| `Vendor Performance Analysis.ipynb`  | Performs EDA, visualizes KPIs, and prepares data insights for Power BI dashboard.                        |

---

## 📊 Power BI Dashboard
The Power BI dashboard presents:
- 📈 Vendor Sales & Purchase Trends
- 💰 Gross Profit and Margin Analysis
- 🏆 Top & Bottom Performing Vendors
- 📆 Temporal trends for strategic planning

<img width="1042" height="596" alt="image" src="https://github.com/user-attachments/assets/a982c69e-ff58-47a3-a70e-73e5090bccdc" />


---

## ⚙️ Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/akhand769/vendor-performance-analytics.git
cd vendor-performance-analytics
```
## 🧭 Usage Guide

- 🏗️ For Analysts — Explore KPIs and trends through Jupyter Notebook.

- 📈 For Business Users — Interact with Power BI dashboard for decision-making.

- ⚡ For Developers — Modify ETL and SQL logic for different datasets or scaling.

## 🧠 Key Insights

 - Automated ingestion of 2 GB+ of vendor data with no manual intervention.

 - KPIs reveal top revenue-generating vendors and high-margin products.

 - Power BI dashboard enables near real-time business monitoring.

## 🛣️ Future Enhancements

 - ⏳ Schedule ETL jobs for automated refresh

 - ☁️ Migrate to cloud data warehouse (e.g., BigQuery, Snowflake)

 - 🧠 Integrate anomaly detection on vendor performance

 - 🔄 Automate Power BI refresh with APIs

## 👤 Author

Akhand Chaurasia
