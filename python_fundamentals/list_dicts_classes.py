# A very simple class
class Dog:
    def __init__(self, name):
        self.name = name

# A dictionary with some info about a dog
dog_info = {"age": 3}

# A list that holds dog objects
dogs = [Dog("Rex")]

# Print out the dog's name and age
print(dogs[0].name)      # Rex
print(dog_info["age"])   # 3
