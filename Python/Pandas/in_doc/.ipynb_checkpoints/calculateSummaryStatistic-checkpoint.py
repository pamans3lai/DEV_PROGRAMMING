import pandas as pd

titanic = pd.read_csv("/home/ai/DEV_PROGRAMMING/Python/Pandas/in_doc/titanic.csv")
titanic.head()

print(titanic[["Sex", "Age"]].groupby("Sex").mean())


print(titanic[["Sex", "Age"]].groupby("Sex").mean())




print(titanic[["Sex", "Age"]].groupby("Sex").mean())

print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())
