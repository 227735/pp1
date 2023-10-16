Description = "Mr. John May, born on 1998-02-16"
Name = Description[4:8]
Surname = Description[9:12]
Initials = Description[4] + Description[9]
Born = Description[24:]

print (f"Description: {Description}")
print (f"Name: {Name}")
print (f"Surname: {Surname}")
print (f"Initials: {Initials}")
print (f"Born: {Born}")