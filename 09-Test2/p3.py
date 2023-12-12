def f(array2D):
    columns = len(array2D[0])
    column_sums = [0] * columns

    for row in array2D:
        for j in range(columns):
            column_sums[j] += row[j]

    return column_sums

# def f(array_2d):
#     return [sum(column) for column in zip(*array_2d)]


print(f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) )

def f(array2D):
    sums = []
    for i in range(0,len(array2D[0])):
        sums.append(0)

    for i in range(0,len(array2D)):
        for j in range(0,len(array2D[i])):
            sums[j] += array2D[i][j]
    return sums

print(f([[3,6,2,7], [9,5,4,0], [2,8,0,9]]) )





#suma cyfr w rzedach

# array2D = [3,6,2,7], [9,5,4,0], [2,8,0,9]

# array1D = []

# sum = 0
# for rows in array2D:
#     for col in rows:
#         sum += col
#     print(sum)
#     array1D.append(sum)

# print(array1D)