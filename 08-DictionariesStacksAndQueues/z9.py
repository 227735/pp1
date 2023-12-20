countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "USA", "population": 331002651},
    {"name": "India", "population": 1380004385},
    {"name": "Brazil", "population": 212559417},
    {"name": "China", "population": 1444216107}
]
print("COUNTRY\tPOPULATION")

index = 0
while index < len(countries):
    country_data = countries[index]
    print(f"{country_data['name']}\t{country_data['population']}")
    index += 1

print()

for country_data in countries:
    country = country_data["name"]
    population = country_data["population"]
    print(f"{country}\t{population}")