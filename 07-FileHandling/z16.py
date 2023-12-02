name = input("Enter file name: ")

with open(name, "r") as file:
    count = 0
    for line in file:
        count += 1

print(count)