import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("superstore.db")

# Export cleaned orders table
clean_orders = pd.read_sql_query("SELECT * FROM clean_orders", conn)
clean_orders.to_csv("clean_orders.csv", index=False)

# Export summary table
sales_summary = pd.read_sql_query("SELECT * FROM sales_summary", conn)
sales_summary.to_csv("sales_summary.csv", index=False)

# Export monthly sales table
monthly_sales = pd.read_sql_query("SELECT * FROM monthly_sales", conn)
monthly_sales.to_csv("monthly_sales.csv", index=False)

print("Data exported for Tableau")

conn.close()
