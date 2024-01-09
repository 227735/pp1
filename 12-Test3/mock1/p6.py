def f(vname):
    if 1 <= len(vname) <= 5:
        if vname[0].isalpha() or vname[0] == '_':
            for i in vname[1:]:
                if not (i.isalnum() or i == '_'):
                    return False
            return True
    return False

print(f("abc"))
print(f("Abc"))
print(f("aBC"))
print(f("_ab_c"))
print(f("abcdef"))
print(f("8abc"))
print(f("_aB8_"))
print(f("_4x") )
