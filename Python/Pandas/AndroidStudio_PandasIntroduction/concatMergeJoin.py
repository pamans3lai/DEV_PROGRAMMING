import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']})
df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'], 'B': ['B3', 'B4', 'B5']})

vstack = pd.concat([df1, df2], ignore_index=True)

print(vstack)

hstack = pd.concat([df1,df2], axis=1, keys=['df1','df2'])

print(hstack)

users = pd.DataFrame({'user_id': [1, 2, 3],
                      'name': ['Alice', 'Bob', 'Charlie']})

orders = pd.DataFrame({'user_id': [1, 2, 1, 3],
                       'item': ['Book', 'Pen', 'Pencil', 'Eraser'],
                       'quantity': [1, 3, 2, 1]})

merged_df = users.merge(orders, on='user_id')

print(merged_df)
