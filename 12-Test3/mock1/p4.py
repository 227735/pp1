def f(fnc, prods):
    result = ','.join(map(fnc, prods))
    return result

prods = ["water", "cheese", "tomato"]
fnc1 = lambda x: "id:" + x[:2]
fnc2 = lambda x: (x[0] + x[-1]).upper()

result1 = f(fnc1, prods)
result2 = f(fnc2, prods)

print(result1)  # "id:wa,id:ch,id:to"
print(result2)  # "WR,CE,TO"