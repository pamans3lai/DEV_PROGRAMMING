import pandas as pd 

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['Saint Petersburg', 'New York', 'Prague', 'Paphos']
}

print(pd.DataFrame(data))

column_age = df['Age']

print(column_age)