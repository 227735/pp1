'''
(p1.py) The vending machine accepts
1, 2 and 5 PLN coins. Define the function
f(amount_to_pay) that returns the minimum number
of coins that can be used to pay
for the purchased product.
'''

def f(amount_to_pay):
    coins = 0
    coins += amount_to_pay // 5
    amount_to_pay = amount_to_pay % 5
    coins += amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2
    coins += amount_to_pay // 1
    return coins
