def validasi_hubungan(daftar1, daftar2):
    a = set(daftar1)
    b = set(daftar2)

    if a.issubset(b):
        print("Set A is a subset of set B")
    elif a.issuperset(b):
        print("Set B is a subset of set A")
    
    if a.isdisjoint(b):
        print("the set are disjoint, they share no elements ")
    else:
        print("the set share these elements: {a & b} ")

validasi_hubungan([1, 2], [1, 2, 3, 4])