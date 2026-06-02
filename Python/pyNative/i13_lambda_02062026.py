karyawan = [
    {"nama": "Alia", "gaji": 50000},
    {"nama": "Budi", "gaji": 7000},
    {"nama": "Cec", "gaji": 60000},
]

staff_singkat = sorted(karyawan, key=lambda x: x['gaji'], reverse=True)

for emp in staff_singkat:
    print(emp)