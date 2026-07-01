# E-commerce-Return-Rate-Reduction-Analysis



# E-Commerce Return Rate Reduction Analysis

## Project Overview

This project analyzes customer product returns in an e-commerce business to identify factors influencing returns and provide actionable business insights.

The analysis focuses on:

* Return Rate by Product Category
* Return Rate by Geography (State)
* Return Rate by Marketing Channel
* Customer Return Behavior
* Return Reasons Analysis

The project uses **Python, MySQL, and Power BI** to perform data cleaning, analysis, and visualization.

---

## Objective

The main objective of this project is to:

* Understand why customers return products.
* Identify high-return categories.
* Analyze geographical return patterns.
* Evaluate marketing channels contributing to returns.
* Support business decisions to reduce return rates.

---

## Tools & Technologies

* Python

  * Pandas
  * NumPy
  * Matplotlib
* MySQL
* Power BI
* Google Colab

---

## Dataset Information

The dataset contains customer purchase and return information with the following columns:

| Column Name       | Description                |
| ----------------- | -------------------------- |
| customer_id       | Unique customer identifier |
| customer_name     | Customer name              |
| age               | Customer age               |
| gender            | Customer gender            |
| city              | Customer city              |
| state             | Customer state             |
| country           | Customer country           |
| category          | Product category           |
| marketing_channel | Source channel             |
| product_price     | Product price              |
| returned          | Return status (Yes/No)     |
| return_reason     | Reason for return          |

Total Records: **4000+**

---

## Data Cleaning Process

The following data cleaning steps were performed using Python:

### Missing Value Treatment

* Age filled using median value
* Missing marketing channels replaced with "Unknown"
* Missing return status replaced with "No"
* Missing return reasons replaced with "Not Specified"

### Duplicate Removal

Duplicate records were identified and removed.

### Feature Engineering

Created a new column:

```text
return_flag
```

Where:

```text
Yes = 1
No = 0
```

---

## Exploratory Data Analysis (EDA)

The following analyses were performed:

### Overall Return Rate

Calculated the percentage of returned products.

### Return Rate by Category

Identified product categories with the highest return rates.

### Return Rate by State

Analyzed geographical return trends.

### Return Rate by Marketing Channel

Evaluated the effectiveness of marketing channels and their return behavior.

### Product Price Analysis

Detected outliers using IQR and boxplot visualization.

---

## SQL Analysis

Business queries were executed using MySQL.

### Key Queries

* Total Customers
* Total Returns
* Overall Return Rate
* Return Rate by Category
* Return Rate by Marketing Channel
* Return Rate by State
* Top Return Reasons
* Gender-wise Return Analysis
* Age Group Analysis

---

## Power BI Dashboard

An interactive dashboard was created containing:

### KPI Cards

* Total Customers
* Total Returns
* Return Rate (%)
* Average Product Price

### Visualizations

* Return Rate by Category
* Return Rate by State
* Return Rate by Marketing Channel
* Top Return Reasons
* Product Price Distribution

### Filters

* Category
* State
* Gender
* Marketing Channel

---

## Business Insights

The analysis helps businesses:

* Identify categories with high return rates.
* Understand common return reasons.
* Optimize marketing campaigns.
* Improve customer satisfaction.
* Reduce operational costs associated with product returns.

---

## Project Workflow

```text
Raw Dataset
     ↓
Python Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
MySQL Business Queries
     ↓
Power BI Dashboard
     ↓
Business Insights & Recommendations
```

---

## Future Enhancements

* Logistic Regression for Return Prediction
* Customer Segmentation
* Product Risk Scoring
* Advanced Power BI Dashboard
* Machine Learning-based Return Forecasting

---

## Author

**Lingamsetty Siva**

Data Analyst Project using Python, MySQL, and Power BI.
