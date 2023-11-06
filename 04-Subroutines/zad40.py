def f(number):
    for i in number:
        if i.count() > 1:
            return sum(i)
        
print(f(230335))