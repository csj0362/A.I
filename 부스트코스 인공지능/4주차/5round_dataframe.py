import pandas as pd

idx = ['Sue', 'Ryan', 'Jay', 'Jane', 'Anna']
col = ['round_1', 'round_2', 'round_3', 'round_4', 'round_5']
data = [[55, 65, 68, 66, 57],
        [64, 77, 71, 79, 67],
        [88, 81, 79, 89, 77],
        [45, 35, 38, 46, 47],
        [91, 96, 98, 97, 99]]

df = pd.DataFrame(data, index=idx, columns=col)

col_round_6 = pd.Series([11, 15, 13, 17, 19], index=idx)
df['round_6'] = col_round_6
print(df)

print(df.describe().loc[['mean', 'max', 'min']])