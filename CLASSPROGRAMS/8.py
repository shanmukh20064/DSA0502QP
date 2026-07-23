import sqlite3

# Connect Database
conn = sqlite3.connect("payroll.db")
cursor = conn.cursor()

# Create Employee Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee(
    Employee_ID INTEGER PRIMARY KEY,
    Employee_Name TEXT,
    Department TEXT,
    Designation TEXT,
    Salary REAL
)
""")

conn.commit()

print("Employee Table Created Successfully!")

# Show Tables
print("\nTables in Database:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

for table in cursor.fetchall():
    print(table[0])

# INSERT Records
cursor.execute("""
INSERT INTO Employee
VALUES(101,'Rahul','Production','Manager',50000)
""")

cursor.execute("""
INSERT INTO Employee
VALUES(102,'Priya','HR','HR Executive',40000)
""")

cursor.execute("""
INSERT INTO Employee
VALUES(103,'Arun','Finance','Accountant',45000)
""")

conn.commit()

print("\nRecords Inserted Successfully!")

# READ Records
print("\nEmployee Records")

cursor.execute("SELECT * FROM Employee")

for row in cursor.fetchall():
    print(row)

# UPDATE Record
cursor.execute("""
UPDATE Employee
SET Salary=55000
WHERE Employee_ID=101
""")

conn.commit()

print("\nRecord Updated Successfully!")

print("\nAfter Update")

cursor.execute("SELECT * FROM Employee")

for row in cursor.fetchall():
    print(row)

# SEARCH Record
print("\nSearch Result")

cursor.execute("""
SELECT * FROM Employee
WHERE Department='HR'
""")

for row in cursor.fetchall():
    print(row)

# DELETE Record
cursor.execute("""
DELETE FROM Employee
WHERE Employee_ID=103
""")

conn.commit()

print("\nRecord Deleted Successfully!")

print("\nFinal Records")

cursor.execute("SELECT * FROM Employee")

for row in cursor.fetchall():
    print(row)

# Close Database
conn.close()

print("\nDatabase Closed Successfully!")