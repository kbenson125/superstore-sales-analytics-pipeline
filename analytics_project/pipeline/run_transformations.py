import sqlite3

conn = sqlite3.connect("superstore.db")

with open("transformations.sql") as f:
    sql_script = f.read()

conn.executescript(sql_script)

print("Transformations complete")

conn.close()
