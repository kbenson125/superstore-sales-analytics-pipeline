import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv("superstore_raw.csv", encoding="latin1", skiprows=1)
print("Columns found in file:", df.columns.tolist())

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("-", "_")

# Convert date columns
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)
df['ship_date'] = pd.to_datetime(df['ship_date'],dayfirst=True)

# Connect to database
conn = sqlite3.connect("superstore.db")

# Load raw data table
df.to_sql("raw_orders", conn, if_exists="replace", index=False)

print("Raw data loaded successfully")

conn.close()


