def f(array2D):
    rows, cols = len(array2D), len(array2D[0])
    if rows != cols:
        return False

    for i in range(rows):
        row_sum = 0
        col_sum = 0
        for j in range(cols):
            row_sum += array2D[i][j]
            col_sum += array2D[j][i]

        if row_sum != col_sum:
            return False
    return True
