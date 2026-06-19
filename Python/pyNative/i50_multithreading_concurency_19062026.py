import threading
import time


def download_file(name, duration):
    print(f"Mulai Download: {name}")
    time.sleep(duration)
    print(f"Download selesai: {name}")


start = time.perf_counter()

# membuat threads
#
t1 = threading.Thread(target=download_file, args=("File_A", 2))
t2 = threading.Thread(target=download_file, args=("File_B", 2))

# mulai threads

t1.start()
t2.start()

# menunggu hinga keduanya  selesai sebelum memulai
t1.join()
t2.join()

end = time.perf_counter()
print(f"Total waktu dibutuhkan: {end - start:.2f} seconds")
