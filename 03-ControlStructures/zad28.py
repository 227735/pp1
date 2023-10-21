EAN = str(input("Enter EAN: "))

if len(EAN) == 13 and EAN[:3] == "590":
    print("Article number is correct. Article manufactured in Poland")
else:
    print("Article number isn't correct or article manufactured not in Poland")