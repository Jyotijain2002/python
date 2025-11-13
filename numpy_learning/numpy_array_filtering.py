import numpy as np

'''
filtering: getting some elements out of an existing array and creating a new array out of them is called filtering

in numpy you filter an array using boolean index list.

a boolean indexlist is a list of booleans corresponding to indexes in the array.

if the value at an index is True that element is contained in the filtered array and if the value is false then that element is excluded from the filtered array
'''

arr=np.array([11,42,63,74,85])

x=[True,False,False,True,True]

filtered_arr=arr[x]
print(filtered_arr) # [11,74,85]



# creating filter array: create a filter array that will return only values higher than 42

def filter_value(arr):
    filter_arr=[]
    for x in arr:
        if(x>42):
            filter_arr.append(True)
        else:
            filter_arr.append(False)
    return filter_arr

filter_arr=filter_value(arr)
print(arr[filter_arr]) #[63 74 85]
print(filter_arr) #[False, False, True, True, True]

filter_x=[]
for x in arr:
    if(x%2==0):
        filter_x.append(True)
    else:
        filter_x.append(False)
print(filter_x)
print(arr[filter_x])


# creating filter directly from array:

arr=np.array([41,42,43,44])
filter_arr=arr>42
print(filter_arr) # [False False  True  True]
print(arr[filter_arr]) # [43,44]
