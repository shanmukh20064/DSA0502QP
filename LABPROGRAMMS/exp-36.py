import matplotlib.pyplot as plt
height1 = [150,155,160,165]
weight1 = [45,50,55,60]
height2 = [155,160,165,170]
weight2 = [48,55,60,65]
height3 = [160,165,170,175]
weight3 = [52,58,64,70]
plt.scatter(height1, weight1, label="Group 1")
plt.scatter(height2, weight2, label="Group 2")
plt.scatter(height3, weight3, label="Group 3")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
plt.legend()
plt.show()