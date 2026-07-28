import json
from collections import Counter
# Read JSON file
with open("movies.json", "r") as file:
    movies = json.load(file)
# Display all movie titles
print("Movie Titles:")
for movie in movies:
    print(movie["Title"])
# Find movies released after 2020
filtered = [movie for movie in movies if movie["Year"] > 2020]
print("\nMovies Released After 2020:")
for movie in filtered:
    print(movie["Title"], "-", movie["Year"])
# Count movies in each genre
genres = [movie["Genre"] for movie in movies]
count = Counter(genres)
print("\nMovies in Each Genre:")
for genre, total in count.items():
    print(genre, ":", total)
# Save filtered dataset
with open("filtered_movies.json", "w") as file:
    json.dump(filtered, file, indent=4)
print("\nFiltered dataset saved as filtered_movies.json")