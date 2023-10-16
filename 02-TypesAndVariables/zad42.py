binary_number = input("Enter binary number (4 digits): ")

if len(binary_number) == 4 and all(bit in '01' for bit in binary_number):
    decimal_number = int(binary_number, 2)
    print(f"Binary number in decimal notation: {decimal_number}")
else:
    print("Invalid input. Please enter a valid binary number with 4 digits.")