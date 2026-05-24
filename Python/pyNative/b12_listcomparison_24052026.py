def awal_akhir_sama(number_list):
    print("daftar yang diberikan:", number_list)

    num_awal = number_list[0]
    num_akhir = number_list[-1]

    if num_awal == num_akhir:
        return True
    else:
        return False

nomor_x = [10, 20, 30, 40, 10]
print("hasilnya adalah", awal_akhir_sama(nomor_x))

nomor_y = [75, 65, 35, 75, 30]
print("hasilnya adalah", awal_akhir_sama(nomor_y))