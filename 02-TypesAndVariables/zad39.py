# Enter price: 24.72
# Enter discount %: 15
# Price with discount: 21.01
# Reduction: 3.71

price = float(input("Enter price: "))
discount = int(input("Enter discount %: "))
price_with_discount = price - (discount/100 * price)
reduction = discount/100 * price

print(f"Price with discount: {price_with_discount:.2f}")
print(f"Reduction: {reduction:.2f}")