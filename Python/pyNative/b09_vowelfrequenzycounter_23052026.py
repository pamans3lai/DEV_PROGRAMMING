vowels = "aeiou"
kalimat = "belajar Coding sangat menyenangkan!"
cacah = 0

# konsersi ke lowercase untuk menghandel "A" dan 'a' secara sama

for char in kalimat.lower():
    if char in vowels:
        cacah += 1

print(f"Jumlah vokal: {cacah}")
