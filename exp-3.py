import pandas as pd

df = pd.read_csv("jobs.csv")

result = df.sort_values(by="job_title", ascending=False)

print(result)