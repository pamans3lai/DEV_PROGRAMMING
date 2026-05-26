def check_palindrome(number):
    print("original number", number)

    original_str = str(number)
    reversed_str = original_str[::-1]

    if original_str == reversed_str:
        print("Yess, given  number is palindrome")
    else:
        print("Bukan. nomor yang diberikan bukan palindrome")

check_palindrome(121)
check_palindrome(125)
