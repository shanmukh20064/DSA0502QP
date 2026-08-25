import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(10,4),
    columns=["A","B","C","D"]
)
df.iloc[2,1] = np.nan
df.iloc[5,3] = np.nan
def highlight_nan(x):
    if pd.isna(x):
        return "background-color: yellow"
    return ""
styled = df.style.applymap(highlight_nan)
styled.to_html("Question11_Output.html")
print("Output saved as Question11_Output.html")