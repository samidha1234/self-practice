import pandas as pd
df=pd.DataFrame({'company':['Amazon','Apple','Google','Facebook','Microsoft'],
    'CEO':['Jeff Bezos','Tim Cook','Sundar Pichai','Mark Zuckerberg','Satya Nadella'],
    'Founded':[1994,1976,1998,2004,1975]})
# print(df)
#setting index
df.index=['Third','Second','Fourth','Fifth','First']
print(df[['CEO','company']])

#slicing data frame
print(df[0:3])
print(df[1:3])

#Data selection operation
