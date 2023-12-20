def create_2d_arr(x, y):
    return [[0 for _ in range(y)] for _ in range(x)]

def display_2d_arr(arr):
    for row in arr:
        print(row)

my_array = create_2d_arr(3, 5)

display_2d_arr(my_array)