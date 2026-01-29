import pandas as pd
'''
wrong data is not as same as empty cell or data with wrong format

sometimes, you can spot wrong data by looking at data set, beacuse you have an expectation of what it should be.

if we see in our data_cleaning.csv file row 7, the duration cell for that row have 450 value, while for other cells in that column reanges from 30 to 60, so we expect it to be a wrong date beacuse we are concluding a person can not work out for 450 minutes

so how to fix this:
1. replacing values
2.removing that row

'''
# locate 7 th row and change the duration cell
df=pd.read_csv('data_cleaning.csv')
df.loc[7,'Duration']=45
print(df)

# This locating and modifying data is okay for small data sets, but it is not sutable for larger data sets.
# for that we will use loops, some conditions etc

for ind in df.index:
    if df.loc[ind,'Duration']>120:
        df.loc[ind,'Duration']=120

print(df)

# removing row:
df1=pd.read_csv('data_cleaning.csv')
for ind in df1.index:
    if(df1.loc[ind,'Duration']>120):
        df1.drop(ind,inplace=True)
print(df1.info())
