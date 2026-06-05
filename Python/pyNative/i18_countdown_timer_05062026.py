from datetime import datetime

def hitung_mundur_ke_tahun_baru():
    sekarang = datetime.now()

    tahun_depan = sekarang.year + 1
    target = datetime(tahun_depan, 1, 1)

    diff = target - sekarang

    jumlah_hari = diff.days
    jam, remainder = divmod(diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return f"{jumlah_hari} hari, {jam}, hours, {minutes} minutes"

print(f"waktu tersisa: {hitung_mundur_ke_tahun_baru()} hingga Tahun Baru")