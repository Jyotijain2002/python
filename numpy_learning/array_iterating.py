import numpy as np


'''
iterating a numpy array:
1) using for loop
'''
arr=np.array([1,2,3,4,5,6,7,8])

for i in arr:
    print(i,end=" ")
print()

print(len(arr))

for ind in range(0,len(arr)):
    print(arr[ind], end=" ")
print()

arr1=[[1,2,3],[4,5,6],[7,8,9]]
for i in arr1:
    for el in i:
        print(el, end=" ")

print()

arr2=[[[1,2,3],[4,5,6],[7,8,9]]]
for i in arr2:
    for j in i:
        for k in j:
            print(k, end=" ")


'''
another method for array iteration:
using method 'nditer()'

number for loops is directly proportional to the dimensionlity of the array
which can be difficult to write for arrays with very high dimensionlity
'''

print()
nums=np.array([1,2,3,4,5,6,7,8,9])
nums1=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(f'dimensionality of nums1: {nums1.ndim}')

for x in np.nditer(nums1):
    print(x,end=" ")

print()

num3=np.array([1,2,True,"hello",7.8])
for x in np.nditer(num3):
    print(x, end=" ")

print()

print(num3.dtype) # U32

'''
iterating array with different datatypes:

'op_dtypes': we can use this argument and pass it the expected datatypes to change the datatypes of the elements while iterating

NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called 'buffer', and in order to enable it in nditer() we pass flags=['buffered'].

Note : we can change a datatype small to large one but vice versa is not true
'''


for x in np.nditer(nums,flags=['buffered'],op_dtypes=['S']):
    print(x, end=" ")

print()

# iterating with different step size

for x in np.nditer(arr[::2]):
    print(x,end=" ") # op: [1,3,5,7]

print()

'''
enumerated iteration using 'ndenumerate()' method:
enumeration means mentioning sequence number of something one by one
like in array sometimes we need index of the element wile iterating so ndenumerate() method can be used for that
'''

for index,element in np.ndenumerate(arr):
    print(index,element)