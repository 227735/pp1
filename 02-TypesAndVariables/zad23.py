a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

obwód = a + b + c
połowa_obwodu = s = int(obwód / 2)
pole = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(obwód, pole)