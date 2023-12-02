with open ("MeatAndFish.txt", "r") as file1:
    with open ("GrainsAndBread.txt", "r") as file2:
        with open("allproducts.txt", "a") as file3:
            file3.write(file1.read())
            file3.write(file2.read())
