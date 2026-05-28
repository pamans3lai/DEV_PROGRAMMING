with open("notes.txt", "w") as file:
    file.write("Hello, ini adalah catatan pertama saya.\n")
    file.write("Python file  handling is simple.\n")
    file.write("Enf of file.\n")

print("Membaca konteks:")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
