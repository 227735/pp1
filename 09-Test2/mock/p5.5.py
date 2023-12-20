def f(arr):
    count = 0
    for row in arr:
        if row[1] == row[0] ** 2:
            count += 1

    return count

two_dimensional_array = [[4, 15], [3, 9], [-3, -9]]
result = f(two_dimensional_array)
print(result)