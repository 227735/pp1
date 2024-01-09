def f(arr2D):
    for row in arr2D:
        row[0], row[-1] = row[-1], row[0]

    return arr2D

print(f([[1, 2], [3, 4]]))
print(f([[1, 2,3,4], [5,6,7,8]]))