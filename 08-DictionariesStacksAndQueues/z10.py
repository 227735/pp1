import json

with open("data.json") as file:
    data = json.load(file)

for item in data:
    print()
    for key, value in item.items():
        print(key, ":", value)