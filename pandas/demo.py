import pandas as pd

data_file= '/home/samidha/Downloads/f1.csv'
colnames = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','kk']
df= pd.read_csv(data_file, \
    names=colnames, header=None)
# print(df)
# print(df.index.unique())
# check data type
# print(df.dtypes)
print(df.dtypes.value_counts())
#-----------------------------------------

#Shape (row,col)
# print(df.shape)     #(row, col)
# print(df.shape[0])  # rows
# print(df.shape[1])  #col

# print(df.size)      #(row*col)

# print(df.ndim)      #dimensions
# print(df['bb'].ndim)   # dimension of a perticular col
#-----------------------------------------
df=df.set_index('aa')
# print(df)
# print(df.loc[[9]])          # label 9
print(df.iloc[9])         # index 9 means 9+1=10th 
print(df.loc[19:26, 'aa':'dd'])
print(df.iloc[18:26,0:3])
# v= df.loc()


# col= 
# df= furniture[furniture.make.isin(col)].copy()
# print(df)
# df= pd.DataFrame(furniture, columns=['aa','bb','cc','dd','ee','ff','gg','hh','ii','kk'])
# print(df)

#changing the data type of column
# furniture.Nunavut=furniture.Nunavut.astype(float)

#create frequency distribution

# print(furniture['Nunavut'].value_counts(ascending=True))
