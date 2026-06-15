class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def fuel_type(self):
        return "Bensin"

class Elektrik(Vehicle):
    def fuel_type(self):
        return "MobLIs"

#usage

moblis = Elektrik("BYD")
print(f"Merk: {moblis.brand}")
print(f"Minum: {moblis.fuel_type()}")
