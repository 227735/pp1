def f(number,even):
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
        
