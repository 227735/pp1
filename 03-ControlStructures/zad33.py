decimal_number = int(input("Enter decimal number: "))

binary_number = ""
iloraz = decimal_number

while iloraz > 0:
    reszta = iloraz % 2
    binary_number = str(reszta) + binary_number
    iloraz = iloraz // 2

print(f"{decimal_number}(10) = {binary_number}(2)")
