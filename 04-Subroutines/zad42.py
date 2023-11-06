def f(number1,number2,number3):
    numbers = []
    numbers.append(number1)
    numbers.append(number2)
    numbers.append(number3)
    max_number = max(numbers)
    min_number = min(numbers)
    return max_number - min_number

print(f(7,4,9))
print(f(2,12,8))