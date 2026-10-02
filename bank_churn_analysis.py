import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# load the data
# using standard kaggle dataset name
df = pd.read_csv('Churn_Modelling.csv')

# taking a quick look at the data
print("--- DATA HEAD ---")
print(df.head())
print("\n--- MISSING DATA ---")
print(df.isnull().sum())

# dropping row number, customer id, and surname since they don't matter for analysis
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

# setting up icici bank brand colors (maroon and orange)
icici_maroon = '#800000'
icici_orange = '#F37021' 
sns.set_palette([icici_maroon, icici_orange])

# let's look at how many people churned vs stayed
plt.figure(figsize=(6, 4))
sns.countplot(x='Exited', data=df)
plt.title('Customer Churn Count')
plt.xlabel('Exited (1 = Yes, 0 = No)')
plt.ylabel('Count')
plt.savefig('churn_count.png')
plt.close()

# checking age distribution for churners and non-churners
plt.figure(figsize=(8, 5))
sns.boxplot(x='Exited', y='Age', data=df)
plt.title('Age vs Churn')
plt.savefig('age_vs_churn.png')
plt.close()

# looking at balance for different geographies
plt.figure(figsize=(8, 5))
sns.barplot(x='Geography', y='Balance', hue='Exited', data=df)
plt.title('Average Balance by Country and Churn Status')
plt.savefig('balance_by_country.png')
plt.close()


# ---- SQL PART ----

# setting up sqlite database
conn = sqlite3.connect('bank_churn.db')
df.to_sql('customers', conn, if_exists='replace', index=False)

# query 1: count of churned customers by country
query1 = """
SELECT Geography, COUNT(*) as CustomerCount
FROM customers
WHERE Exited = 1
GROUP BY Geography
ORDER BY CustomerCount DESC;
"""
churn_by_country = pd.read_sql(query1, conn)
print("\nChurn by Country:\n", churn_by_country)

# query 2: average balance and salary by gender
query2 = """
SELECT Gender, AVG(Balance) as AvgBalance, AVG(EstimatedSalary) as AvgSalary
FROM customers
GROUP BY Gender;
"""
avg_financials = pd.read_sql(query2, conn)
print("\nAverage Financials by Gender:\n", avg_financials)

# query 3: churn count by age group (using simple case when)
query3 = """
SELECT 
    CASE 
        WHEN Age < 30 THEN 'Under 30'
        WHEN Age BETWEEN 30 AND 50 THEN '30-50'
        ELSE 'Over 50'
    END as AgeGroup,
    SUM(Exited) as TotalChurned
FROM customers
GROUP BY AgeGroup
ORDER BY TotalChurned DESC;
"""
churn_by_age = pd.read_sql(query3, conn)
print("\nChurn by Age Group:\n", churn_by_age)

conn.close()
