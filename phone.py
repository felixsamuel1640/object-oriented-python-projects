class Phone:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def call(self):
        print(f"Calling from {self.brand} {self.model}")


phone1 = Phone("One Plus", 15)
phone2 = Phone("iPhone", 17)

phone1.call()
phone2.call()

