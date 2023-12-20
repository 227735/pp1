arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = arr[0]

for i in arr:
    if len(i) > len(longest):
        longest = i

print(longest)
