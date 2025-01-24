email = input("Masukkan email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"username kamu adalah {username} & domain is {domain}")
