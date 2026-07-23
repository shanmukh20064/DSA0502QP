import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Alphabet.csv")
df["Date"] = pd.to_datetime(df["Date"])
data = df[(df["Date"] >= "2024-01-01") &
          (df["Date"] <= "2024-01-05")]
plt.bar(data["Date"].dt.strftime("%Y-%m-%d"), data["Volume"])
plt.title("Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.xticks(rotation=45)
plt.show()