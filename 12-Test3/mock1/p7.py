def f(arr2D):
    column_sums = [sum(col) for col in zip(*arr2D)]
    for i in range(len(column_sums)):
        for j in range(i + 1, len(column_sums)):
            if column_sums[i] == column_sums[j]:
                return True
    return False

arr1 = [[3, 4, 2], [5, 1, 6]]
arr2 = [[3, 4, 2], [5, 1, 7]]
arr3 = [[3, 4], [5, 1], [4, 7]]
arr4 = [[3, 4], [5, 9], [4, 7]]

print(f(arr1))
print(f(arr2))
print(f(arr3))
print(f(arr4))