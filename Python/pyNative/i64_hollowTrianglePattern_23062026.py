def print_segitiga_hollow(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            # kondisi untuk 2 sisi segitiiga dan base
            if j == n - i + 1 or j == n + i + 1 - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()


print_segitiga_hollow(5)
