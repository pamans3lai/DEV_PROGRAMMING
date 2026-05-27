numbers  = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
genap = []
ganjil = []

for num in numbers: 
    if num % 2 == 0:
        genap.append(num)
    else:
        ganjil.append(num)

print(f"Even numbes: {genap}")
print(f"Odd nubmers: {ganjil}")
