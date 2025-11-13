import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data1.csv')
# df.plot()
# plt.show()
'''
scatter plot: if we want a scatter plot then we can get that using the argment "kind"
eg:
df.plot(kind='type_of_graph', x='x_coordinates', y='y-coordinates')
types of kind:
scatter
hist(histogram): histogram only need one column, and it shows us the frequency of each interval.
'''

# df.plot(kind='scatter',x='Duration',y='Calories')
df['Duration'].plot(kind='hist')
plt.show()