def f(arr):
    even_numbers = []
    odd_numbers = []

    for i in arr:
       if i % 2 == 0:
           even_numbers.append(i)

    for i in arr:
       if i % 2 != 0:
           odd_numbers.append(i)

    return even_numbers + odd_numbers

print(f([1,2,3,4,5,6,7,8,9,10,12,13,14]))
