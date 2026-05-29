from collections import Counter

def get_frekuensi(input_string):
    # bersihkan string: hilangkan spasi dan lowercase
    clean_text = input_string.lower().replace(" ", "")

    # Counter secara otomatis membangun frekuensi map
    return Counter(clean_text)

text = "Aku Cinta Impala"
freq = get_frekuensi(text)

print(f"Original: {text}")
print(f"hasil frequensi: {freq}")


