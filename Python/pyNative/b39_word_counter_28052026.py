try:
    with open("notes.txt", "r") as file:
        data = file.read()
        words = data.split()
        word_count = len(words)
        print(f"File mengandung {word_count} kata.")

except FileNotFoundError:
    print("Error: File 'xxx.txt' tidak ditemukan.") 

