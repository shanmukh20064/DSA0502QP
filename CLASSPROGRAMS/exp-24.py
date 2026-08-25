import matplotlib.pyplot as plt
year = [2019,2020,2021,2022,2023]
income = [45000,50000,52000,61000,70000]
plt.plot(year, income, marker="o")
plt.xlabel("Year")
plt.ylabel("Income")
plt.title("Financial Data")
plt.grid()
plt.show()