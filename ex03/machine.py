from beverages import HotBeverage


class CoffeeMachine:
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup? Gimme my money back!"

    def __init__(self):
        self.counter = 0
        self.broken = False

    def repair(self):
        self.counter = 0
        self.broken = False

    def serve(self, beverage_type):
        if self.broken:
            raise CoffeeMachine.BrokenMachineException()

        if not issubclass(beverage_type, HotBeverage):
            raise TypeError("Invalid beverage type")

        from random import randint
        self.counter += 1

        if self.counter >= 10:
            self.broken = True

        if randint(0, 1):
            return beverage_type()
        else:
            return CoffeeMachine.EmptyCup()

from beverages import Coffee, Tea, Chocolate, Cappuccino
from machine import CoffeeMachine

def main():
    machine = CoffeeMachine()

    drinks = [Coffee, Tea, Chocolate, Cappuccino]

    for i in range(15):
        try:
            drink = machine.serve(drinks[i % len(drinks)])
            print(drink)
        except CoffeeMachine.BrokenMachineException as e:
            print(f"Machine cassée ! {e}")
            print("Réparation...")
            machine.repair()

if __name__ == "__main__":
    main()
