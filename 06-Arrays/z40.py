def f(arr):
    line = "-" * 41
    formatted_str = line + "\n|"
    for num in arr:
        formatted_str += f"{num:4}|"
    formatted_str += "\n" + line
    return formatted_str

print(f([1,34,567,567,456,23,3,459]))