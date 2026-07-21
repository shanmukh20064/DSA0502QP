import pandas as pd

df = pd.read_csv("employe.csv")

print("Distinct Department IDs:")
print(df["department_id"].drop_duplicates())