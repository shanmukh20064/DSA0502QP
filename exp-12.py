import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(1,100,size=(10,4)),
                  columns=["A","B","C","D"])
print(df)
df.style.set_properties(**{
    "background-color":"black",
    "color":"yellow"
})