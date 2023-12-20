numer = int(input("Podaj liczbę: "))

suma_cyfr = 0

while numer > 0:
    cyfra = numer % 10  # Pobierz ostatnią cyfrę
    suma_cyfr += cyfra  # Dodaj cyfrę do sumy
    numer //= 10  # Usuń ostatnią cyfrę

print("Suma cyfr w liczbie wynosi:", suma_cyfr)
