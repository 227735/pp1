name = input("Enter your name: ")

for letter in name:
    numerical_representation = ord(letter)
    print(f"{letter}({numerical_representation})", end=" ")
print("Name:", name)