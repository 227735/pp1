array = [15, 8, 31, 47, 2, 19]

reverse_array = []
for i in range(len(array)-1, -1, -1):
    reverse_array.append(array[i])


# reverse_array = array[::-1]
print(reverse_array)