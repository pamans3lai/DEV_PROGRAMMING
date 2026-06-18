class Flyer:
    def fly(self):
        print("Flying high!")


class Swimmer:
    def swim(self):
        print("Swimming fast!")


class Duck(Flyer, Swimmer):
    pass


# penggunaan

d = Duck()
d.fly()
d.swim()

print(f"MRO: {Duck.__mro__}")
