import matplotlib.pyplot as plt
plt.subplot(2,1,1)
plt.plot([1,2,3],[2,4,6])
plt.title("First Plot")
plt.subplot(2,1,2)
plt.plot([1,2,3],[6,4,2])
plt.title("Second Plot")
plt.tight_layout()
plt.show()