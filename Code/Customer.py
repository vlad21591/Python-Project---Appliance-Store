from Coupon import *


class Customer:
    def __init__(self, details=["id", "first_name", "last_name", "gender", "address", "phone"]):
        self.id = details[0]
        self.first_name = details[1]
        self.last_name = details[2]
        self.setGender(details[3])
        self.address = details[4]
        self.phone = details[5]
        self.coupon_list = []

    def __eq__(self, other):
        if self.id == other.id:
            return True

    def setGender(self, gender):
        if gender.lower() not in ["male", "m", "female", "F"]:
            self.gender = "F"
        else:
            self.gender = gender[0].upper()

    def print_details(self):
        print("{} : {} {}, {}  from {} with phone number: {}".format(self.id, self.last_name, self.first_name,
                                                                     self.gender, self.address, self.phone))

    def __str__(self):
        return "Id: {}, First Name: {}, Last Name: {}, Address: {}, Phone: {}, Gender: {}.".format(
            self.id,
            self.first_name,
            self.last_name,
            self.address,
            self.phone,
            self.gender)

    def add_Coupon(self, c: Coupon):
        # __eq__ is overwritten in class Coupon (by name)
        if c not in self.coupon_list:
            self.coupon_list.append(c)
        else:
            print("The coupon is already registered")


def main():
    cus1 = Customer(["207633439", "Israel", "Hamsa", "Male", "Final Space", "055-555-1555"])
    cus2 = Customer(["307533934", "Chochava", "Star", "Lady", "Final Space", "054-444-1444"])
    c1 = Coupon("SIMPLE_DIS", 100, 1, "Holiday Discount")
    c2 = Coupon("SIMPLE_DIS", 200, 2, "LOL")
    c3 = Coupon("PERCENTAGE", 300, 3, "LOL")
    print(c1)
    cus1.add_Coupon(c1)
    cus1.add_Coupon(c2)
    cus1.add_Coupon(c3)
    print(cus1.coupon_list)



