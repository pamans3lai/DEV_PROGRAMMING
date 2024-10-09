import pandas as pd

df1 = pd.DataFrame({"A": [1, 2, None], "B": [4, 5, 6]})
df2 = pd.DataFrame({"A": [None, 2, 3], "B": [4, None, 6]})

def take_smaller(a1, a2):
    return a1 if a1.sum() <a2.sum() else a2

combined = df1.combine(df2, take_smaller)

print(combined)