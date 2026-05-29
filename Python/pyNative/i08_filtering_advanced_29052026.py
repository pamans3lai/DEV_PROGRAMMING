words = ["apple", "education", "ice", "ocean", "python", "umbrella"]

vokal_panjang = [
        w for w in words
        if len(w) > 5 and w[0].lower() in 'aiueo'
        ]

print(f"ori: {words}")
print(f"filter: {vokal_panjang}")
