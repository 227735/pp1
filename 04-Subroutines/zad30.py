def f(number,even):
    number = str(number)    
    parzyste = 0
    odd = 0

    for i in number:
        if int(i) %2 == 0:
            parzyste += int(i)
        else:
            if int (i) %2 != 0:
                odd += int(i)
        
    if even == True:
        return parzyste
    return odd

print(f(3124,True))
print(f(3124,False)) 
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))


        
