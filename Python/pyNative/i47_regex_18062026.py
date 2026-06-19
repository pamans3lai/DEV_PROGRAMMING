import re

text = "hubungi kami di support@company.com atau sales.dept@office.org untuk bantuan"

# regex pola untuk email standar
pola_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# emails = re.findall(pola_email, text)
print(f"email ketemu: {re.findall(pola_email, text)}")

# print(f"email ketemu: {emails}")
