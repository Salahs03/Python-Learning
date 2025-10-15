class Person:
    def __init__(self, name):
        self.name = name  # attribute

    def greet(self):
        print(f"Hello, my name is {self.name}!")

# create objects
person1 = Person("Alice")
person2 = Person("Bob")

person1.greet()
person2.greet()
