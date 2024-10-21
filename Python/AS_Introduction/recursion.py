def countdown(n):
    print(n, end=' ')
    if n == 0:
        return             # Terminates recursion
    else:
        countdown(n - 1)   # Recursive call


countdown(0)
