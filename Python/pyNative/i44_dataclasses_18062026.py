from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int


# Usage
b1 = Book("1984", "George Orwell", 328)
b2 = Book("1984", "George Orwell", 328)

print(b1)
print(f"Iss b1 equal to b2? {b1 == b2}")
