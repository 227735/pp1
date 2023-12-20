import csv
import json

with open("products.csv", "r") as csvfile:
    products_data = []
    csvreader = csv.DictReader(csvfile)
    for i in csvreader:
        products_data.append(i)

with open("products.json", "w") as jsonfile:
    json.dump(products_data, jsonfile, indent = 4)

print(products_data)








