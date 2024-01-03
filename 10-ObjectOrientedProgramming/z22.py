class Contact:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"{self.name}\t{self.email}\t{self.telephone}"

class ContactList:
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

contact1 = Contact("John Brown", "brown@onet.pl", "555234000")
contact2 = Contact("Anna May", "am@o2.pl", "232000199")
contact3 = Contact("George Small", "smallg@google.pl", "222999100")
contact4 = Contact("Paola Big", "bigpaola@poczta.pl", "100200300")

contact_list = ContactList()

contact_list.add(contact1)
contact_list.add(contact2)
contact_list.add(contact3)
contact_list.add(contact4)
contact_list.display_contacts()