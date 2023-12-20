def f(subjects):
    highest_avg_subject = None
    highest_avg = 0

    for key, values in subjects.items():
        suma = sum(values)
        dlugosc = len(values)
        avg = suma / dlugosc

        if avg > highest_avg:
            highest_avg = avg
            highest_avg_subject = key

    return highest_avg_subject

print(f({"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]}))




        













# def f(dictionary,x,y):
#     suma = 0
#     for key, value in dictionary.items():
#         for i in value:
#             if i in range(x,y+1):
#                 suma += i
#     return suma

# print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))
# print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10))
