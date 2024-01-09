def f(arr):
    for i in arr:
        if arr.count(i) % 2 != 0:
            return i
        
print(f([3,3,4,4,4,2,2,2,2]))
print(f([6,6,6,6,4,4,5,2,2,2,2,2,2]))