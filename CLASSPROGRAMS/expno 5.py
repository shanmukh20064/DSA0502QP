import sqlite3
import pandas as pd

conn = sqlite3.connect("student.db")

df = pd.read_sql_query("SELECT * FROM Student", conn)

print(df)

filtered = pd.read_sql_query(
    "SELECT * FROM Student WHERE Marks > 80",
    conn
)

print(filtered)

filtered.to_csv("high_marks.csv", index=False)

conn.close()
