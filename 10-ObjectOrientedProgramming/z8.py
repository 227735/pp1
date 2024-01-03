class Phone():
    def __init__(self, numer_telefonu):
        self.numer_telefonu = numer_telefonu
        self.rozmowa_trwa = False
        self.poziom_baterii = 100

    def dzwon(self, numer):
        print(f"Dzwonię pod numer {numer}...")
        self.rozmowa_trwa = True

    def odbierz(self):
        if self.rozmowa_trwa:
            print(f"Odbieram połączenie od {self.numer_telefonu}")
        else:
            print("Brak połączenia przychodzącego.")

    def sprawdz_baterie(self):
        print(f"Poziom baterii: {self.poziom_baterii}%")
        
myPhone = Phone(numer_telefonu="123-456-7890")
print("Początkowy stan:")
myPhone.sprawdz_baterie()
myPhone.dzwon("987-654-3210")
myPhone.odbierz()
myPhone.sprawdz_baterie()