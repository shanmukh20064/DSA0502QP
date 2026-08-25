import pandas as pd
import numpy as np
data = {
    "A":[1,2,np.nan,4],
    "B":[5,np.nan,7,8],
    "C":[9,10,11,np.nan]
}
df = pd.DataFrame(data)
print("Original DataFrame")
print(df)
df = df.fillna(0)
print("\nAfter Replacing NaN")
print(df)