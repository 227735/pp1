import csv

def f(num):
    with open("data.csv","r", encoding="utf-8") as file:
        content = csv.DictReader(file)

        suma = 0

        for line in content:
            dzieci = line["children"]
            if int(dzieci) > num:
                suma += 1
        return suma
    
print(f(0))