with open ("z10.txt", "r") as file1:
    with open("copylines.txt", "w") as file2:
        for line in file1:
            file2.write(line)