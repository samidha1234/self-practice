import pandas as pd
import numpy as np

dates = pd.date_range('1/1/2000', periods=8)

df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
# print(df['A'])
# interchange column values
df[['B', 'A']] = df[['A', 'B']]
print(df)
#correct way to swap column values
df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy()   

