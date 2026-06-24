FILE_NAME = "todo.txt"


def add_task(task):
    with open(FILE_NAME, "a") as f:
        f.write(task + "\n")


def view_task():
    try:
        with open(FILE_NAME, "r") as f:
            print("\n--- Tugas saat ini ---")
            for i, line in enumerate(f, 1):
                print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("Gak ketemu")


def clear_task():
    open(FILE_NAME, "w").close()
    print("list cleared")


add_task("Code in Python")
