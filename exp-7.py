import pandas as pd
df = pd.read_csv("sales.csv")
pivot = pd.pivot_table(df,
                       values="Sale",
                       index="Item",
                       aggfunc=["max","min"])
print(pivot)