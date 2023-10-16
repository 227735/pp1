import random

number = random.randrange(1,7)
if number == 1 or number == 6:
    print(f"{number} Your number is special")
else:
    print (number)