import random

max_num = 30

random_number = random.randint(1, max_num)
guess = 0
while guess != random_number:
    guess = int(input(f"Tebak nomor antara 1 & {max_num}: "))
    if guess < random_number:
        print("Salah! Terlalu rendah..")
    elif guess > random_number:
        print("Salah! Terlalu tinggi..")
    print(f"Random nomor: {random_number}")
