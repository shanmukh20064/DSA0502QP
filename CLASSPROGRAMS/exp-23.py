import matplotlib.pyplot as plt
x = []
y = []
with open("data.txt") as f:
    for line in f:
        a, b = line.split()
        x.append(int(a))
        y.append(int(b))
plt.plot(x, y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line Plot from Text File")
plt.show()