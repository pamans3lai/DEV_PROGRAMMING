import os


def find_txt_files(start_dir):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".txt"):
                # gabung jalur follder dan nama file secara benar
                full_path = os.path.join(root, file)
                print(f"Ditemukan: {full_path}")


# penggunaan
find_txt_files(".")
