import pandas as pd

'''
data cleaning: refers to fixing bad data
that bad data can be:
1. empty cells
2. data in wrong format
3. wrong data
4. duplicates


so in data_cleaning.csv these are the bad data:

1. The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).

2.The data set contains wrong format ("Date" in row 26).

3. The data set contains wrong data ("Duration" in row 7).

4. The data set contains duplicates (row 11 and 12).
'''


'''
empty cells: can potentially give us wrong result when we analyze data.

there are following ways to handle empty cells:

1. remove cells with empty cells:
   for this we use method
   "dropna()"
   this method return new dataframe, and will not change the original.

   if we want to change original dataframe, then use "inplace=true" argument. by using inplace argument , this method will not return a new dataframe and will remove all rows containing null values.

2. replace empty values:
   instead removing the rows with null values, we can fill those empty cells using method:
   "fillna()"

   this method relace all the empty cells with a specified value, and it also gives a new dataframe but you can use argument "inplace=true" for making changes in the original dataframe

   2.1. replace only for specified columns:
        to only replace empty values for one column, specify the column name for the dataframe
        eg: df.fillna({'calories':130},inplace=true)
    
   2.2. replace using mean , median,or mode
        pandas uses the mean(), median() and mode() methods to calculate the respective values for a specified column

        eg:
        x=df['calories'].mean()
        df.fillna({'calories':x},inplace=true)


        *mean=average of all the values in trhat column
        *median=middle value in that column after sorting the in     values that column
        *mode=thae value that appears frequently 

        NaN: not a number, used for showing that data is undefined/missing
        
'''

# deleting the empty cell rows

df=pd.read_csv('data_cleaning.csv')
print(df)
print()

new_df=df.dropna()
print('newdf:')
print(new_df.to_string())
print('df:')
print(df)

df.dropna(inplace=True)
print("after using inplace argument df")
print(df)


# replacing the mepty cell values:

# fillna() method
df1=pd.read_csv('data_cleaning.csv')
df1.fillna('filled',inplace=True)
print('after filling all the empty cells with "filled"')
print(df1)

df2=pd.read_csv('data_cleaning.csv')
#filling a specified column
df2.fillna({'Calories':544},inplace=True)
print('after filling colories column with ')
print(df2)

# filling empty cells with mean/median/mode

df3=pd.read_csv('data_cleaning.csv')
x=df['Calories'].mean()
df3.fillna({'Calories':x},inplace=True)
print('after filling Calories column with mode value for that coulmn')
print(df3)