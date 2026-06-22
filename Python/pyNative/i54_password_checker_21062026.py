def check_password(password):
    checks = [
        len(password) >= 8,
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        any(not char.isalnum() for char in password),
    ]

    score = sum(checks)
    levels = {
        5: "sangat kuat",
        4: "kuat",
        3: "sedang",
        2: "lemah",
        1: "sangat  lemah",
        0: "invalid",
    }

    return f"Kekuatan: {score}/5 ({levels.get(score)})"


print(check_password("haha"))
