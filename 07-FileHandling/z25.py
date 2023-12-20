import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)

ilosc = len(temperatures)
suma = 0

for i in temperatures:
    suma += int(i)

average = suma / ilosc

print(average)

