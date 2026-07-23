import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="ecommerce_db",
        port=3306
    )

    if conn.is_connected():
        print("Connected to MySQL Successfully")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customer(
        CustomerID INT PRIMARY KEY,
        CustomerName VARCHAR(50),
        Email VARCHAR(50),
        Phone VARCHAR(15)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Product(
        ProductID INT PRIMARY KEY,
        ProductName VARCHAR(50),
        Category VARCHAR(50),
        Price DECIMAL(10,2),
        Stock INT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders(
        OrderID INT PRIMARY KEY,
        CustomerID INT,
        OrderDate DATE,
        TotalAmount DECIMAL(10,2),
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Payment(
        PaymentID INT PRIMARY KEY,
        OrderID INT,
        PaymentMethod VARCHAR(30),
        PaymentStatus VARCHAR(20),
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Review(
        ReviewID INT PRIMARY KEY,
        CustomerID INT,
        ProductID INT,
        Rating INT,
        ReviewText VARCHAR(100),
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
        FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
    )
    """)

    cursor.execute("DELETE FROM Review")
    cursor.execute("DELETE FROM Payment")
    cursor.execute("DELETE FROM Orders")
    cursor.execute("DELETE FROM Product")
    cursor.execute("DELETE FROM Customer")

    cursor.execute("INSERT INTO Customer VALUES (101,'Rahul','rahul@gmail.com','9876543210')")
    cursor.execute("INSERT INTO Customer VALUES (102,'Priya','priya@gmail.com','9876543211')")

    cursor.execute("INSERT INTO Product VALUES (201,'Laptop','Electronics',55000,10)")
    cursor.execute("INSERT INTO Product VALUES (202,'Book','Books',500,25)")

    cursor.execute("INSERT INTO Orders VALUES (301,101,'2026-07-14',55000)")
    cursor.execute("INSERT INTO Orders VALUES (302,102,'2026-07-15',500)")

    cursor.execute("INSERT INTO Payment VALUES (401,301,'UPI','Paid')")
    cursor.execute("INSERT INTO Payment VALUES (402,302,'Card','Pending')")

    cursor.execute("INSERT INTO Review VALUES (501,101,201,5,'Excellent')")
    cursor.execute("INSERT INTO Review VALUES (502,102,202,4,'Good Book')")

    cursor.execute("UPDATE Product SET Stock=Stock-1 WHERE ProductID=201")
    cursor.execute("UPDATE Product SET Stock=Stock-1 WHERE ProductID=202")

    conn.commit()

    print("\nCustomer Records")
    cursor.execute("SELECT * FROM Customer")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("""
    UPDATE Customer
    SET Phone='9999999999'
    WHERE CustomerID=101
    """)
    conn.commit()

    print("\nAfter Update")
    cursor.execute("SELECT * FROM Customer")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("DELETE FROM Customer WHERE CustomerID=102")
    conn.commit()

    print("\nAfter Delete")
    cursor.execute("SELECT * FROM Customer")
    for row in cursor.fetchall():
        print(row)

except Error as e:
    print("Error:", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("\nMySQL Connection Closed")