import sqlite3

# Connect to Database
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Create Student Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student(
Student_ID INTEGER PRIMARY KEY,
Name TEXT,
Gender TEXT,
Age INTEGER,
Email TEXT,
Phone TEXT,
Department_ID INTEGER
)
""")

conn.commit()

# CREATE (Insert)
cursor.execute("""
INSERT INTO Student
VALUES(101,'Shanmukh','Male',20,
'shanmukh@gmail.com',
'9876543210',1)
""")

conn.commit()

# READ
print("Student Records")

cursor.execute("SELECT * FROM Student")

rows = cursor.fetchall()

for row in rows:
    print(row)

# UPDATE
cursor.execute("""
UPDATE Student
SET Age=21
WHERE Student_ID=101
""")

conn.commit()

print("\nAfter Update")

cursor.execute("SELECT * FROM Student")

for row in cursor.fetchall():
    print(row)

# DELETE
cursor.execute("""
DELETE FROM Student
WHERE Student_ID=101
""")

conn.commit()

print("\nAfter Delete")

cursor.execute("SELECT * FROM Student")

rows = cursor.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No Records Found")

conn.close()