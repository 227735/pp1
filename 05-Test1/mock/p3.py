def f(name):
    words = name.split()
    letters = " "
    for i in words:
        letters += i[0]
    return letters.strip()

print(f("Internet of Things"))
        