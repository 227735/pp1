import re
with open ("grades.txt", "r") as file:
    content = file.read()

    grades_match = re.search(r'Grades: (.+)', content, re.DOTALL)
    if grades_match:
        grades_str = grades_match.group(1).split(', ')
        grades = [float(grade) for grade in grades_str]

        mean_grade = sum(grades) / len(grades)

print(mean_grade)



