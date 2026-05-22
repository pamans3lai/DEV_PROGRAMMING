print("Cetak nomor saat ini dan sebelumnya dalam rentang 10")
nomor_sebelumnya = 0

for i in range(10):
    x_jumlah = nomor_sebelumnya + i
    print(f"Nomor saat ini {i}, nomor sebelumnya {nomor_sebelumnya}, jumlah: {x_jumlah}") 

    nomor_sebelumnya = i
