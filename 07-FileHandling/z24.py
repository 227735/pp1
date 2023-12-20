import csv

with open("studentslist.txt", "r", encoding = "utf-8") as file:
    # csvreader = csv.reader(file, delimiter = ",")
    csvreader = csv.DictReader(file)

    for row in csvreader: 
        name = row["first_name"]
        last_name = row["last_name"]
        email = row["email"]
        age = row["age"]

        if int(age) < 30:
            print(name, last_name ,email )
