import numpy as np

'''numpy searching arrays:
where() method: using this method we can search for a certain value and return the indexes that get a  first match
'''

arr=np.array([1,2,3,4,5,6,7,8])
ind=np.where(arr==5) # 4
print(ind) # 4

ind =np.where(arr%2==0) # [2,4,6,8]
print(ind)

'''
"searchsorted()" method: numpy helper method that performs the binary search on numpy array and returns the index where the specified value would be inserted to maintain the search order.

the "searchsorted()" method is assumed to be used on sorted arrays 

in "searchsorted method by default left most index is returned, but we can give 
side='right' to return the right most instead
'''

index=np.searchsorted(arr,5)
print(index) # op: 4

index=np.searchsorted(arr,7,side='right') # 7
print(index)

'''
we can also search for multi values in an array using searchsorted() method by passing a list of values 
'''

indexs=np.searchsorted(arr,[1,5,7,9]) # [0,4,6,8]
print(indexs)