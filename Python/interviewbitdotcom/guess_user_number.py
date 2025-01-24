import random

def guess(num):
    low = 1
    high = num
    feedback = ''
    while feedback != 'b':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        # guess = random.randint(low, high)
        feedback = input(f"is it {guess}? Apakah itu terlalu rendah (R), terlalu tinggi (T), atau itu benar (B)?").lower()
        if feedback == 'r':
            low = guess + 1
        elif feedback == 't':
            high = guess - 1
    print(f"Saya dapat! Itu {guess}")

    guess(1000)
