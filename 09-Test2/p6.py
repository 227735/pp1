import json


def f(age, course, average):
    ilosc = 0
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    for student in data:
        if student["age"] >= age:
            courses = student["studies"]["courses"]
            for course1 in courses:
                if (course1["name"] == course):
                    dlugosc = len(course1["grades"])
                    suma = 0
                    for number in course1["grades"]:
                        suma += number
                    avg = suma / dlugosc
                    if avg >= average:
                        ilosc += 1
    return ilosc

print(f(21, "statistics", 4)) 