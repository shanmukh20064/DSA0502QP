import pandas as pd
df = pd.read_csv("school.csv")
group = df.groupby("School_Code")
print(group)
print("\nType of GroupBy Object:")
print(type(group))