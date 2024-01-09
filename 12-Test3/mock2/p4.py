def f(fnc, res):
    results = list(filter(fnc, res))

    if not results:
        return -1

    difference = max(results) - min(results)
    return difference

res = [95, 90, 20, 50, 70]
fnc1 = lambda x: x > 50
fnc2 = lambda x: x > 30 and x < 90

print(f(fnc1, res))  # Output: 25
print(f(fnc2, res))  # Output: 20