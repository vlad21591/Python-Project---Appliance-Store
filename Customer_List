from Customer import *
from Phone import *


class Customer_List:
    def __init__(self, file_name):
        self.cstmr_lst = []
        if file_name != "empty":
            with open(file_name, "r") as csv_file:
                csv_file.readline()
                for r in csv_file:
                    listing = r.rstrip().split(",")
                    self.cstmr_lst.append(
                        Customer([listing[0], listing[1], listing[2], listing[5], listing[3], listing[4]]))
        else:
            self.cstmr_lst = []

    def __str__(self):
        return "Customer List With {} listings".format(len(self.cstmr_lst))

    def print_lst(self):
        print(self.__str__())
        for c in self.cstmr_lst:
            print(c)

    def print_names(self):
        print(self.__str__())
        for c in self.cstmr_lst:
            print(c.first_name, c.last_name)

    def add_customer(self, customer):
        b = True
        for c in self.cstmr_lst:
            if c == customer:
                b = False
        if b:
            self.cstmr_lst.append(customer)
        else:
            print("We already have a customer with that ID")

    def delete_a_customer_by_id(self, id):
        for customer in self.cstmr_lst:
            if customer.id == id:
                self.cstmr_lst.remove(customer)

    def print_customer_info_by_familiy_name(self, last_name):
        for customer in self.cstmr_lst:
            if customer.last_name == last_name:
                print(customer)

    def find_cus(self, cus_id):
        for c in self.cstmr_lst:
            if c.id == cus_id:
                print(c)
                return c

    def get_tupple_of_ID(self):
        list1 = list()
        for x in self.cstmr_lst:
            list1.append(x.id)
        a = ''.join(list1)
        print(list1)


def main():
    filename = "custmer.csv"
    lst = Customer_List(filename)
    lst.print_names()
    print(lst)
    print("------------------------------")
    lst.print_lst()
    c2 = Customer(["368496836", "Adam", "Levin", "Male", "DC", "054-564-6439"])
    print("------------------------------")
    print("Adding a new customer to the list:")
    lst.add_customer(c2)
    print("------------------------------")
    print("After adding a new customer")
    lst.print_lst()
    print("------------------------------")
    print("All customers whose last name is \"Geller\" ")
    lst.print_customer_info_by_familiy_name("Geller")
    print("------------------------------")
    print("The customer with ID 11: ")
    lst.find_cus("11")
    lst.get_tupple_of_ID()


