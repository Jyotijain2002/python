import pandas as pd

# correlation: relationship
df=pd.read_csv('data1.csv')
print(df.corr())
'''
output:
          Duration     Pulse  Maxpulse  Calories
Duration  1.000000 -0.155408  0.009403  0.922717
Pulse    -0.155408  1.000000  0.786535  0.025121
Maxpulse  0.009403  0.786535  1.000000  0.203813
Calories  0.922717  0.025121  0.203813  1.000000


it gives us a matrix in which, it shows the correlation/relationship between a column to itself and with other columns.

corr() method calculates the relationship between each column in your data set.

output explained:
The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

The number varies from -1 to 1.
 
1 means 1:1 relationship ( if a value went up in first column, the other one went up as well)

0.9 is also a good relationship: more probability if one went up then the other will also probably

-0.9: if one went up then the other will went down probably

0.2 means NOT a good relationship, meaning that if one goes up that does not mean that the other will.


what is a good correlation:
It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.

perfect correlation: each column have a perfect relationship with  itself. when corr result is 1.00

good correlation: "Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.

bad correlation: "Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.
'''

