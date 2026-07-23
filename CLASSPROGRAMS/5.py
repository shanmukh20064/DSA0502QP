import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO students(name, age, department)
VALUES('Shanmukh', 20, 'CSE')
""")

conn.commit()
conn.close()