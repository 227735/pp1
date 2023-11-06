def f(detector):
    count = 0
    max_count = 0
    for i in detector:
        if i == "+":
            count += 1
            max_count = max(max_count, count)
        else:
            if i == "-":
                count -= 1

        if max_count >= 3:
            return True
    return False


print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))

