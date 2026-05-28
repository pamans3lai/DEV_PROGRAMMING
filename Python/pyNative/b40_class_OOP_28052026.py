class Car:
    def __init__(self, make, model, year):
        # setting up attibutes
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        # metode untuk menggunakan atibut objek
        print(f"{self.year} {self.make} {self.model} sedang dinyalakan")

# membuat objek (contoh Class)
my_car = Car("Toyota", "Camry", 2022)

# memanggil metode
my_car.start_engine()

