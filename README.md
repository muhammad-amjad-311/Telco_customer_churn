# Telco Customer Churn Analysis & Dashboard

An end-to-end data analysis project that cleans a telecom customer dataset with Python (pandas) and visualizes customer churn patterns in an interactive Power BI dashboard.

## 📌 Project Overview

Customer churn — when a customer stops using a company's service — is one of the most costly problems for subscription-based businesses. This project analyzes the **Telco Customer Churn dataset** (7,043 customers, 21 attributes) to identify which factors most strongly predict churn, and presents the findings through a Power BI dashboard.

## 🗂️ Dataset

- **Source:** [Telco Customer Churn (IBM Sample Dataset)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Rows:** 7,043 customers
- **Columns:** 21 (demographics, account info, subscribed services, billing, and churn status)

## 🧹 Data Cleaning (Python / pandas)

Key cleaning steps performed in `clean.py`:

| Issue | Fix |
|---|---|
| `TotalCharges` stored as text (`object`) instead of numeric | Converted using `pd.to_numeric()` with `errors='coerce'` |
| 11 rows had blank/whitespace `TotalCharges` (new customers with `tenure = 0`) | Filled with `0` since no billing history existed yet |
| Data types validated for all 21 columns | Confirmed via `df.info()` and `df.describe()` |

```python
import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

# Fix TotalCharges: convert blank strings to NaN, then to float
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(0)

df.to_csv("Telco-Customer-Churn-Cleaned.csv", index=False)
```

## 📊 Power BI Dashboard

The dashboard visualizes churn rate (%) across key customer segments, rather than raw counts, using a custom DAX measure:

```DAX
Churn Rate % = 
DIVIDE(
    CALCULATE(COUNTROWS('Telco-Customer-Churn-Cleaned'), 'Telco-Customer-Churn-Cleaned'[Churn] = "Yes"),
    COUNTROWS('Telco-Customer-Churn-Cleaned')
)
```

### Dashboard includes:
- **KPI Cards** — Total Customers, Overall Churn Rate
- **Churn Rate by Contract Type**
- **Churn Rate by Tenure (binned)**
- **Churn Rate by Internet Service Type**
- **Churn Rate by Payment Method**
- **Churn Rate by Monthly Charges (binned)**
- **Slicers** for interactive filtering (Payment Method, Tenure, Monthly Charges)

## 🔍 Key Insights

| Factor | Highest-Risk Segment | Churn Rate |
|---|---|---|
| **Tenure** | 0–20 months (new customers) | ~48% |
| **Contract Type** | Month-to-month | ~42% |
| **Internet Service** | Fiber optic | ~42% |
| **Payment Method** | Electronic check | ~45% |
| **Gender** | No significant difference | ~26–27% |

**Overall churn rate:** 27% across 7,043 customers.

### Summary
Customers most likely to churn are **new (low tenure)**, on a **month-to-month contract**, using **Fiber optic internet**, and paying via **electronic check**. Gender has no meaningful impact on churn. These findings suggest retention efforts should focus on incentivizing longer contracts and automatic payment methods, particularly for newly onboarded customers.

## 🛠️ Tools Used

- **Python** (pandas) — data cleaning
- **Power BI Desktop** — data visualization and dashboarding
- **DAX** — custom measures for churn rate calculation

## 📁 Repository Structure

```
├── Telco-Customer-Churn.csv           # Raw dataset
├── clean.py                           # Data cleaning script
├── Telco-Customer-Churn-Cleaned.csv   # Cleaned dataset
├── Telco_Churn_Dashboard.pbix         # Power BI dashboard file
└── README.md
```

## 🚀 How to Use

1. Clone this repository
2. Run `clean.py` to generate the cleaned dataset (or use the pre-cleaned CSV included)
3. Open `Telco_Churn_Dashboard.pbix` in Power BI Desktop to explore the interactive dashboard
