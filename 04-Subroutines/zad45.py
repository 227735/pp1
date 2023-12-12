def f(expression):
    try:
        result = eval(expression)
        return result
    except:
        return 0


print(f("")) 
print(f("3+8+1"))   
print(f("2+3-4+5-0"))