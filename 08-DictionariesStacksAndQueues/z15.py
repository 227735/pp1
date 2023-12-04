basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}

person = basic_data.copy()
person.update(advanced_data)

print(person)

# person = {
#     **basic_data,
#     **advanced_data
# }