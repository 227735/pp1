import re

def f(text):
    numbers = re.findall(r'\b\d+\b', text)
    positive = []
    for num in numbers:
        if int(num) > 0:
            positive.append(int(num))
    total_sum = sum(positive)
    return total_sum

text_example = "11 and 4 is 15"
result = f(text_example)
print(result)  