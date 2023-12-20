def f(first_letter, last_letter):
    with open("data.txt", "r", encoding="utf-8") as file:
        suma = 0
        content = file.read().split()
        for word in content:
            if word.lower().startswith(first_letter.lower()) and word.lower().endswith(last_letter.lower()):
                suma += 1
        return suma

print(f("w", "d"))


def f(first_letter,last_letter):
    count = 0
    f = open("test.txt","r",encoding = "UTF-8")
    wiersze = f.readlines()
    
    for linia in wiersze:
        linijka = linia.strip().split()
        for slowo in linijka:
            if len(slowo) > 0:
                if(slowo[0] == first_letter and slowo[-1] == last_letter):
                    count += 1
    return count

print(f("w", "d"))