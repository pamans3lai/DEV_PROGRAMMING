
nomor_rahasia = 7

while True:
    tebak = int(input("Tebak nomr rahasia:"))

    if tebak == nomor_rahasia:
        print("Selama! Anda benar")
        break
    else:
        print("Ulangi lagi")

    
for number in range(1, 11):
    if number == 5:
        continue 

    print(number)


