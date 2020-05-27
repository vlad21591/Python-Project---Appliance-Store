from Product import *


class Phone(Product):

    def __init__(self, name="", quantity=10, price=100, manufacturer="Apple", id="", screen_size = float, os=""):
        super().__init__(name, quantity, price, manufacturer, id)
        self.screen_size = screen_size
        self.os = os

    def __str__(self):
        return "Phone: with screen size of {}, os = {}, quantity = {}, price = {}, id = {} ".format(
            self.screen_size, self.os, self.quantity, self.price, self.id)


def main():
    p1 = Phone("iPhone", 10, 100, "Apple", 1, 5, "OS")
    print(p1)



