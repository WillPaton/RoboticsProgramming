import os
import inspect
import tkinter as tk
from tkinter import *
from tkinter import ttk

def QuitButtonPressed():
    main_window.quit()

def ViewCartButtonPressed():
    DisplayCartWindow()

def AddItemsButtonPressed():
    global cart
    items_to_add = {}
    for i in range(len(products)):
        if entry_fields[i].get() != "":
            try:
                amount_added = int(entry_fields[i].get())
                items_to_add.update({products[i].name : amount_added})
            except ValueError:
                print(f"Error, expected int value in entry {i}")
        entry_fields[i].delete(0, END)#Clear entry field
    cart = AddItems(cart, items_to_add)

def AddItems(current_cart, items_to_add):
    for item, amount in items_to_add.items():
        if current_cart.get(item):
            current_cart[item] += amount#If item in cart, add amount to cart
        else:
            current_cart.update({item : amount})#If item not in cart, add it with amount
    return current_cart

def DisplayCartWindow():
    cart_window = Tk()
    cart_window.title("Cart")
    cart_window.geometry(f"{main_window_width}x{len(cart) * 30}")#got lazy with sizing
    cart_window.columnconfigure(0, minsize=main_window_width // 2)
    cart_window.columnconfigure(1, minsize=main_window_width // 2)

    product_labels = []
    amount_labels = []
    for item, amount in cart.items():
        item_label = tk.Label(cart_window, text=item)
        amount_label = tk.Label(cart_window, text=amount)
        item_label.grid(column=0, row=len(product_labels))
        amount_label.grid(column=1, row=len(amount_labels))
        product_labels.append(item_label)
        amount_labels.append(amount_label)
        
def CreateImage(image_file):
    local_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    new_image = PhotoImage(file = (local_dir + f"\\{image_file}"))
    return new_image
    
class ShopProduct:
    name = ""
    image = None
    amount = 0
    
    def __init__(self, name, image_file, amount):
        self.name = name
        self.image = CreateImage(image_file)
        self.amount = amount
        

main_window = Tk()

#Products
products = []
products.append(ShopProduct("Apple", "apple.png", 0))
products.append(ShopProduct("Banana", "banana.png", 0))
products.append(ShopProduct("Orange", "orange.png", 0))
products.append(ShopProduct("Carrot", "carrot.png", 0))
products.append(ShopProduct("Pineapple", "pineapple.png", 0))
products.append(ShopProduct("Cabbage", "cabbage.png", 0))

#Cart
cart = dict()

#Grid cells for products
column_count = 3
row_count = len(products)

#Window
main_window_height = int(main_window.winfo_screenheight() * 0.50)# height = 50% of screen height
main_window_width = int(main_window_height * 0.6)# width = 85% of window height
main_window.title("Shop Products")
main_window.geometry(f"{main_window_width}x{main_window_height}")
main_window.columnconfigure(0, minsize=main_window_width // column_count)
main_window.columnconfigure(2, minsize=main_window_width // column_count)

#Define product images, labels and entry fields on grid
image_labels = []
product_labels = []
entry_fields = []

for i in range(len(products)):
    image_labels.append((tk.Label(image = products[i].image)))
    product_labels.append(tk.Label(text = products[i].name))
    entry_fields.append(tk.Entry())
    image_labels[i].grid(
        column = 0, 
        row = i,
        padx = (main_window_width * 0.05, 0), 
        pady = main_window_height * 0.01
        )
    product_labels[i].grid(column = 1, row = i)
    entry_fields[i].grid(column=2, row=i, sticky=W)

#Quit, reset, confirm buttons
quit_button = tk.Button(text="Quit", command=QuitButtonPressed)
view_cart_button = tk.Button(text="View Cart", command=ViewCartButtonPressed)
add_items_button = tk.Button(text="Add Items", command=AddItemsButtonPressed)

quit_button.grid(column=0, row=(len(products) + 1))
view_cart_button.grid(column=1, row=(len(products) + 1))
add_items_button.grid(column=2, row=(len(products) + 1))

main_window.mainloop()