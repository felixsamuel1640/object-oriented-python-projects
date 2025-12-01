so I did this myself:
from abc import ABC, abstractmethod
class Product(ABC):

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    @abstractmethod
    def get_final_price(self):
        pass

class PhysicalProduct(Product):
    def __init__(self, name, price, category, shipping_cost, weight):
        super().__init__(name, price, category)
        self.shipping_cost = shipping_cost
        self.weight = weight

    def get_final_price(self):
        return f"Shipping Cost: N{self.shipping_cost:,.0f}, Weight: 
{self.weight}, Total: N{self.price + self.shipping_cost:,}"

class DigitalProduct(Product):
    def __init__(self, name, price, category, file_size, license_key):
        super().__init__(name, price, category)
        self.file_size = file_size
        self.license_key = license_key

    def get_final_price(self):
        return  f"Final price for {self.name} is N{self.price:,}"

class SubscriptionProduct(Product):
    def __init__(self, name, price, category, duration, discount):
        super().__init__(name, price, category)
        self.duration = duration
        self.discount = discount

    def get_final_price(self):
        discount = self.price * self.discount / 100
        return f"Price: N{self.price} Discount: N{discount}, Total: 
N{self.price - discount:,.0f}"

if __name__ == "__main__":
    product1 = PhysicalProduct("Wireless Mouse", 16000, "Gadgets",
                               2500, 1.2)
    product2 = DigitalProduct("Photo Editing Software", 12000,
                              "software", "1.GB",
                              "ZXCV-9988-LKJH")
    product3 = SubscriptionProduct("Music Streaming Platform", 4500, 
"Subscription",
                                   3, 10)

    products = [
        product1,
        product2,
        product3
    ]

    for pro in products:
        print(pro.get_final_price())

