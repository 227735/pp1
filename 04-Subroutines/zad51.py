def sum(n):
    if n <= 0:
        return 0
    else:
        return n + sum(n - 1)

result = sum(10)
print("The sum of natural numbers from 1 to 10 is:", result)