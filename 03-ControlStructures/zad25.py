number_of_products_purchased = int(input("Enter number of products purchased: "))
product_price = int(input("Enter product price: "))

if number_of_products_purchased > 2:
    amount_to_pay = (number_of_products_purchased - 2) * product_price * 0.75 + 2 * product_price
else:
    amount_to_pay = number_of_products_purchased * product_price
print(f"Amount to pay: {amount_to_pay}")