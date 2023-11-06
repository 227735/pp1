def f(sentence): 
    new = ""

    for i in sentence:
        new += i.strip()
    return new

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs") )
