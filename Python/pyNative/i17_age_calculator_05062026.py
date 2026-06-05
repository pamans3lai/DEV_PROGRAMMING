from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_exact_age(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        today = datetime.now().date()

        diff = relativedelta(today, birthdate)

        return f"{diff.years} years, {diff.months} months, {diff.days} days"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

user_age = calculate_exact_age("1986-12-03")
print(f"Exact Age: {user_age}")