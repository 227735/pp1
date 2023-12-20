def fibonacci_nth(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

n = 10
result = fibonacci_nth(n)
print(result)


# def fibonacci_sum(n):
#     fib_sum = 0
#     a, b = 0, 1

#     for _ in range(n):
#         fib_sum += a
#         a, b = b, a + b

#     return fib_sum

# n = 10
# result = fibonacci_sum(n)
# print(result)
