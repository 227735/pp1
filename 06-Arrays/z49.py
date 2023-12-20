array = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for i in range(1, 6):
    for j in range(1, 6):
        array[i-1][j-1] = i * j
        
for row in array:
    print(" ".join(map(str, row)))