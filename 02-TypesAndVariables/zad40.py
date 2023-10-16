number = input("Enter credid card number: ")
if len(number) == 16 and number.isdigit():
    print(number[0:4]+" "+number[4:8]+" "+number[8:12]+" "+number[12:16]) 
else:
    print("Invalid input. Please enter a 9-digit number.")