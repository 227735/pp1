def is_valid_password(password):
    if len(password) < 6:
        return False

    unique_characters = []
    for i in password:
        if i not in unique_characters:
            unique_characters.append(i)

    return len(unique_characters) >= 6

print(is_valid_password("ax15")) 
print(is_valid_password("book123"))   
print(is_valid_password("A2water3"))
print(is_valid_password("qwerty"))
print(is_valid_password(""))   