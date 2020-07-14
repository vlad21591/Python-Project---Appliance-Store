from Product_List import *
from Customer_List import *
from Sale import *


class Store:
    def __init__(self, cus_file_name, prod_file="empty", phone_file="empty", refregerator_file="empty"):
        self.cus_list = Customer_List(cus_file_name)
        self.prod_list = Product_list(prod_file, phone_file, refregerator_file)
        self.sales_list = []

    def make_sale(self, cus_id, prod_name):

        relevant_costumer = self.cus_list.find_cus(cus_id)
        relevant_prod = self.prod_list.find_an_item_by_name(prod_name)

        best_normal_discount_for_prod = int(0)
        best_percentage_discount_for_prod = int(0)

        for coupon in relevant_costumer.coupon_list:
            if coupon.pr_id == relevant_prod.id and coupon.type == "SIMPLE_DIS":
                best_normal_discount_for_prod = coupon.discount

        for coupon in relevant_costumer.coupon_list:
            if coupon.pr_id == relevant_prod.id and coupon.type == "PERCENTAGE":
                best_percentage_discount_for_prod = (coupon.discount / 100)

        best_price_with_normal_dis = (int(relevant_prod.price) - int(best_normal_discount_for_prod))
        if best_normal_discount_for_prod < 0:
            best_normal_discount_for_prod == 0

        best_price_with_percentage_dis = int(relevant_prod.price) * int(best_percentage_discount_for_prod)

        if best_price_with_percentage_dis > best_price_with_normal_dis:
            self.sales_list.append(Sale(cus_id, relevant_prod.id, best_price_with_percentage_dis))
        else:
            self.sales_list.append(Sale(cus_id, relevant_prod.id, best_price_with_normal_dis))

    def find_phone_by_size(self, min_size=0, max_size=10):
        self.prod_list.find_phone_in_list(min_size, max_size)

    def show_sales(self):
        count = 0
        for i in self.sales_list:
            print("Sale number {} :".format(count))
            print(i)
            count += 1
        # The sales are appending to the list by the order they are made so the list is already sorted for this
        # if not, we can sort the list by sale.date and then show it

    def profit(self):
        p = 0
        for i in self.sales_list:
            p += int(i.price)
        print("The profit from all the sale is ", p)
        return p

    def count_product(self, item_name):
        self.prod_list.count_product(item_name)

    def find_price_of_item(self, item_name):
        price = 0
        for p in self.prod_list.Prod_list:
            if p.name == item_name:
                price += int(p.price)
        return price

    def is_cus_in_list(self, id):
        x = self.cus_list.find_cus(id)
        if x is None:
            return False
        elif x.id == id:
            return True

    def is_prod_in_list(self, prod_name):
        x = self.prod_list.find_an_item_by_name(prod_name)
        if x is None:
            return False
        elif x.name == prod_name:
            return True


def main():
    cusFile = "custmer.csv"
    ProdFile = "proudact.csv"
    PhoneFile = "phone.csv"
    RefrigeratorFile = "refrigerator.csv"
    s1 = Store(cusFile, ProdFile, PhoneFile, RefrigeratorFile)
    c = Coupon("PERCENTAGE", 4, 1, "New Year")
    ross = s1.cus_list.find_cus("12")
    ross.add_Coupon(c)
    print(s1.cus_list)
    print(s1.prod_list
    s1.make_sale("12", "note8")
    s1.profit()
    s1.find_price_of_item("note8")
    s1.is_cus_in_list("12")
    s1.find_phone_by_size(6, 7)
    s1.count_product(Phone)



