def f(arr):
    suma = 0
    for row in arr:
        ostatni = row[-1]
        suma += ostatni
    return suma

print(f([
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]))

def column_sums(array):
    column_sums = [0] * len(array[0])

    for row in array:
        for i in range(len(row)):
            column_sums[i] += row[i]

    return column_sums

print(column_sums([
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]))



