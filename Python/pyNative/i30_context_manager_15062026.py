class DatabaseConnection:
    def __enter__(self):
        print("Menghubungkan ke database..")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Menutup jaringan secara aman..")
        return False

try:
    with DatabaseConnection() as db:
        print("Memproses data..")
        raise Exception("ada yg keliru")

except Exception as e:
    print(f"Error: {e}")
