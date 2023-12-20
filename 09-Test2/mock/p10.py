def f(arr):
    for i in arr:
        if arr.count(i) % 2 != 0:
            return i

print(f([7,7,7,7,4,4,4,5,5]))


