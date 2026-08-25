import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(-50,50,size=(10,4)),
                  columns=["A","B","C","D"])
def color(val):
    if val < 0:
        return "color:red"
    else:
        return "color:black"
print(df)
df.style.applymap(color)