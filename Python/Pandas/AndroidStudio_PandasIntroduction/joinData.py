import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 
'B': ['B0', 'B1', 'B2']},
index=['I0', 'I1', 'I2'])

df2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'], 
'D': ['D0', 'D2', 'D3']},
index=['I0', 'I2', 'I3'])

# df1_join_df2 = df1.join(df2, how='outer')

df1_join_df2 = df1.join(df2, how='inner')

print(df1_join_df2)