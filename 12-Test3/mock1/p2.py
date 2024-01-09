def f(x,y,digit):
    liczby = ""
    for i in range(x,y+1):
        liczby += str(i)
    return liczby.count(str(digit))

print(f(10,15,1))
print(f(28,32,2))
print(f(100,105,6))
print(f(100,101,0))


