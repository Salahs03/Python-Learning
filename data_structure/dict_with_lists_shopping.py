# A dictionary where each key maps to a list of items
shopping_list = {
    "fruits": ["apple", "banana", "orange"],
    "vegetables": ["carrot", "spinach", "broccoli"],
    "drinks": ["water", "juice"]
}

# Accessing items
print("Fruits:", shopping_list["fruits"])
print("First vegetable:", shopping_list["vegetables"][0])

# Adding a new item to the drinks list
shopping_list["drinks"].append("tea")

print("Updated shopping list:", shopping_list)


