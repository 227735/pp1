def is_subset(first_array, second_array):
    for element in first_array:
        if element not in second_array:
            return False
    return True


print(is_subset([2, 4, 5, 24, 2, 5, 2], [1, 2, 3, 4, 5, 6, 7]))
