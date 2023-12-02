array = [15, 8, 31, 47, 2, 19]

sum_values = 0
count = 0
index = 0

while index < len(array):
    sum_values += array[index]
    count += 1
    index += 1

if count != 0:
    mean = sum_values / count
    print("Arithmetic mean:", mean)
else:
    print("Cannot calculate mean. The array is empty.")