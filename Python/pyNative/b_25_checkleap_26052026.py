def is_leap(year):
    # standard leap year logic
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
is_leap(2024)
is_leap(2026)
is_leap(2100)
