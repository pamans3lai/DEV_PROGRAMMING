import random


def play_game():
    target = random.randint(1, 100)
    attempts = 10

    print("nomor antara 1 dan 100")

    while attempts > 0:
        try:
            guess = int(input(f"({attempts} left) Enter guess: "))

        except ValueError:
            print("invalid. masukkan angka!")
            continue

        if guess == target:
            print(f"Benar! number {target}")
            return
        elif guess < target:
            print("Lebih Tinggi")
        else:
            print("lower")

        attempts -= 1

    print(f"Game over. number adalah {target}")
