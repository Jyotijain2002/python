import pandas as pd

'''
cleaning data of wrong format:
cells with wrong format can make it difficult,or even impossible to analyze data
so, to handle this, we can do:
1. to remove that row, with wrong format
2. to convert all cells into the same format
'''

'''
# convert into a correct format:
 here in the data_cleaning.csv file the date column have wrong format in to cells
 so, to fix this we will be using "to_datatime()" method

'''
df=pd.read_csv('data_cleaning.csv')
print("formatting the date column:")
df['Date']=pd.to_datetime(df['Date'],format='mixed')
print(df)
 
'''
row 26 was fixed, but row 22 got a NaT(not a time), or in other words an empty value
so now we can use dropna() method to remove that row will NaT date cell 
'''
df.dropna(subset=['Date'],inplace=True)
print('after removing row with NaT date cell')
print(df)