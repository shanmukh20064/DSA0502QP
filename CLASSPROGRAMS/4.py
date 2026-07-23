import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    department TEXT
)
""")
conn.commit()
print("Table created successfully!")

print("\nTables in the database:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    print(table[0])

cursor.execute("INSERT INTO students(name, age, department) VALUES('Shanmukh',20,'CSE')")
cursor.execute("INSERT INTO students(name, age, department) VALUES('Rahul',21,'ECE')")
cursor.execute("INSERT INTO students(name, age, department) VALUES('Priya',19,'IT')")
conn.commit()
print("\nRecords inserted successfully!")

print("\nStudent Records:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("""
UPDATE students
SET department='AI & DS'
WHERE name='Rahul'
""")
conn.commit()
print("\nRecord updated successfully!")

print("\nRecords After Update:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nSearch Result (Department = AI & DS):")
cursor.execute("SELECT * FROM students WHERE department='AI & DS'")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("DELETE FROM students WHERE name='Priya'")
conn.commit()
print("\nRecord deleted successfully!")

print("\nFinal Records:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
print("\nDatabase closed successfully!")