#latihan tanggal Oct 13 2024 14:28
#https://realpython.com/python-lists-tuples/

x = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", ["hh", "ii"], "j"]

print(x[0], x[2], x[4])

print(x[1])

letters = ["A", "B", "c", "d"]  # A list
letters[2] = "C"
print(letters)

huruf = ("A", "B", "c", "d")  # A tuple
#huruf[2] = "C"
print(huruf)

# method:
# .append
# .extend
# .insert
# .remove
# .pop 
# using operators and built-in functions with lists and python-lists-tuples
# concatenation
# repetition (*)
#


t = ("foo", "bar", "baz", "qux")
s1, s2, s3, s4 = t
print(s1)
print(s2)
print(s3)
print(s4)
