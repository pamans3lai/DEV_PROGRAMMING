import math

class Circle:
    def__init__(self, radius):
        self.radius  = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)


# penggunaan
c = Circle(5)
print(f"Area dengan radius 5: {c.area:.2f}")

c.radius =10
print(f"Area dengan radius 10: {c.area:.2f}")
