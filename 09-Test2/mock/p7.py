import re

def f(arr):
    count = 0
    for username in arr:
        if re.match("^[a-z0-9_]{4,12}$", username):
            count += 1

    return count

usernames = ["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]
result = f(usernames)
print(result)  # Output: 2