# menulis sebuah file
#
favorite_things = ["gajah", "singa", "liger"]

file = open("favorites.txt", "w") # membukan file dalam mode menulis

for thing in favorite_things:
    file.write(thing + "\n") # menulis seteiap thing ke file

file.close() # menutup file

# Membaca file

file = open("favorites.txt", "r") # membuka file dalam read mode

for line in file:
    print(line.strip()) # print setiap line dari file, menyingkirkan extra gbaris

file.close() # menutup file
