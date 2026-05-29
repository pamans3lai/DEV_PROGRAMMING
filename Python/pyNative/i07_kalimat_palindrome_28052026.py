def apakah_kalimat_palindrome(kalimat):
    # filter tanda bacadan spasi konversi ke lowercase
    karakter_bersih = [kar.lower() for kar in kalimat if kar.isalnum()]

    # join ke dalam string
    str_bersih = "".join(karakter_bersih)

    # bandingkan dengan kebalikannya
    return  str_bersih == karakter_bersih[::-1]

test_s = "A man,  a plan, a canal: Panama"

print(f"is palindrome? {apakah_kalimat_palindrome(test_s)}")
print(f"karakter_bersih: {karakter_bersih}")
print(f"str_bersih: {str_bersih}")

