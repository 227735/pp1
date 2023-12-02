array = [2, 3, 7, 5, 4]
print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[-1])
print(array[-2])

sum = array[0] + array[-1]
print(sum)

middle = len(array) //2
print(array[middle])

for i in array:
    print(i,end=" ")

print( )

for j in array[:middle]:
    print(j,end =" ")

