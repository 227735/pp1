def f(word):
    new = []

    dlugosc = len(word)
    for i in range(dlugosc):
        new.append(word[:i] + word[i].capitalize()+ word[i+1:])
    return "-".join(new)

print(f("book"))
print(f(""))


