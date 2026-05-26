def daftar_gabungan(daftar1, daftar2):
    daftar_hasil = []

    #  ganjil
    for num in daftar1:
        if num % 2 != 0:
            daftar_hasil.append(num)
    
    #  genap
    for num in daftar2:
        if num % 2 == 0:
            daftar_hasil.append(num)

    return daftar_hasil

    daftar1 = [10, 20, 25, 30, 35]
    daftar2 = [40, 45, 60, 75, 90]
    print("daftar_hasil:", daftar_gabungan(daftar1, daftar2))