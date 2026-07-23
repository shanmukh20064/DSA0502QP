import sqlite3
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
    Book_ID INTEGER PRIMARY KEY,
    Book_Name TEXT,
    Author TEXT,
    Publisher TEXT,
    Price REAL
)
""")
conn.commit()
print("Books Table Created Successfully")
print("\nTables in Database")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for table in cursor.fetchall():
    print(table[0])
cursor.execute("""
INSERT INTO Books
VALUES(101,'Python Programming','Guido','Pearson',550)
""")
cursor.execute("""
INSERT INTO Books
VALUES(102,'Database Systems','Navathe','McGraw Hill',700)
""")
cursor.execute("""
INSERT INTO Books
VALUES(103,'Operating Systems','Galvin','Wiley',650)
""")
conn.commit()
print("\nRecords Inserted Successfully")
print("\nBook Records")
cursor.execute("SELECT * FROM Books")
for row in cursor.fetchall():
    print(row)
cursor.execute("""
UPDATE Books
SET Price=600
WHERE Book_ID=101
""")
conn.commit()
print("\nRecord Updated Successfully")
print("\nAfter Update")
cursor.execute("SELECT * FROM Books")
for row in cursor.fetchall():
    print(row)
print("\nSearch Result")
cursor.execute("""
SELECT * FROM Books
WHERE Author='Guido'
""")
for row in cursor.fetchall():
    print(row)
cursor.execute("""
DELETE FROM Books
WHERE Book_ID=103
""")
conn.commit()
print("\nRecord Deleted Successfully")
print("\nFinal Records")
cursor.execute("SELECT * FROM Books")
for row in cursor.fetchall():
    print(row)
conn.close()
print("\nDatabase Closed Successfully")
