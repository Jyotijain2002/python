'''
viewing the data:

if want to view some spacified number of rows form the starting with header
then use
"head(specified_rows_number)" method
and if dont pass any argument to the head method then it will return firts 5 rows with header


and similarly we have 'tail()' method that rteurn the last specified_number_of_rows from the dataframe with headers
'''
import pandas as pd

df=pd.read_csv("data1.csv")
print(df.head(10)) # will print first 10 rows with headers (0-9)
print()
print(df.head()) # will print first 5 rows form start with header (0-4)
print()
print(df.tail(10)) #print rows form end (159-168)
print()
print(df.tail()) # print rows(164-168)


# info about data of dataframe: info() method
print(df.info())
'''
output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  169 non-null    int64
 1   Pulse     169 non-null    int64
 2   Maxpulse  169 non-null    int64
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None


explanation of result:
it tells us that there are 169 rows with index form 0 to 168 with 4 data columns
then info about columns, there not-null count( count when the value in that column is not null) and datatype of that column
and then about all the datatypes used in df
and the menory used
'''