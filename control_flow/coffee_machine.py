class CoffeeMachine:
    def start(self):
        self._heat_water()
        self._brew_coffee()
        print("Coffee is ready!")

    def _heat_water(self):
        print("Heating water...")

    def _brew_coffee(self):
        print("Brewing coffee...")

machine = CoffeeMachine()
machine.start()
