# memasukkan user input
user_input = input("enter a phrase: ")

# menghilangkan of menggunakan replace() metode dan memecah user  user input ke kata individu menggulanakn split()method
phrase = (user_input.replace('of', '')).split()

# inisiasi string kosong untuk menambahkan akronim
a = ""

# for loop untuk menambahkan acronym
for word in phrase:
    a = a + word[0].upper()

print(f'Acronym of {user_input} is {a}')
