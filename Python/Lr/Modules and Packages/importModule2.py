import calculator
# Import the `calculator` module here

calc = calculator.Calculator()
#Create a new instance of the `Calculator` class defined in the `calculator` module
for i in range(100):
    calc.add(i)# Use the Calculator method `add` to add `i` to the current value.

print(calc.get_current())
