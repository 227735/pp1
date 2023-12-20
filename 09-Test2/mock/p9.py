def f(arr):
    suma = 0
    for row in arr:
        if row[0] >= 0:
            suma += row[0]
        if row[1] >=0:
            suma -= row[1]
    return suma

print(f([[3,0], [2,1]]))



