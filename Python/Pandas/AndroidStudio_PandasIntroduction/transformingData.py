import pandas as pd

numbers = pd.Series([1, 3, 7, 9, 17, 23, 29])
last_digits_gb = numbers.groupby(numbers % 10)

print(numbers)
print(last_digits_gb)