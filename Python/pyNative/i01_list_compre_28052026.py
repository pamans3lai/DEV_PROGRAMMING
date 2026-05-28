words = ["appple", "bat", "cherry", "dog", "elderberry"]

# 1 baris transformasi dan filtering

filtered_words = [w.upper() for w in words if len(w) >= 4]

print(f"original: {words}")
print(f"hasil: {filtered_words}")

