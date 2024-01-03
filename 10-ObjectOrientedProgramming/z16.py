class CellPhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = 100
        self.on = False
        self.app = None

    def info(self):
        print(f"{self.brand} {self.model} is {'On' if self.on else 'Off'}.")

    def use_app(self, app_name):
        if self.on:
            self.app = app_name
            print(f"{self.brand} {self.model} is using {app_name}.")
        else:
            print("Please turn on the phone first.")

phone1  = CellPhone("Samsung", "Galaxy S21")
phone2 = CellPhone("iPhone", "12 Pro")

phone1.info()
phone1.use_app("Messaging")

phone2.info()
phone2.use_app("Camera")