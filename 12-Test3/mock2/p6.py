import re

def f(mnumbers):
    pattern = re.compile(r'^[+-]?[1-7a-dA-D]+$')
    return sum(1 for num in mnumbers if pattern.match(num))

# Example usage:
result1 = f(["A15", "-31", "7abC", "+D1", "-gH"])
result2 = f(["A05", "-3+1", "7ab8C", "+D1", "-22k"])

print(result1)  # Output: 5
print(result2)  # Output: 1