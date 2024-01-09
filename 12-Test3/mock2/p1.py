def f(n):
    odd = []
    for i in str(n):
        if int(i) % 2 != 0:
            odd += i

    if len(odd) < 1:
        return -1
    
    największa = int(max(odd))
    najmniejsza = int(min(odd))
    roznica = największa - najmniejsza
    return roznica

print(f(10852))
print(f(7235973))
print(f(4388))
print(f(846206))

