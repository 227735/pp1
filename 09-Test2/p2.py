def f(human_age):
    if human_age <= 2:
        dog_age = human_age * 10
    else:
        dog_age = 2 * 10 + (human_age - 2) * 4
    return dog_age

result1 = f(15)
result2 = f(2)

print(result1)
print(result2) 