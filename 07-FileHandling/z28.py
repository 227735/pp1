import re 

with open ("z10.txt", "r") as file:
    file_content = file.read()
    wzór = r'\b\w{6,}\b'
    words = re.findall(wzór, file_content)

for word in words:
    print(word)

