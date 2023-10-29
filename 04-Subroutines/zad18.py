def numbers(n):
    string = " "
    for i in range(1,n+1):
        string += (str(i)) + " "
    return string.strip()

print(numbers(15))

