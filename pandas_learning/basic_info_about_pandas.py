'''
pandas -> used to analyze data
pandas= panel data / python data analysis

pandas-> used for working with data sets,it has functions for analyzing,cleaning,exploring and manipulating data
'''

import pandas as pd

my_data_set={
    'cars':["bmw",'volvo','ford'],
    'passings':[3,7,2]
}

my_var=pd.DataFrame(my_data_set)
print(my_var)
# output
#     cars  passings
# 0    bmw         3
# 1  volvo         7
# 2   ford         2

print()

# pandas version finding
print(pd.__version__)