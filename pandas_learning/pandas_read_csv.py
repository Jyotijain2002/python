'''
read CSV file: is a simple way to store big data sets to use CSV files

csv file: contains plain text 
'''

import pandas as pd

df=pd.read_csv('data1.csv')
'''if we have a large dataframe with many rows, pandas will only return the first 5 rows and last 5 rows
'''
print(df)

'''if we want to print whole large dataframe,then use "to_string()" method'''
print(df.to_string())

'''
"maxrows": the number of rows is defined in pandas option setting.
for example if maxrows=60 then if dataframe contains more than 60 rows, the 
print(df) 
statement will return only the headers and the first and last 5 rows
we can change the maximum rows   

'''

print(pd.options.display.max_rows) # 60
#changing max_rows
pd.options.display.max_rows=999
print(df) # now it will print all the rows
print(pd.options.display.max_rows) # 999
