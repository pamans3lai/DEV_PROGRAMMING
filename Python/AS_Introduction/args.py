def add(a, b, *args):
    total = a + b
    for n in args:
        total += n
    return total


print(add(1, 2, 3, 4, 5))
