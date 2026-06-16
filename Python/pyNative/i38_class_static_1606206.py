class Pizza:
    def __init__(self, name, toppings):
        self.name = name
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls("Margherita", ["cheese", "tomato"])

    @staticmethod
    def validate_topping(topping):
        prohibited = ["plastic", "metal"]
        return topping not in prohibited

#penggunaan

order = Pizza.margherita()
print(f"Pizza ordered: {order.name}")
print(f"Is mushroom valid? {Pizza.validate_topping('mushroom')}")
