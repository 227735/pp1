height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

BMI = (weight / (height ** 2))

print(round(BMI, 1))
