import pandas as pd

df = pd.read_csv("students.csv")

print("Highest:", df["Marks"].max())
print("Lowest:", df["Marks"].min())
print("Average:", df["Marks"].mean())
print("Median:", df["Marks"].median())
print("Standard Deviation:", df["Marks"].std())

# Grade Assignment
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(grade)

top_students = df[df["Marks"] == df["Marks"].max()]

print(df)
print(top_students)
