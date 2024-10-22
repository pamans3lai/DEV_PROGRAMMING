msg = input('input message: ')
def SMS_shortener(msg):
    while len(msg) > 160:
        try:
            lst = msg.split(" ")
            lst.append(lst.pop(-2) + lst.pop().title())
            msg = " ".join(lst)
        except IndexError:
            print("Text can not be shortened.")
    return msg

print(msg)
