class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y}"

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)


p1 = Point(1, 2)
p2 = Point(3, 4)
kombinasi = p1 + p2

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"kombinasi: {kombinasi}")
