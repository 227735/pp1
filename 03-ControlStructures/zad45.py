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