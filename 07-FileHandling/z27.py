import re

text = "To be, or not to be, that is the question"

wzór = r'\b\w+\b'

words = re.findall(wzór, text)

print(len(words))