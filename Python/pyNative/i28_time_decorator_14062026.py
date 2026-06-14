import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"Fungsi '{func.__name__}' memerlukan {duration:.4f} detik.")
        return result
    return wrapper

@timer
def waste_time():
    time.sleep(15)

waste_time()

