def f(card_number):
    new = card_number[0:1]+ "**********"+ card_number[12:16]
    return new

print(f("5290312400019022") )