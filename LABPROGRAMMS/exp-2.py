import pandas as pd
df = pd.read_csv("jobhistory.csv")
result = df.groupby("employee_id").size()
print("Employees with two or more jobs:")
print(result[result >= 2])