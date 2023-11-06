def f(x,y):
    count = 0
    for i in range(x,y+1):
        if i % 2 == 0 and i < 0:
            count += 1
    return count

print(f(-7,8))
print(f(-1,11))
