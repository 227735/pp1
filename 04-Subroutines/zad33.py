def f(n):
    string = ""
    if n == 1:
        return ("*")
    else:
        if n != 1:
            string += "*/" * n
        return string[0:-1]
    
print(f(4))