import csv


def proses_gaji(input_file, output_file):
    gaji = []
    baris = []

    # baca data
    with open(input_file, mode="r", newline="") as f:
        reader = csv.Dictreader(f)
        for row in reader:
            gaji.append(int(row["Gaji"]))
            rows.append(row)

    gaji_rerata = sum(gaji) / len(gaji)

    # tulis data
    fieldnames - ["Nama", "Gaji"]
    with open(output_file, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writer()
        writer.writerows()
        writer.writerow({"Nama": "Rerata", "Gaji": gaji_rerata})
