import matplotlib.pyplot as plt
language = ["Python","Java","C","C++","JavaScript"]
popularity = [90,80,70,60,85]
plt.bar(language, popularity)
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Programming Language Popularity")
plt.show()