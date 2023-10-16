import random

computer_number = random.randrange(1,7)

number = input("Enter number between 1 snd 6: ")
if number == computer_number:
    print("Congrats, you won")
else:
    print("Your number is wrong")