array = [-15, 8, -31, 47, -2, 19]

max_number = array[0]
min_number = array[0]

for number in array:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print("Array:", array)
print("Maximum number:", max_number)
print("Minimum number:", min_number)