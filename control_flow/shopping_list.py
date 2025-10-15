def add_item(shopping_list, item):        # Function adds items if not already in list
    item = item.strip().lower()          
    if item not in shopping_list:
        shopping_list.append(item)        # Add item to the list
        return f"{item.title()} added."
    else:
        return f"{item.title()} is already on the list."

my_list = []                              # Empty list to start with
print(add_item(my_list, "Milk"))          # Call the function with arguments
print(add_item(my_list, "milk"))
print(add_item(my_list, "Bread"))
print("Final list:", my_list)


# lists + string formatting + avoiding duplicates