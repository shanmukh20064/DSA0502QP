import pandas as pd
data = {
    "name":["John","Alice","David","Emma"],
    "score":[85,90,88,95],
    "attempts":[1,2,1,3],
    "qualify":["Yes","Yes","Yes","No"]
}
df = pd.DataFrame(data)
print(df[["name","score"]])