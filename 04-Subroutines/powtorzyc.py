for i in range(0, 7):
    for j in range(0, 7):
        print(i+1 + j*7, end=" ")
    print()

n = int(input("Podaj liczbę n: "))
number = 2
prime = []

def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

while len(prime) < n:
    if(czy_pierwsza(number)):
        prime.append(number)
    number += 1


print(prime)


a = 0
b = 1
for _ in range(20):
    print(a, end=' ')
    a, b = b, a + b

for i in range(6,-1,-3):
    for j in range(1,4):
        print(f' {i+j}',end='')
    print()

print()

i = 6
while i >= 0:
    j = 1
    while j <= 3:
        print(f' {i+j}', end='')
        j += 1
    print()
    i -= 3

a = int(input("Enter the width (a): "))
b = int(input("Enter the height (b): "))

for i in range(a):
    if i == 0 or i == a - 1:
        print("*" * b)
    else:
        print("*" + " " * (b - 2) + "*")

rows = 9

for i in range(1, rows + 1):
    print(str(i) * i)

rows = 5

for i in range(1, rows * 2):
    if i <= rows:
        print("* " * i)
    else:
        print("* " * (rows * 2 - i))

number = int(input("Enter number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

amount = int(input("Enter the amount in PLN: "))

piątki = int(amount / 5)
reszta_z_piątek = int(amount % 5)
dwójki = int(reszta_z_piątek / 2)
reszta_z_dwójek = int(reszta_z_piątek % 2)
jedynki = int(reszta_z_dwójek / 1)


print("The amount of PLN 18 in coins: ")
print(f"5 zł : {piątki}")
print(f"2 zł : {dwójki}") 
print(f"1 zł : {jedynki}")

decimal_number = int(input("Enter decimal number: "))

binary_number = ""
iloraz = decimal_number

while iloraz > 0:
    reszta = iloraz % 2
    binary_number = str(reszta) + binary_number
    iloraz = iloraz // 2

print(f"{decimal_number}(10) = {binary_number}(2)")

time_24_hour = input("Enter time (24-hour format):")

hours, minutes = map(int, time_24_hour.split(':'))

period = "am" if hours < 12 else "pm"

if hours == 0:
    hours_12_hour = 12
elif hours <= 12:
    hours_12_hour = hours
else:
    hours_12_hour = hours - 12

print(f"Time in 12-hour format: {hours_12_hour}:{minutes:02d}{period}")


age = int(input("Enter dog's years: "))

if age == 2:
    human_age = int((age * 10.5))
elif age == 1:
        human_age = 10.5
else:
    human_age = (int((age - 2) * 4 + 2 * 10.5))
print(human_age)

for i in range(1, 11):
    dzielenie = 1 / i
    print(f'1/{i} = {dzielenie}')

binary_number = input("Enter binary number (4 digits): ")

if len(binary_number) == 4 and all(bit in '01' for bit in binary_number):
    decimal_number = int(binary_number, 2)
    print(f"Binary number in decimal notation: {decimal_number}")
else:
    print("Invalid input. Please enter a valid binary number with 4 digits.")










