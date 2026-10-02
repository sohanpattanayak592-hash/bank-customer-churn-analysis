Bank Customer Churn Analysis: Predicting Customer Exit

This repository contains a portfolio data analytics project aimed at understanding why customers leave their bank. I used the standard Kaggle Bank Customer Churn dataset to uncover patterns in customer attrition and translated those findings into an interactive business intelligence dashboard.

The Business Problem

Customer retention is a core metric for any financial institution. Since acquiring a new customer is significantly more expensive than retaining an existing one, identifying the behavioral or demographic patterns that precede a closed account (churn) is highly valuable. This project explores historical banking data to pinpoint those exact patterns.

Phase 1: Data Cleaning & Python EDA

Data Preparation: I loaded the Churn_Modelling.csv dataset into Pandas, checked for missing values, and removed non-predictive columns like RowNumber, CustomerId, and Surname.   
PY

Exploratory Data Analysis (EDA): I used Matplotlib and Seaborn to visualize customer churn counts, age distributions, and average balances. To align the visuals with a specific corporate profile, I customized the charts using (Maroon #800000 and Orange #F37021).   
PY
+ 1

SQL Integration: I loaded the cleaned Pandas DataFrame into a local SQLite database (bank_churn.db) using the sqlite3 library. This allowed me to write standard SQL queries (utilizing GROUP BY and CASE WHEN statements) to extract targeted insights on churn by country, average financials by gender, and churn by age group.   
PY
+ 1

Phase 2: Power BI Dashboard
To make these insights accessible to non-technical stakeholders, I built an interactive dashboard. You can view the final file in this repository under the name Bank_churn_analysis.pbix.

Data Modeling: I imported the cleaned data and ensured the Exited, HasCrCard, and IsActiveMember columns were treated as text rather than numerical values to prevent unwanted mathematical aggregations.   
MD

DAX Measures: I wrote custom DAX formulas to generate top-level metrics, including Total Customers (using COUNTROWS), Total Churned (using a CALCULATE function filtered to "CHURNED"), and a percentage Churn Rate (using the DIVIDE function).   
MD

Visualizations:

KPI Cards: Displaying Total Customers, Total Churned, and the overall Churn Rate at a glance.   
MD

Donut Chart: Showing the binary proportion of retained versus churned customers.   
MD

Clustered Bar Chart: Breaking down total churn by customer age.   
MD

Map Visual: Highlighting churn hotspots by geography.   
MD

Interactivity: I added dropdown slicers for Geography and IsActiveMember so users can filter the entire dashboard dynamically to investigate specific segments.   
MD

Formatting: The dashboard features a clean white background and is styled exclusively with ICICI Bank's exact hex codes (Maroon #8A1538 and Orange #F15A22) for a professional finish.   
MD

Key Insights Discovered
Age Factor: Older customers demonstrate a noticeably higher churn rate compared to younger demographics.

Regional Variance: Customers located in Germany churn at a significantly higher rate than those in France and Spain.

Gender & Balance: There is no substantial difference in the average account balance between male and female customers.

How to Run the Project
Ensure Churn_Modelling.csv and bank_churn_analysis.py are in the same directory.

Run the Python script to generate the EDA charts and execute the SQLite queries (results will print directly to your terminal).

Open Bank_churn_analysis.pbix in Power BI Desktop to interact with the final dashboard.
