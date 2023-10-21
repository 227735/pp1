numbers = []
n = 1
while (n != 0):
    n = int(input("Wprowadź liczbę: "))
    if(n != 0):
        numbers.append(n)
quantity = len(numbers)
sum = 0
for i in range(0, len(numbers)):
    sum += numbers[i]
mean = sum / quantity

print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={int(mean)}")