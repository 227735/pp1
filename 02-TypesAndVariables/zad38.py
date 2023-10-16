number = input("Enter phone number: ")
if len(number) == 9 and number.isdigit():
    print(number[0:3]+"-"+number[3:6]+"-"+number[6:10]) 
else:
    print("Invalid input. Please enter a 9-digit number.")