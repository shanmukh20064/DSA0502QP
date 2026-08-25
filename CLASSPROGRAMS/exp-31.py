import matplotlib.pyplot as plt
boys = [20,25,30,35]
girls = [15,20,25,30]
error = [2,3,2,1]
x = ["A","B","C","D"]
plt.bar(x, boys, yerr=error, label="Boys")
plt.bar(x, girls, bottom=boys, yerr=error, label="Girls")
plt.xlabel("Group")
plt.ylabel("Marks")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()