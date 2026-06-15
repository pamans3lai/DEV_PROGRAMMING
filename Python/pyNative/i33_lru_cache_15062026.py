from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

#kalkulasi

n = 50
print(f"Fibonacci({n}) = {fib(n)}")
print(f"cache Info: {fib.cache_info()}")
