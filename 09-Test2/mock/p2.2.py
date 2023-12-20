def f(d):
    count = 0 

    for i in d:
        if i == '+':
            count += 1 
        elif i == '-':
            count -= 1 

    return count

recorded_information = "+-+++++-"
result = f(recorded_information)
print(result)