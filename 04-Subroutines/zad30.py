def f(number,even):
<<<<<<< HEAD
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


        
=======
    number = str(number)
    nieparzyste = 0
    parzyste = 0
    for i in number:
        if int(i) % 2 == 0:
            parzyste += int(i)
        else: 
            int(i) % 2 != 0
            nieparzyste += int(i)

    if even == True:
        return parzyste
    else: 
        if even == False:
            return nieparzyste
        
>>>>>>> dc9c90746dd8ab69cda24a3755d970c3034a4d56
