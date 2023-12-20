with open ("z23.txt", "a") as file:
    for i in range(1,11):
        file.write(str(i) + ",")
        file.write(str(i **2) + ",")
        file.write(str(i **3))
        file.write("\n")
        
