def f(d, v):
    count = 0 
    for key, value in d.items():
        if value != v:
            count += 1
    return count

dictionary_example = {'a': True, 'b': False, 'c': True, 'd': True, 'e': False}
value_example = True
result = f(dictionary_example, value_example)
print(result)