import random

def rand_elem(array):
    return random.choice(array)

my_array = [1, 5, 9, 3, 7, 2, 8, 4, 6]

for _ in range(3):
    print(rand_elem(my_array))
