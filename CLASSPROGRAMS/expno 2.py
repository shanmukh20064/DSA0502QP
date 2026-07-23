import pandas as pd

students = pd.read_csv("students.csv")
departments = pd.read_csv("departments.csv")
marks = pd.read_csv("marks.csv")

# Merge Student and Department
df = pd.merge(students, departments, on="DepartmentID")

# Merge with Marks
df = pd.merge(df, marks, on="StudentID")

print(df)

df.to_csv("student_report.csv", index=False)
