from Customer import *


class Product:
    def __init__(self, name="", quantity=0, price=0.0, manufacturer="", id=""):
        self.name = name
        self.quantity = int(quantity)
        self.price = price
        self.manufacturer = manufacturer
        self.id = id

    def __str__(self):
        return "Id:{}, Name:{}, Manufacturer:{}, Price(unit): {} , Quantity: {}.".format(
            self.id, self.name, self.manufacturer, self.price, self.quantity)

    def __eq__(self, other):
        if self.name == other.name:
            return True


def main():
    p1 = Product("Watch", 10, 100, "Apple", "1")
    print(p1)



