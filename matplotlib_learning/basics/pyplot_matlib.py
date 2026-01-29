'''
matplotlib: low level graph plotting library in python that serves as a visualiztaion utility,it is open sourced 

'''
import matplotlib.pyplot as plt
import numpy as np

'''
matplotlib pyplot: most of the matplotlib utilities lies under pyplot submodule and usually imported under plt alias

matplotlib plotting:
plot() method is used to plot the graph, its argument are array like data-structure like, list,array,tuple etc
this method takes two argument first:
x-coordinates list
y-coordinates list


'''
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([0,1,1,2,3,5,8,13,21,34])
#plt.plot(x,y)
#plt.show()


'''
plotting without line:
to plot only markers, you can use shortcut string notation parameter 'o' , which mean rings

multiple points: we can plot as many as points in the graph but both axis should have same number of points
'''
#plt.plot(x,y,'o')
#plt.show()


'''default x-points:
if we don't specify the points on x-axis, they will get the default values 0,1,2,3 etc, depending upon the length of y-points list
'''

y_points=np.array([0,1,8,27,64,125,216,243,512,729,1000])
#plt.plot(y_points,'o')

#plt.show()

'''markers:
   you can use the keyword "marker" to emphasize each point with a specified marker

   AT W3SCHOOL THERE IS A LIST OF MARKERS, REFERENCE IT FROM THERE. 
'''
#plt.plot(y_points,marker='*')
#plt.show()



'''
formate strings fmt:
we can use a shortcut string notation parameter to sepecify the marker.
this parameter is called fmt, and its syntax:
      marker|line|color
'''

yP=np.array([0,3,6,9,12,15,18,21,24,27])
#plt.plot(yP,'o:g') # HERE first marker=o , then line=: means dotted, and then color=g(green)
#plt.plot(yP,'*--m') # here line= -- (dashed)
#plt.show()

'''
we can also specify the marker size using the argument "markersize or ms"
'''
#plt.plot(yP,'o c',ms=20)
#plt.show()

'''
we use "markeredgecolor/mec" argument to set the color of the edge of the markers
'''
#plt.plot(yP, marker='o',ms=15,mec='y')
#plt.show()

'''
we can also set the marker face color using argument "markerfacecolor/mfc"
'''
yp=np.array([3,1,8,10])
plt.plot(yp,marker='*',ms=20,mec='c',mfc='purple')
plt.show()

'''
we can use hexa-decimal color values
'''


'''
matplotlib line:

for changing the line style we can use 'linestyle/ls' argument
eg ls='--/ dashed' (dashed) 

for changing the line color we can use 'color/c' argument
eg c='g'

for changing the line width, we can use 'linewidth/lw' argument
eg: lw='20'
'''

'''
we can plot multiple lines in a single graph by plotting different lines in same graph
eg:
x=[1,2,3]
y=[1,23,34]
new_y=[2,4,5,78]
plt.plot(x,y)
plt.plot(new_y)
plt.show()
'''

