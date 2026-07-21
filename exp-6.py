import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Alphabet.csv")
df["Date"] = pd.to_datetime(df["Date"])
data = df[(df["Date"] >= "2024-01-01") &
          (df["Date"] <= "2024-01-05")]
plt.scatter(data["Volume"], data["Close"])
plt.title("Trading Volume vs Closing Price")
plt.xlabel("Volume")
plt.ylabel("Closing Price")
plt.grid(True)
plt.show()