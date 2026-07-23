import pandas as pd
df = pd.read_csv("school.csv")
group = df.groupby(["School_Code","Class"])
for name,data in group:
    print("\nGroup:",name)
    print(data)