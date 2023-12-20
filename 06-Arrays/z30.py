def bubblesort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

array1 = [9, 5, 7, 2, 8]
array2 = [12, 4, 1, 9, 6]
array3 = [5, 2, 10, 1, 7]

print("Original array 1:", array1)
print("Sorted array 1:", bubblesort(array1))

print("\nOriginal array 2:", array2)
print("Sorted array 2:", bubblesort(array2))

print("\nOriginal array 3:", array3)
print("Sorted array 3:", bubblesort(array3))