array = [[True,False],[True,True],[False,False]]

for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = not array[i][j] 

print(array)