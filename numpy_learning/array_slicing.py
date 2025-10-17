import numpy as np
'''
slicing array:
slicing means taking elements from one index to another given index
like:
[start : end]
or
[start : end : step]

step: this value determine the step of the slicing

if don't pass the start , it will consider it to be 0
and if dont pass the end , it will consider it to be be end of the array
'''
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[3:7]) # 7th index will not be included
print(arr[0:9:2]) # op: [1,3,5,7,9]

print('\n')

num=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(num[0:3:2]) #op: [[1 2 3] [7 8 9]]
print(num[0][0:3:2]) #op: [1,3]
# or
print(num[0,0:3:2]) #op:[1,3]

'''
negative slicing: use minus operator to refer to an index from the end
'''
print(arr[-3:-1]) # op: [7,8]
print(arr[-1:]) # op: [9]


arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr1[0:2, 1:4]) #op: [[2,3,4] [7,8,9]]