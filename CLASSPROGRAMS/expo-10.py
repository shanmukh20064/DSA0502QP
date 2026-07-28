import pandas as pd

# Read CSV file
df = pd.read_csv("attendance.csv")

# Calculate Attendance Percentage
df["AttendancePercentage"] = (df["ClassesAttended"] / df["TotalClasses"]) * 100

print("Attendance Percentage:")
print(df)

# Students below 75%
shortage = df[df["AttendancePercentage"] < 75]

print("\nStudents Below 75% Attendance:")
print(shortage)

# Generate Shortage List
shortage.to_csv("shortage_list.csv", index=False)

print("\nShortage list saved as shortage_list.csv")