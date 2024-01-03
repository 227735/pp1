class C():
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        if self.age < 18:
            return self.surname.lower() + self.name[0].lower() + str(self.seniority)
        else:
            return self.surname.upper() + self.name[0].upper() + str(self.seniority)

c1 = C("Anna", "May", 17, 7)
print(c1)
c2 = C("George", "Brown", 21, 4)
print(c2)


