import matplotlib.pyplot as plt
maths = [75,80,65,90,85,70,95]
science = [70,82,60,88,84,72,96]
plt.scatter(maths, science)
plt.xlabel("Maths Marks")
plt.ylabel("Science Marks")
plt.title("Maths vs Science")
plt.show()