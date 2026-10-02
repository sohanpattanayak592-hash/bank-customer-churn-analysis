# Bank Customer Churn Analysis

This is a data analytics project for my portfolio. I used the standard Kaggle Bank Customer Churn dataset to try and understand why customers are leaving the bank.

### The Business Problem
Banks want to retain their customers. It costs more to acquire a new customer than to keep an existing one. By looking at historical data, we can try to find patterns that indicate a customer might close their account (churn).

### Steps Taken
* Downloaded the data and loaded it into pandas.
* Checked for missing values and dropped columns that aren't useful for prediction (like names and IDs).
* Created a few visualizations using matplotlib and seaborn to explore the data. I used maroon and orange colors for the charts.
* Loaded the data into a local SQLite database to practice writing SQL queries.
* Queried the data to find insights.

### Basic Insights
* Older customers seem to churn more often than younger customers.
* Customers in Germany had a noticeably higher churn rate compared to France and Spain.
* There doesn't seem to be a huge difference in the average balance between male and female customers.

### How to Run
Just make sure you have `Churn_Modelling.csv` in the same folder and run the python script. It will print the SQL results to the terminal and show the charts.
