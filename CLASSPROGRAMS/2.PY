import pandas as pd
data = {
    "Department_ID":[10,20,30,10,40,20,50]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
print("\nDistinct Department IDs:")
print(df["Department_ID"].drop_duplicates())