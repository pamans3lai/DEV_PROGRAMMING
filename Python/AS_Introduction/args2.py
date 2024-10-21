def add(*args):
    total = 0
    for n in args:
        total += n
    return total

small_numbers = [1, 2, 3]
large_numbers = [9999999,1111111]

print(add(*small_numbers))
print(add(*large_numbers))
