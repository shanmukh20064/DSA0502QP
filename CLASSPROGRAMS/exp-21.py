import pandas as pd
data = {
    "Name":["John","ALICE","DaVid","EMMA"]
}
df = pd.DataFrame(data)
df["Name"] = df["Name"].str.swapcase()
print(df)