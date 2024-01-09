def f(uid):
    powt = 0
    for i in uid:
        if uid.count(i) >= 2:
            powt = 1
    if powt == 0:
        return True
    return False

print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))
print(f(["bob2","bob2"]))
print(f(["bob2","BOB2"]) )
