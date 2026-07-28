import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
size = np.random.randint(50,500,50)
plt.scatter(x, y, s=size)
plt.title("Scatter Plot with Different Sizes")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()