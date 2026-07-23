import csv
import json
import xml.etree.ElementTree as ET
# -------------------- Read students.csv --------------------
students = []
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
# -------------------- Read marks.csv --------------------
marks = []
with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        marks.append(row)
# -------------------- Read results.json --------------------
with open("results.json", "r") as file:
    json_data = json.load(file)
# -------------------- Read results.xml --------------------
tree = ET.parse("results.xml")
root = tree.getroot()
print("\nStudent Results")
print("-" * 60)
passed = 0
failed = 0
department = {}
for student in students:
    sid = student["StudentID"]
    name = student["StudentName"]
    dept = student["Department"]
    # Find student's marks
    for mark in marks:
        if mark["StudentID"] == sid:
            m = int(mark["Marks"])
            # Grade Calculation
            if m >= 90:
                grade = "A+"
                result = "Pass"
            elif m >= 80:
                grade = "A"
                result = "Pass"
            elif m >= 70:
                grade = "B"
                result = "Pass"
            elif m >= 60:
                grade = "C"
                result = "Pass"
            elif m >= 50:
                grade = "D"
                result = "Pass"
            else:
                grade = "F"
                result = "Fail"
            print(f"{sid}\t{name}\t{dept}\t{m}\t{grade}\t{result}")
            # Count pass/fail
            if result == "Pass":
                passed += 1
            else:
                failed += 1
            # Department-wise pass count
            if dept not in department:
                department[dept] = {"pass": 0, "total": 0}
            department[dept]["total"] += 1
            if result == "Pass":
                department[dept]["pass"] += 1
            break
# -------------------- Failed Students --------------------
print("\nFailed Students")
for student in students:
    sid = student["StudentID"]
    for mark in marks:
        if mark["StudentID"] == sid and int(mark["Marks"]) < 50:
            print(student["StudentName"])
# -------------------- Department-wise Pass Percentage --------------------
print("\nDepartment-wise Pass Percentage")
for dept in department:
    p = (department[dept]["pass"] / department[dept]["total"]) * 100
    print(dept, ":", round(p, 2), "%")
# -------------------- Export Cleaned Dataset --------------------
with open("student_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["StudentID", "StudentName", "Department", "Marks"])
    for student in students:
        sid = student["StudentID"]
        for mark in marks:
            if mark["StudentID"] == sid:
                writer.writerow([
                    sid,
                    student["StudentName"],
                    student["Department"],
                    mark["Marks"]
                ])
                break
print("\nCleaned dataset exported successfully as student_report.csv")