def greet_user(name):
    # Normalize the input
    name = name.title()

    # Conditional logic with only plain strings
    if name == "Alice":
        print("Hello Alice, nice to see you again!")
    elif name == "Bob":
        print("Hey Bob, welcome back!")
    else:
        print("Hi there, welcome!")

# Example call
greet_user("alice")
