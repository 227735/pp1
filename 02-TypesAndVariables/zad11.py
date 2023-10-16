fincome = int(input("Enter father’s income:"))
mincome = int(input("Enter mother’s income:"))
number = int(input("Enter number of people in family:"))
Total_income = int(fincome) + int(mincome)
per_person = (Total_income/number)
print(f"Income perp person is: {per_person}")

