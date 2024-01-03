class Ebook():
    def __init__(self,title, author, number_of_pages):
        self.title = title
        self.author = author 
        self.number_of_pages = number_of_pages
        self.current_page = 0
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False
        self.current_page = 0
    
    def info(self):
        return (f"Title: {self.title}\nAuthor: {self.author}\nPage numbers: {self.number_of_pages}\nCurrent page: {self.current_page}\nIs Open: {self.is_open}")

    def read(self, pages):
        if self.is_open:
            if self.current_page + pages <= self.number_of_pages:
                self.current_page += pages
                return f"Read {pages} pages. Current page: {self.current_page}"
            else:
                return "Nie ma takiej strony."
        else:
            return "Książka jest zamknięta."

ebook1 = Ebook("Ballada Ptaków i Węży", "Suzanne Collins", 456)

ebook1.open()
print(ebook1.info())
print()
print(ebook1.read(25))
print(ebook1.info())
print()
ebook1.close()
print(ebook1.read(25))
print(ebook1.info())


