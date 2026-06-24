def turbo_pascal(n):
    segitiga = [[1]]

    for i in range(1, n):
        prev_row = segitiga[-1]
        # memulai segitiga dengan 1
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        # akhir baris dengan  1
        new_row.append(1)
        segitiga.append(new_row)

    return segitiga


#  penggunaan
#
for row in turbo_pascal(5):
    print(row)
