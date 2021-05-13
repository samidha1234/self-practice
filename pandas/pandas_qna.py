import pandas as pd 

# print(pd.__version__)

import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# print(pd.Series(mylist))
# print(pd.Series(myarr))
# print(pd.Series(mydict))

set1 = pd.Series(mydict)
set1.name= 'first_alpha_ser'
# print(set1)

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
#items of series A not present in series B
# print(ser2[~ser2.isin(ser1)])

#items not common to both series A and series B
ser_u=pd.Series(np.union1d(ser1,ser2))
ser_i=pd.Series(np.intersect1d(ser1,ser2))
# print(ser_u)
# print("-------------------")
# print(ser_i)

# print(ser_u[~ser_u.isin(ser_i)])

#get the minimum, median, 75th, and max of a numeric series
ser = pd.Series(np.random.normal(10, 5, 25))
# print(ser)
# print(ser.min())
# print(ser.max())
# print(ser.median())

# get frequency counts of unique items of a series

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
# print(ser.value_counts())

#keep only top 2 most frequent values as it is and replace everything else as ‘Other’
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
# print(ser)
# print("----------------")
# print("Top 2 Freq:", ser.value_counts())
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
# print(ser)

#convert a numpy array to a dataframe of given shape
ser = pd.Series(np.random.randint(1, 10, 35))
df= pd.DataFrame(ser.values.reshape(7,5))
# print(df)

# find the positions of numbers that are multiples of 3 from a series
ser = pd.Series(np.random.randint(1, 10, 7))
# print(ser)
# print(np.argwhere(ser % 3==0))

#extract items at given positions from a series
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# print(ser.take(pos))

#stack two series vertically and horizontally
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
# print(ser1.append(ser2))
print(pd.concat([ser1,ser2]))l;

ser1.iloc[49:50]

#extract the row and column number of a particular cell with given criterion
