def f(number):
    sum = 0
    string = str(number)
    for i in string:
        if string.count(i) >= 2:
            sum += int(i)
    return sum
        
print(f(230335))