import random

with open ("z22.txt", "a") as file:
    for _ in range(51):
        randomowy = random.randint(100,999)
        file.write(str(randomowy))
        file.write("\n")
        
