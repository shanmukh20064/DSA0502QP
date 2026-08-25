import pandas as pd
data = {
    "Name":["Apple","Banana","Mango","Orange"]
}
df = pd.DataFrame(data)
print(df["Name"].str.find("an"))