number = 7536

while number > 0:
    # ambil nomor terakhir
    digit = number % 10

    # hilangkan digit terakhir dari number
    number = number // 10

    print(digit, end=" ")