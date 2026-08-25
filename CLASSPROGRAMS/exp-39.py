import pandas as pd
data = {
    "Name":["John","Alice","David","Emma","James"],
    "Age":[20,21,22,23,24],
    "Marks":[85,90,88,91,87]
}
df = pd.DataFrame(data)
print(df.head(3))