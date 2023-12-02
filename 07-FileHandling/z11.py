file = open("numbers.txt", "r")

suma = 0
for line in file:
    
    number = int(line) 
    suma += number

print(suma)
file.close()