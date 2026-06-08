def temukan_duplikat(nums):
    terlihat = set()
    duplikat = set()

    for x in nums:
        if x in terlihat:
            duplikat.add(x)
        else:
            terlihat.add(x)

    return duplikat

nomor = [1, 2, 2, 3, 4, 5, 1, 6, 4]
print(f"duplikat ditemukan: {temukan_duplikat(nomor)}")