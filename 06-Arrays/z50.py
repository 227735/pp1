array = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

smallest_value = float('inf')
largest_value = float('-inf')
smallest_row, smallest_col = 0, 0
largest_row, largest_col = 0, 0

for i, row in enumerate(array):
    for j, value in enumerate(row):
        if value < smallest_value:
            smallest_value = value
            smallest_row, smallest_col = i, j
        if value > largest_value:
            largest_value = value
            largest_row, largest_col = i, j

print(f"Smallest value: {smallest_value} at row {smallest_row + 1}, column {smallest_col + 1}")
print(f"Largest value: {largest_value} at row {largest_row + 1}, column {largest_col + 1}")