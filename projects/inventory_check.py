inventory = {"apple": 5, "banana": 0, "orange": 3}
needed = ["apple", "banana", "grape"]

def check_inventory():
    for item in needed:
        if item in inventory and inventory[item] > 0:
            print(item, "is available")
        else:
            print(item, "is missing or out of stock")

check_inventory()

# This code checks inventory items in a dictionary against a list of needed items
