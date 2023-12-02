array = [[1,3,5],[8,7,2]]

# a.	Sum of the first element in the first row and the last element in the last row
print(array[0][0] + array[-1][-1])
# b.	Sum of the elements in the middle column
print(array[0][1] + array[1][1])

# num_rows = len(array)
# num_columns = len(array[0])  # Zakładamy, że liczba kolumn w każdym wierszu jest taka sama

# if num_columns > 1:
#     middle_column_index = num_columns // 2
#     sum_b = sum(row[middle_column_index] for row in array)
#     print("b. Sum of the elements in the middle column:", sum_b)
# else:
#     print("b. Unable to calculate the sum as there is only one column.")

# c.	Sum of the elements in the last row
print(sum(array[-1]))

