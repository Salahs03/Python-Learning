class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"  # Dog’s unique sound

class Cat(Animal):
    def speak(self):
        return "Meow!"  # Cat’s unique sound

# create objects and print their sounds
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
