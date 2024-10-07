import pandas as pd

titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

titanic.to_csv("titanic.csv", index=False)

titanic.info()

ages = titanic["Age"]
ages.head()
