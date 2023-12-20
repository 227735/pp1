movie_titles = ["The Hunger Games", "The Snow", "Balllad", "Songsbirds", "Coriolanus"]
file = open("movies.txt", "w")

for title in movie_titles:
    file.write(title + "\n")

file.close()