products = {"milk": 2.50, "bread": 1.00, "cheese": 4.50}
discount_items = ("milk", "cheese")

def show_discounts():
    for item, price in products.items():
        if item in discount_items:
            print(item, "is on discount!")
        else:
            print(item, "is regular price.")

show_discounts()

# This code checks which products are on sale
