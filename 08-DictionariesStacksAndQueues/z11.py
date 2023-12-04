import json

movie = {
    "title":"Snow",
    "year": 2022,
    "actor":{"leading":"Jan Klowlaski","supporting":"Anna Maj"},
    "oscar":False,
}

with open("movie.json", "w", encoding = "utf-8") as file:  
    json.dump(movie, file, indent = 4)