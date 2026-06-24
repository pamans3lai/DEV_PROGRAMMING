import secrets
import string


def generate_password(length):
    if length < 4:
        return "terlalu pendek"

    # definisikan karakter pool
    pool = string.ascii_letters + string.digits + string.punctuation

    # generate password using secrets for cryptographic security
    password = "".join(secrets.choice(pool) for _ in range(length))
    return password


print(f"Kata Sandi aman: {generate_password(17)}")
