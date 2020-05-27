from Product import *
from Refrigerator import *
from Phone import *


class Product_list:
    def __init__(self, file_name, phone_file, ref_file):
        self.Prod_list = []
        if file_name != "empty":
            with open(file_name, "r") as csv_file:
                csv_file.readline()
                for r in csv_file:
                    listing = r.rstrip().split(",")
                    self.Prod_list.append(Product(listing[1], listing[2], listing[3], listing[4], listing[0]))

        if ref_file != "empty":
            with open(ref_file, "r") as csv_file:
                csv_file.readline()
                for r in csv_file:
                    listing = r.rstrip().split(",")
                    self.Prod_list.append(Refrigerator(
                        listing[1], listing[2], listing[3], listing[4], listing[0], listing[5], listing[6]))

        if phone_file != "empty":
            with open(phone_file, "r") as csv_file:
                csv_file.readline()
                for r in csv_file:
                    listing = r.rstrip().split(",")
                    self.Prod_list.append(Phone(
                        listing[1], listing[2], listing[3], listing[4], listing[0], listing[5], listing[6]))

    def __str__(self):
        self.make_list()
        return ""

    # __str__ should return a string but I cant iterate my list with 1 string....
    # this method not the best looking one but it works

    def make_list(self):
        print_list = []
        for i in self.Prod_list:
            print_list.append(i)
        for i in print_list:
            print(i)

    def is_in_list(self, p: Product):
        b = False
        # __eq__ is overwritten in class Product (by name)
        if p in self.Prod_list:
            b = True
            print("Item exists in the list")
        else:
            print("Item is not in the list")
        return b

    def add_product(self, p: Product):
        if p.quantity != 0:
            # __eq__ is overwritten in Product(by name)
            if p not in self.Prod_list:
                self.Prod_list.append(p)
                print("Item was added")
            else:
                print("Item exists in the list")
        else:
            print("Quantity of the item is zero")

    def make_sell(self, name):
        made_sale = False
        for i in self.Prod_list:
            if i.name == name:
                made_sale = True
                print("Item was sold")
                # print(i)
                i.quantity -= 1
                #  print(i)
                return made_sale
        else:
            print("Item not found")

    def find_phone_in_list(self, min_size=float(0), max_size=float(10)):
        list_of_objects = []
        print("The phones are: ")
        for i in self.Prod_list:
            if isinstance(i, Phone):
                if float(min_size) <= float(i.screen_size) <= float(max_size):
                    print(i)
                    list_of_objects.append(i)
        return list_of_objects

    def count_product(self, item_name):
        print("The amount is :")
        q = 0
        for i in self.Prod_list:
            if isinstance(i, item_name):
                q += int(i.quantity)
        print(q)
        return q

    def find_an_item_by_name(self, item_name):
        for i in self.Prod_list:
            if i.name == item_name:
                print(i)
                return i

    def count_all(self):
        count = 0
        for x in self.Prod_list:
            count += int(x.quantity)
        return count


def main():
    #   p1 = Product("Key", 10, 100, "Samsung", 1)
    #   p2 = Phone("Iphone8", 123, 3500, "apple", 99, 4.2, "apple")
    #   p3 = Phone("8", 123, 3500, "a", 99, 4.2, "a")
    ProdFile = "proudact.csv"
    ref_file = "refrigerator.csv"
    phone_file = "phone.csv"
    pl = Product_list(ProdFile, phone_file, ref_file)
    print(pl)
    pl.find_phone_in_list(6, 7)
    pl.count_product(Phone)
    pl.count_all()

# pl.find_an_item_by_name("Ipad3")
#   pl.is_in_list(p1)
#   pl.is_in_list(p2)
#   pl.add_product(p1)
#   pl.is_in_list(p1)
#   pl.make_sell("Iphone8")
#   pl.make_sell("Iphone8")
#   pl.add_product(p1)
#   pl.add_product(p3)
