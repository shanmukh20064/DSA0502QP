import pandas as pd
data = {
    "Name":["John","Alice","David"],
    "Age":[20,21,22],
    "Marks":[85,90,88]
}
df = pd.DataFrame(data)
print(df)