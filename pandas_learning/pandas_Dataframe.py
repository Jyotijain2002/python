import pandas as pd

'''
DataFrame:
it is a 2-d data structure,like a 2d array or table with rows and columns
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

'''
if we want a particular row from the dataframe then we can use "loc" attribute, which is used to locate a row
'''

print(my_dataframe.loc[0])
'''
output: this is a Series
start chennai
end   ahemdabad
fare  1500
'''

# return row 0 and 1
print(my_dataframe.loc[[0,1]])
'''
output: when using [], the result will be a dataframe
      start         end  fare
0   chennai   ahemdabad  1500
1    mumbai     lucknow  2000
'''

# named indexs
'''
with the help of "index" argument , we an name the labels/indexs by our own
'''
my_dataframe2=pd.DataFrame(my_table,index=['row1','row2','row3','row4','row5'])
print(my_dataframe2)
'''
output:
         start         end  fare
row1   chennai   ahemdabad  1500
row2    mumbai     lucknow  2000
row3  banglore  chandigarh  1700
row4     delhi        agra   800
row5    jaipur     udaipur   500
'''
# locate named indexs
print(my_dataframe2.loc["row1"])
'''
output:
start      chennai
end      ahemdabad
fare          1500
Name: row1, dtype: object
'''

'''load files into a dataframe'''
df=pd.read_csv('data.csv')
print(df)
print(type(df)) #<class 'pandas.core.frame.DataFrame'>
'''
output:
         name  age education
0  jyoti jain   22     btech
1        asha   21        ba
2       dipti   20      bcom
3       navya   23       msc
'''