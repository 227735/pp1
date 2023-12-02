def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

array_a = ["water", "book", "sky"]
array_b = ["water", "book", "sky"]
array_c = [True, False]
array_d = [True, False, True]
array_e = [5, 3, 1]
array_f = [5, 3, 1]
array_g = [3, 2, 1]
array_h = [3, 2]

print(compare(array_a, array_b))
print(compare(array_c, array_d))
print(compare(array_e, array_f))
print(compare(array_g, array_h))