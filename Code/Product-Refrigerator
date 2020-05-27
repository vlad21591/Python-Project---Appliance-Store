from Product import *


class Refrigerator(Product):

    def __init__(self, name="", quantity=10, price=100, manufacturer="", id="", number_of_doors=2, size=500):
        super().__init__(name, quantity, price, manufacturer, id)
        self.number_of_doors = number_of_doors
        self.size = size

    def __str__(self):
        return "Refrigerator: of size  {}, quantity = {}, price = {}, id = {} ".format(
            self.size, self.quantity, self.price, self.id)


def main():
    r1 = Refrigerator("Jamson", 1, 2, "LG", "1", 3, 2)
    print(r1)



