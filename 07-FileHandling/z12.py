name = "Monika Klosowska"
university = "Krakow University of Economics"
field = "Applied Informatics"

file = open("student.txt", "w")
file.write(name+"\n")
file.write(university+"\n")
file.write(field+"\n")

file.close()
