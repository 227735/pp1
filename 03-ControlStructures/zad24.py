Current_price = 140.00
Previous_price = 200.00

decreas = 100 - ((100 * Current_price) / Previous_price)

if decreas > 10:
    print(f"Buy the product! Product price reduced by {decreas}%")
else:
    print("Don't buy it.")
