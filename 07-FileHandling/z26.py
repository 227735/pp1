import re

text = "To be, or not to be, that is the question"

vowels = re.findall("[aeiouAEIOU]", text)

print(len(vowels))