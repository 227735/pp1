interested = input("Are you interested in computer science? (Y/N): ") 
playing = input("Do you like playing computer games? (Y/N): ")
instagram = input("Do you have an Instagram account? (Y/N): ")

if interested == "T":
    odp_int = "Yes"
else:
    odp_int = "No"

if playing == "T":
    odp_pl = "Yes"
else:
    odp_pl = "No"

if instagram == "T":
    odp_inst = "Yes"
else:
    odp_inst = "No"
    

print(f"Interested in computer science: {odp_int}")
print(f"Playing computer games: {odp_pl}")
print(f"Has an Instagram account: {odp_inst}")
