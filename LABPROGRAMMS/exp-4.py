import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Alphabet.csv")
df["Date"] = pd.to_datetime(df["Date"])
data = df[(df["Date"] >= "2024-01-01") &
          (df["Date"] <= "2024-01-05")]
plt.plot(data["Date"], data["Close"], marker="o")
plt.title("Alphabet Stock Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.grid(True)
plt.show()