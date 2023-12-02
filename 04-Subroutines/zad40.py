def f(number):
    number_str = str(number)
    total = 0

    for digit in number_str:
        if number_str.count(digit) > 1:
            total += int(digit)

    return total

print(f(230335))