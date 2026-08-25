import pandas as pd
data = {
    "Name":["John","Alice","David"],
    "Age":[20,21,22]
}
df = pd.DataFrame(data,
                  index=["A","B","C"])
print(df)