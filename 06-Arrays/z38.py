def f(arr, value):
    count = 0
    for num in arr:
        if num > value:
            count += 1
    return count

result = f([1,2,3,4,5,6,7,8,9], 2)
print(result)