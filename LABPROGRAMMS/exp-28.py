import matplotlib.pyplot as plt
language = ["Python","Java","C","C++","JavaScript"]
popularity = [90,80,70,60,85]
plt.barh(language, popularity)
plt.xlabel("Popularity")
plt.title("Horizontal Bar Chart")
plt.show()