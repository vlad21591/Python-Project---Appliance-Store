class Coupon:
    def __init__(self, type, discount, pr_id, name, date="1/1/2020"):
        if type in ["SIMPLE_DIS", "PERCENTAGE"]:
            self.type = type
        else:
            print("Please enter a valid coupon type")
        self.discount = discount
        self.pr_id = pr_id
        self.name = name
        self.date = date

    def __str__(self):
        return "Coupon is {} type with a discount of {} for product with the id of {}. \n" \
               "The name of the coupon is {} and its date is {} ".format(
                 self.type, self.discount, self.pr_id, self.name, self.date)

    def __eq__(self, other):
        if self.name == other.name:
            return True


def main():
    c1 = Coupon("First", 100, 100, "LOL")
    c2 = Coupon("Second", 10, 10, "LOL")
    c3 = Coupon("Second", 10, 10, "LOL2")

    if c1 == c2:
        print("Equal")
    elif c1 != c2:
        print("Not Equal")

    if c2 == c3:
        print("Equal")
    elif c2 != c3:
        print("Not Equal")
