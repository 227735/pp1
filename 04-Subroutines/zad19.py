# numer = int(input("Podaj liczbę: "))

# suma_cyfr = 0

# while numer > 0:
#     cyfra = numer % 10  # Pobierz ostatnią cyfrę
#     suma_cyfr += cyfra  # Dodaj cyfrę do sumy
#     numer //= 10  # Usuń ostatnią cyfrę

# print("Suma cyfr w liczbie wynosi:", suma_cyfr)


numbers = []
number  =123

for i in str(number):
    numbers.append(int(i))
print(numbers)

suma = 0
for i in numbers:
    suma += i
print(suma)