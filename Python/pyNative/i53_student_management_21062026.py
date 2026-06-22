students = {}


def add_student(s_id, name, grade):
    students[s_id] = {"name": name, "grade": grade}


def update_grade(s_id, new_grade):
    if s_id in students:
        students[s_id]["grade"] = new_grade
    else:
        print("Student not found")


def display_student():
    for s_id, info in students.items():
        print(f"ID: {s_id} | Nama: {info['name']} | Grade: {info['grade']}")


add_student(101, "Alice", "A")
update_grade(101, "A++")
display_student()
