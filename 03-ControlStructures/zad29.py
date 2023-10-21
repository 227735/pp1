washing_product = input("Washing product: ")
rinse = True
spin = False

total_washing_time = 0 

if washing_product == "shoes":
    total_washing_time = 20
elif washing_product == "jacket":
    total_washing_time = 40
else:
    if washing_product == "underwear":
        total_washing_time = 70

if rinse:
    total_washing_time += 15

if spin:
    total_washing_time += 9

print(f"Total washing time: {total_washing_time} minutes")