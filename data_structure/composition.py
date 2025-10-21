# Engine class
class Engine:
    def start(self):
        print("Engine starts")

# Car class uses Engine and a list of passengers
class Car:
    def __init__(self):
        self.engine = Engine()
        self.passengers = []  # data structure (list)

    def add_passenger(self, name):
        self.passengers.append(name)

    def drive(self):
        self.engine.start()
        if self.passengers:
            print("Passengers:", ", ".join(self.passengers))
        else:
            print("No passengers in the car")

# Create car and add passengers
car = Car()
car.add_passenger("Alice")
car.add_passenger("Bob")
car.drive()
