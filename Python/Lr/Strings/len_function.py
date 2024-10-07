phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""

index_to_slice = int(len(phrase) / 2)
first_half = phrase[:index_to_slice]
print(first_half)
