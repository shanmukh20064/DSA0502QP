import matplotlib.pyplot as plt
import numpy as np
group = ["A","B","C","D"]
men = [22,30,35,40]
women = [25,28,32,38]
x = np.arange(len(group))
width = 0.35
plt.bar(x-width/2, men, width, label="Men")
plt.bar(x+width/2, women, width, label="Women")
plt.xticks(x, group)
plt.xlabel("Group")
plt.ylabel("Scores")
plt.title("Scores by Group and Gender")
plt.legend()
plt.show()