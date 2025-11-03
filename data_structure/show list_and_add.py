fruits = ["apple", "banana"]

def add_and_show(fruit):
    fruits.append(fruit)
    print("Updated fruit list:")
    for item in fruits:
        print("-", item)

add_and_show("orange")

# This code adds a new fruit to a list and displays all fruits
