import re
from collections import Counter


def count_words(text):
    # hilangkan punctuassi dan gunakan regex dan ubah menjadi lowercase

    clean_text = re.sub(r"[^\w\s]", "", text).lower()

    # pisahkan menjadi kata dan hitung
    words = clean_text.split()
    return dict(Counter(words))


text = "Pyhton is great  Python is fast and learning Python is fun!"
print(f"word frequency: {count_words(text)}")
