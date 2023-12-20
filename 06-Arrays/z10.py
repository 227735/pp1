array = [1, 2, 3, 4, 5]
array[0] = array[0] - 1
array[-1] = array[-1] + 4
middle = len(array) // 2
array[middle] = array[middle] * 2
print(array)