import re

def f(text):
    numbers = re.findall(r'\d+', text)
    positive = []
    for num in numbers:
        if int(num) > 0:
            positive.append(int(num))
            total_sum = sum(positive)
    return total_sum

print(f("to ja 23, xd 56"))