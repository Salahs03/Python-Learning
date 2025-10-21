# Parent class
class Animal:
    def __init__(self, name, sounds):
        self.name = name
        self.sounds = sounds  # data structure (list)

    def speak(self):
        for sound in self.sounds:  # iterate over the list
            print(f"{self.name} says: {sound}")

# Child classes inherit from Animal
class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Create objects
dog = Dog("Rex", ["woof", "bark", "arf"])
cat = Cat("Luna", ["meow", "purr", "hiss"])

dog.speak()
cat.speak()
