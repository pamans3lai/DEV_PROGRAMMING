def adalah_anagram(str1, str2):
    # bersihkan dan urutkan kedua  string
    s1 = sorted(str1.lower().replace(" ", ""))
    s2 = sorted(str2.lower().replace(" ", ""))

    # jika sorted list identik, itu adalah_anagram
    return s1 == s2 

w1, w2 = "listen", "silent"
result = adalah_anagram(w1, w2)

print(f'apakah "{w1}" adalah anagram dari "{w2}"? {result}')

