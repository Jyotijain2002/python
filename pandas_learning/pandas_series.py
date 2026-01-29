import pandas as pd

'''
pandas series: is a one dimensional array holding data of any data-type like a column in a table 
'''
a=[1,2,4]
my_var=pd.Series(a)
print(my_var)
'''
op:
0  1 
1  2
2  4
'''

'''
labels:
if nothing else is specified , the values are labled with their index number,firts value has index 0, second value has index 1 etc.
this lable can be used to access a specified value
'''
print(my_var[0])


'''
creating labels:
with the index argument,we can name our own labels
'''

a=[1,7,3]
my_var=pd.Series(a,index=['xxx','yyy','zzz'])
print(my_var)

'''
op:
xxx    1
yyy    7
zzz    3
dtype: int64
'''

'''
we can also use a key/value, like dictionary, when creating a Series 
in this the key will work as labels
'''
dict1={
    "name":"jyoti jain",
    "age":22,
    "education":"Btech"
}

my_series_dict=pd.Series(dict1)

print(my_series_dict)
'''
output:
name         jyoti jain
age                  22
education         Btech
dtype: object
'''

'''
if only want to include some of the key-value pair of the dictionary into the Series than we will use "index" argument in which we specify only those keys/labels which we want to include in our Series
'''

my_dict_series=pd.Series(dict1,index=["name","education"])
print(my_dict_series)
'''output: will include only name and education
name         jyoti jain
education         Btech
dtype: object
'''


'''
DataFrame:
data sets in pandas are usually multi-dimensional tables, called DataFrames.
Series is like a column, a Dataframe is whole table
'''

my_table={
    "start":["chennai","mumbai","banglore","delhi","jaipur"],
    "end":["ahemdabad","lucknow","chandigarh","agra","udaipur"],
    "fare":[1500,2000,1700,800,500]
}
my_dataframe=pd.DataFrame(my_table)
print(my_dataframe)
'''
output:
      start         end  fare
0   chennai   ahemdabad  1500
1    mumbai     lucknow  2000
2  banglore  chandigarh  1700
3     delhi        agra   800
4    jaipur     udaipur   500
'''