import matplotlib.pyplot as plt
language = ["Python","Java","C","C++","JavaScript"]
popularity = [90,80,70,60,85]
color = ["red","green","blue","orange","purple"]
plt.bar(language, popularity, color=color)
plt.title("Programming Language Popularity")
plt.show()