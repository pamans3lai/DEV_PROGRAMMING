try:
    tepung = 2
    gula = l
    resep = tepung/gula
    print("Kamu sudha cukup bahan. kuy masak")

except ZeroDivisionError:
    print("Ooops, butuh gula lagi. Tidak bisa dibagi 0")

except Exception as e:

    print("Ooops, ada yg keliru", str(e))
