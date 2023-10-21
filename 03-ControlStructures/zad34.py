amount = int(input("Enter the amount in PLN: "))

piątki = int(amount / 5)
reszta_z_piątek = int(amount % 5)
dwójki = int(reszta_z_piątek / 2)
reszta_z_dwójek = int(reszta_z_piątek % 2)
jedynki = int(reszta_z_dwójek / 1)


print("The amount of PLN 18 in coins: ")
print(f"5 zł : {piątki}")
print(f"2 zł : {dwójki}") 
print(f"1 zł : {jedynki}")

