import pandas as pd
df = pd.read_csv("school.csv")
result = df.groupby("School_Code")["Age"].agg(["mean","min","max"])
print(result)