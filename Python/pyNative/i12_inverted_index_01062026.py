def invert_biblio(data):
    inverted = {}
    for author, books in data.items():
        for book in books:
            inverted[book] = author
    return inverted

authors = {
    "Orwell": ["1984",  "Animal Farm"],
    "Huxley": ["Brave New World"]
}
print(f"Inverted Index: {invert_biblio(authors)}")