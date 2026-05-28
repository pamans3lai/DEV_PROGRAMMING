input_string = "Indonesia245"

contains_digit  = False

# iterate through each charcter

for char in input_string:
    if char.isdigit():
        contains_digit = True
        break

print(f"The String '{input_string} contains {contains_digit}")
