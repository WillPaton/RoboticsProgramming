"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
        if current_cart.get(item):
            current_cart[item] += 1 #Add 1 to item amount
        else:
            current_cart[item] = 1 #Add item if it doesn't exist
    return current_cart

def read_notes(notes):
    #add each item from notes to a dict with a default value of 1
    return dict.fromkeys(notes, 1)

def update_recipes(ideas, recipe_updates):
    #combine dicts, recipe_updates's values replace existing items values in ideas
    ideas.update(recipe_updates)
    return ideas

def sort_entries(cart):
    return dict(sorted(cart.items()))#sorts alphabetically

def send_to_store(cart, aisle_mapping):
    fulfillmet_cart = dict()
    for item, amount in cart.items():
        if aisle_mapping.get(item):#if store has item
            #add item to dict, amount converted to tuple
            fulfillmet_cart[item] = [amount] + aisle_mapping[item]
    #sort dict by key in reverse
    fulfillmet_cart = dict(sorted(fulfillmet_cart.items(), reverse=True))
    return fulfillmet_cart

def update_store_inventory(fulfillment_cart, store_inventory):
    for item, info in fulfillment_cart.items():
        if store_inventory.get(item):
            store_inventory[item][0] -= info[0]#update item stock
        if store_inventory[item][0] <= 0:#if out of stock
            store_inventory[item][0] = "Out of Stock"#replace amount
    return store_inventory
