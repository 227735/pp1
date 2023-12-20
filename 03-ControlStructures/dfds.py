def check_people_status(input_str):
    count = 0
    for char in input_str:
        if char == '+':
            count += 1
        elif char == '-':
            count -= 1

        if count < 0:
            return False
    return True

# Przykładowe użycie:
status = check_people_status("+++---++-)")
print(status)  # Powinno zwrócić False