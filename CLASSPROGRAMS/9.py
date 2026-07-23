import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="hospital_db",
        port=3306
    )

    if conn.is_connected():
        print("Connected to MySQL Successfully")

    cursor = conn.cursor()

    # Create Patient Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patient(
        PatientID INT PRIMARY KEY,
        PatientName VARCHAR(50),
        Age INT,
        Gender VARCHAR(10),
        Disease VARCHAR(50)
    )
    """)

    # Create Doctor Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Doctor(
        DoctorID INT PRIMARY KEY,
        DoctorName VARCHAR(50),
        Specialization VARCHAR(50)
    )
    """)

    # Create Appointment Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Appointment(
        AppointmentID INT PRIMARY KEY,
        PatientID INT,
        DoctorID INT,
        AppointmentDate DATE,
        FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
        FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID)
    )
    """)

    # Create Treatment Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Treatment(
        TreatmentID INT PRIMARY KEY,
        PatientID INT,
        Prescription VARCHAR(100),
        LabTest VARCHAR(100),
        FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
    )
    """)

    # Create Payment Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Payment(
        PaymentID INT PRIMARY KEY,
        PatientID INT,
        Amount DECIMAL(10,2),
        PaymentStatus VARCHAR(20),
        FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
    )
    """)

    # Clear old records (prevents duplicate key errors)
    cursor.execute("DELETE FROM Payment")
    cursor.execute("DELETE FROM Treatment")
    cursor.execute("DELETE FROM Appointment")
    cursor.execute("DELETE FROM Doctor")
    cursor.execute("DELETE FROM Patient")

    # Insert Patient
    cursor.execute("INSERT INTO Patient VALUES (101,'Ramesh',45,'Male','Fever')")
    cursor.execute("INSERT INTO Patient VALUES (102,'Priya',30,'Female','Diabetes')")

    # Insert Doctor
    cursor.execute("INSERT INTO Doctor VALUES (201,'Dr.Kumar','General')")
    cursor.execute("INSERT INTO Doctor VALUES (202,'Dr.Anita','Diabetologist')")

    # Insert Appointment
    cursor.execute("INSERT INTO Appointment VALUES (1,101,201,'2026-07-14')")
    cursor.execute("INSERT INTO Appointment VALUES (2,102,202,'2026-07-15')")

    # Insert Treatment
    cursor.execute("INSERT INTO Treatment VALUES (1,101,'Paracetamol','Blood Test')")
    cursor.execute("INSERT INTO Treatment VALUES (2,102,'Insulin','Sugar Test')")

    # Insert Payment
    cursor.execute("INSERT INTO Payment VALUES (1,101,500.00,'Paid')")
    cursor.execute("INSERT INTO Payment VALUES (2,102,1200.00,'Pending')")

    conn.commit()

    print("\nPatient Records")
    cursor.execute("SELECT * FROM Patient")

    for row in cursor.fetchall():
        print(row)

    # Update
    cursor.execute("""
    UPDATE Patient
    SET Disease='Viral Fever'
    WHERE PatientID=101
    """)

    conn.commit()

    print("\nAfter Update")
    cursor.execute("SELECT * FROM Patient")

    for row in cursor.fetchall():
        print(row)

    # Delete
    cursor.execute("DELETE FROM Patient WHERE PatientID=102")
    conn.commit()

    print("\nAfter Delete")
    cursor.execute("SELECT * FROM Patient")

    for row in cursor.fetchall():
        print(row)

except Error as e:
    print("Error:", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("\nMySQL Connection Closed")