from Customer import *
from Product import *


class Sale:
    def __init__(self, customer_id=0, product_id=0, price=0.0, date=""):
        self.customer_id = customer_id
        self.product_id = product_id
        self.price = price
        self.date = date

    def __str__(self):
        return "customer_id: {}. product_id: {}. price: {:,.2f}. date: {}".format(
            self.customer_id, self.product_id, self.price, self.date)


def main():
    c1 = Customer(["207633439", "Israel", "Hamsa", "Male", "Final Space", "055-555-1555"])
    p1 = Product("Track", 1, 10000, "Ford")
    sale1 = Sale(c1.id, p1.id, p1.price, "31/03/2020")
    print(sale1)


