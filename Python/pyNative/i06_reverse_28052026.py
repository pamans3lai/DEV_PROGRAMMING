def pembalik_katas(kalimat):
    # split kalimat menjadi kata
    katas = kalimat.split()

    # balik setiap kata menggunakan  slicing
    katas_terbalik = [kata[::-1] for kata in  katas]

    # gabung balik menjadi single string
    return " ".join(katas_terbalik)

text = "Aku Cinta IMPALA"
hasil = pembalik_katas(text)
print(f"Original: {text}")
print(f"hasil: {hasil}")
