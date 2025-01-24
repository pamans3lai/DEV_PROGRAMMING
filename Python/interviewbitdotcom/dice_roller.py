# importing random Module
import random

# initializing an while loop to keep the program executing

while True:
    print("Rolling Dice...")

    # menggunakan random.randint(1,6) untuk menggenerate nilai acak antara 1 & 6
    print(f"The value is ", random.randint(1,6))

    # meminta user untuk main lagi atau udahan
    repeat = input("Main lagi 'y' for yes & 'n' for no: ")

    # jika user menjawab tidak, loop akan berhenti dan program berehenti
    if repeat == 'n':
        break
