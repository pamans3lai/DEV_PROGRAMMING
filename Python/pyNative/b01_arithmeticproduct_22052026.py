
def hasil_multiplikasi(num1, num2):
    produk = num1 * num2
    if produk <= 1000:
        return produk
    else:
        return num1 + num2 

result = hasil_multiplikasi(40, 30)
print(result)


result = hasil_multiplikasi(20, 30)
print(result)
