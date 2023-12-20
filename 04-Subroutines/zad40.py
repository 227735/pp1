def f(number):
<<<<<<< HEAD
    sum = 0
    string = str(number)
    for i in string:
        if string.count(i) >= 2:
            sum += int(i)
    return sum
        
=======
    number_str = str(number)
    total = 0

    for digit in number_str:
        if number_str.count(digit) > 1:
            total += int(digit)

    return total

>>>>>>> dc9c90746dd8ab69cda24a3755d970c3034a4d56
print(f(230335))