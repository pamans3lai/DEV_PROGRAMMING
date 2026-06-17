from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)


class Square(Shape):
    def __init__(self, side):
        self.side = side**2

    def area(self):
        return self.side**2


shapes = [Circle(5), Square(4)]
for s in shapes:
    print(f"{type(s).__name__}, Area: {s.area():.2f}")
