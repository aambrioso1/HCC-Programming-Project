import pandas as pd

data = {'Alex': [1, 59], 'Sonya': [2, 51], 'Erika': [3, 21] }
rows = ['gender', 'age']

print(f'data: {data}')
print(rows)
df = pd.DataFrame(data, index=rows)
print(df)
# df['total'] = df.sum()
# print(df)
