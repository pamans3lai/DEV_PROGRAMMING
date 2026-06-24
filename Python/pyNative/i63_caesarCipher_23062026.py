def cipher_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if we start at  'A' or 'a'
            start = ord("A") if char.isupper() else ord("a")
            # kalkulasi posisi baru antara 0-25 range
            new_pos = (ord(char) - start + shift) % 26
            result += chr(start + new_pos)
        else:
            result += char

    return result


# penggunaan
#
encrypted = cipher_caesar("Hallo San!", 3)
print(f"encrypted: {encrypted}")
print(f"Decrypted: {cipher_caesar(encrypted, -3)}")
