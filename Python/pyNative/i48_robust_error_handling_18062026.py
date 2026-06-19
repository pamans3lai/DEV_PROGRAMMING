def membagi_nomor(a, b):
    try:
        hasil = a / b
        print(f"Hasil: {hasil}")
    except ZeroDivisionError:
        print("Error: ga bisa dibagi 0")
    except TypeError:
        print("Error:  masukkan nomor (int atau floats).")
    except Exception as e:
        print(f"error tak terduga:  {e}")
    finally:
        print("operasi KOMPLIT")


# 2026-06-18 15:51
membagi_nomor(10, 0)
print("-" * 20)
membagi_nomor(10, "apple")
