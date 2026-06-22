def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]


primes = generate_primes(10, 50)
print(f"Prime in range: {primes}")
