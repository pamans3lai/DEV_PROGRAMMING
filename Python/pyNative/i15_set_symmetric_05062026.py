def dapatkan_ekslusif_id(id1, id2):
    set1 = set(id1)
    set2 = set(id2)
    return set1 ^ set2

pengunjung_januari = [10, 20, 30, 40]
pengunjung_pebruari = [30, 50, 60, 40]

ekslusif = dapatkan_ekslusif_id(pengunjung_januari, pengunjung_pebruari)
print(f"visitor ekslusif: {ekslusif}")

