def f(arr):
    suma = 0
    for i in arr:
        if arr.count(i) == 1:
            suma += 1
    return suma

print(f([11,22,33,11]))