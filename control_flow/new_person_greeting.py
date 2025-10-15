class Person:
    def __init__(self, name):
        self.name = name  # store the person's name

    def greet(self):
        print(f"Hello, my name is {self.name}!")  # print a greeting

# create two Person objects and call greet
person1 = Person("Alice")
person2 = Person("Bob")

person1.greet()
person2.greet()
