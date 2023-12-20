# def decimal_to_binary(number):
#     stack = []

#     while number > 0:
#         remainder = number % 2
#         stack.append(remainder)
#         number //= 2

#     binary_result = ""
#     while stack:
#         binary_result += str(stack.pop())

#     return binary_result

# decimal_number = int(input("Enter a natural number: "))
# binary_number = decimal_to_binary(decimal_number)
# print(f"The binary representation of {decimal_number} is: {binary_number}")


def decimal_to_binary(n):
    stack = []

    # Perform division and push remainders onto the stack
    while n > 0:
        remainder = n % 2
        stack.append(remainder)
        n //= 2

    # Pop and display values from the stack
    binary_number = ""
    print("Division\tRemainder")
    for _ in range(len(stack)):
        current_remainder = stack.pop()
        binary_number += str(current_remainder)
        print(f"{n * 2} / 2 = {n}\t\t{current_remainder}")

    return binary_number[::-1]

# Example: Convert the natural number 18 to binary
natural_number = 18
binary_result = decimal_to_binary(natural_number)

print(f"\nNatural number: {natural_number}")
print(f"Binary number: {binary_result}")