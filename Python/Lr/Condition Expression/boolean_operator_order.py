name = "John"
age = 17

print(name == "John" or not age > 17)

print(name == "John" and not age == 17)

print((name == "John" or name == "Jane") and 25 > age >= 16)

                       
# Boolean operators are not evaluated from left to right. There's an order of operations for boolean operators: not is evaluated first, and is evaluated next, and or is evaluated last.
# For more structured and detailed information, you can refer to this Hyperskill knowledge base page .
# Task
# Write an expression that evaluates to True if name is either "John" or "Jane" who are 16 or older, but younger than 25.
#  Hint  