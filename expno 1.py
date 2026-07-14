import pandas as pd

# Read CSV
df = pd.read_csv("students.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Department"] = df["Department"].fillna("Unknown")

# Rename columns
df.rename(columns={
    "StudentName": "Name",
    "Department": "Dept"
}, inplace=True)

# Change data types
df["Marks"] = df["Marks"].astype(float)
df["StudentID"] = df["StudentID"].astype(int)

# Save cleaned data
df.to_csv("students_cleaned.csv", index=False)

print(df)
