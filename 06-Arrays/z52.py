def swapKolumn(input_array):
    for row in input_array:
        row[0], row[-1] = row[-1], row[0]

    for row in input_array:
        print(row)

