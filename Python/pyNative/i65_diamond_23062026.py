def berlian(n):
    # sebagian atas (growth)
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

    # sebagian bawah (shrink)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


berlian(4)
