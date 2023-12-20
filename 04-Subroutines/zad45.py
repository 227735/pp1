def f(expression):
    try:
        result = eval(expression)
        return result
    except:
        return None


print(f("")) 
print(f("3+8+1"))   
print(f("2+3-4+5-0"))