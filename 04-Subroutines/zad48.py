def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False 

    first_three_digits = int(product_code[:3])
    control_digit = int(product_code[3])
    digit_sum = 0
    
    for i in str(first_three_digits):
        digit_sum += int(i)

    remainder = digit_sum % 7
    return control_digit == remainder

print(f("1082"))  # Returns True
print(f("2035"))  # Returns True
print(f("1114"))  # Returns False
print(f("7071"))  # Returns False