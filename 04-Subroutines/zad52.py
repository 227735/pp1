def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

result = power(5, 3)
print("5^3 is:", result)