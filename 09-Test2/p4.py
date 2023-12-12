def f(dictionary,x,y):
    suma = 0
    for key, value in dictionary.items():
        for i in value:
            if i in range(x,y+1):
                suma += i
    return suma



print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))
print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10))
