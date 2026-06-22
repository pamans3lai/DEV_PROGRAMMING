def file_stats(filename):
    lines, words, chars = 0, 0, 0

    try:
        with open(filename, "r") as f:
            for line in f:
                lines += 1
                words += len(line.split())
                chars += len(line)

        print(f"Lines: {lines} | Words: {words} | Character: {chars}")
    except FileNotFoundError:
        print("The file does not exist")
