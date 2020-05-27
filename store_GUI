from tkinter import *
from Store import *
from tkinter import messagebox
from tkinter.ttk import *

# Start of UI code
window = Tk()
window.title("Store Data")
window.geometry("500x350")

# Objects generator code for GUI
cusFile = "custmer.csv"
ProdFile = "proudact.csv"
PhoneFile = "phone.csv"
RefrigeratorFile = "refrigerator.csv"
s1 = Store(cusFile, ProdFile, PhoneFile, RefrigeratorFile)
c = Coupon("PERCENTAGE", 4, 1, "New Year")
ross = s1.cus_list.find_cus("12")
ross.add_Coupon(c)


# cus1 = s1.cus_list.find_cus("11")
# cus1.add_Coupon(c)


# Functions of buttons
def clicked_sale():
    x = txt_sale.get()
    y = x.split()
    if s1.is_cus_in_list(y[0]) and s1.is_prod_in_list(y[1]):
        s1.make_sale(y[0], y[1])
        a = s1.find_price_of_item(y[1])
        total_string = y[0] + " " + y[1] + " " + str(a)
        messagebox.showinfo("Sale Function", total_string)
    else:
        messagebox.showinfo("Sale Function", "Fail to make sale")


def clicked_find():
    x = txt_find.get().split()
    y1 = x[0]
    y2 = x[1]
    list1 = s1.prod_list.find_phone_in_list(y1, y2)
    list_for_msg = ". \n".join(str(x) for x in list1)
    if len(list_for_msg) == 0:
        messagebox.showinfo("Find function", "Empty")
    else:
        messagebox.showinfo("Count Function", list_for_msg)


def clicked_count():
    x = select.get()
    if x == 1:
        y = s1.prod_list.count_product(Phone)
        messagebox.showinfo("Count Function", y)
    elif x == 2:
        s1.prod_list.count_product(Refrigerator)
        messagebox.showinfo("Count Function")
    elif x == 3:
        y = s1.prod_list.count_all()
        messagebox.showinfo("Count Function", str(y))
    elif x not in (1, 2, 3):
        messagebox.showerror("Count Function Error")


def clicked_total():
    x = s1.profit()
    messagebox.showinfo("Total_Sum Function", str(x))


# Buttons
make_sale = Button(window, text="Make sale", command=clicked_sale)
find_phone = Button(window, text="Find phone by size", command=clicked_find)
count_products = Button(window, text="Count number of products", command=clicked_count)
get_total = Button(window, text="Get total", command=clicked_total)

# Radio Buttons
select = IntVar()
rad_phone = Radiobutton(window, text="Phones", value=1, variable=select)
rad_refrig = Radiobutton(window, text="Refrigerators", value=2, variable=select)
rad_all = Radiobutton(window, text="All", value=3, variable=select)

# Buttons grids
make_sale.grid(row=0, column=10)
find_phone.grid(row=1, column=10)
count_products.grid(row=2, column=10)
get_total.grid(row=3, column=10)
rad_all.grid(row=2, column=9)
rad_phone.grid(row=2, column=2)
rad_refrig.grid(row=2, column=3)

# Entries
txt_sale = Entry(window, width=20)
txt_find = Entry(window, width=20)
txt_sale.focus()

# Entries grids
txt_sale.grid(row=0, column=3)
txt_find.grid(row=1, column=3)

window.mainloop()
# End of UI code
print("GUI Terminated")
