def different(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n1 != n3:
        return True
    return False

n1 = input("Enter first number: ")
n2 = input("Enter second number: ")
n3 = input("Enter third number: ")

print(different(n1,n2,n3))

if different:
    print(f"Numbers {n1}, {n2}, and {n3} are different.")
else:
    print("The numbers are not all different.")