# def f(name):
#     words = name.split()
#     letters = " "
#     for i in words:
#         letters += i[0]
#     return letters.strip()

# print(f("Internet of Things"))
        
zdanie = "Internet of Things"
string = ""

for i in zdanie.split():
    string += i[0]

print(string)
