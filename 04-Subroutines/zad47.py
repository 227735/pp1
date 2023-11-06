def f(text):
    new = ""
    for i in text:
        new += i +"-"
    return new[:-1]

print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))
