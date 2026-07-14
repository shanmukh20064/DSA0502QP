import pandas as pd
import re

df = pd.read_csv("students.csv")

# Missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Email validation
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_email = df[
    ~df["Email"].astype(str).str.match(email_pattern)
]

print(invalid_email)

# Phone validation
invalid_phone = df[
    ~df["Phone"].astype(str).str.match(r'^\d{10}$')
]

print(invalid_phone)

# Negative marks
negative_marks = df[df["Marks"] < 0]

print(negative_marks)

# Remove negative marks
df = df[df["Marks"] >= 0]

df.to_csv("validated_students.csv", index=False)
