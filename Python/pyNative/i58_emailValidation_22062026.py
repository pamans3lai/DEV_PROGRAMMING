import re


def validasi_email(email):
    # pola: [nama] @ [domain] . [extensi]
    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    if re.search(regex, email):
        print(f"'{email}' is a valid Email")
    else:
        print(f"'{email} is a Invalid Email")


# penggunaan
#
validasi_email("pytnon@projkf.com")
validasi_email("pytnlkjalsdf_-on@projkf.com")
