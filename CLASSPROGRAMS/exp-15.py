import pandas as pd
import numpy as np
data = {
    "A":[1,np.nan,np.nan,4],
    "B":[np.nan,np.nan,7,8],
    "C":[9,np.nan,np.nan,np.nan]
}
df = pd.DataFrame(data)
result = df[df.isnull().sum(axis=1)>=2]
print(result)