import json

with open("students.json", "r") as file:
    students_data = json.load(file)

    limited_students = [ {
        "first_name" : student["name"],
        "first_surname" : student["surname"],
        "student_id" : student["student_id"]
    }

    for student in students_data
    ]

with open("limited.json", "w") as file:
    json.dump(limited_students, file, indent=2)