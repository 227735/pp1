array = 34,7,19,4,21,8

even_count = 0
index = 0

while index < len(array):
    if array[index] % 2 == 0:
        even_count += 1
    index += 1

print(even_count)