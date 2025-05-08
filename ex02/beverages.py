class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "Hot beverage"

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"


class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "tea"
        self.price = 0.30

    def description(self):
        return "A relaxing cup of tea."


class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "chocolate"
        self.price = 0.50

    def description(self):
        return "Chocolate, sweet chocolate."


class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45

    def description(self):
        return "Un po' Italia nella sua tazza !"


def main():
    boisson = HotBeverage()
    cafe = Coffee()
    the = Tea()
    chocolat = Chocolate()
    cappuccino = Cappuccino()

    print("HotBeverage instance:")
    print(boisson)
    print("\nCoffee instance:")
    print(cafe)
    print("\nTea instance:")
    print(the)
    print("\nChocolate instance:")
    print(chocolat)
    print("\nCappuccino instance:")
    print(cappuccino)


if __name__ == "__main__":
    main()
