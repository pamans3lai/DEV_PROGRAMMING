baris = 5

# outer loop untuk baris nomor
#
for i in range(baris, 0, -1):
    # inner loop for printting numbers in each row
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
