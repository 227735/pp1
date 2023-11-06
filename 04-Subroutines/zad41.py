def f(n):
    liczba_pierwsza = 2
    kandydat = 3

    while n > 1:
        for i in range(2, int(kandydat**0.5) + 1):
            if kandydat % i == 0:
                break
        else:
            liczba_pierwsza = kandydat
            n -= 1
        kandydat += 2

    return liczba_pierwsza

print(f(1))
print(f(5))