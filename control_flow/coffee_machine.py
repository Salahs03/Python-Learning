class CoffeeMachine:
    def start(self):
        self._heat_water()   # heat the water
        self._brew_coffee()  # brew the coffee
        print("Coffee is ready!")  # final message

    def _heat_water(self):
        print("Heating water...")

    def _brew_coffee(self):
        print("Brewing coffee...")

# create a CoffeeMachine object and start it
machine = CoffeeMachine()
machine.start()

