import numpy as np

'''
joining numpy arrays: means putting content of two or more arrays into a single array

in numpy we join arrays by axes.
concatenate() method: in this we pass the sequence of arrays which we want to join, along with the axis, if axis is not explicitly passed , it is taken as 0
'''

arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[6,7,8],[9,10,11]])

arr=np.concatenate((arr1,arr2),axis=0)
print(arr)
'''
op:
[[ 1  2  3]
 [ 4  5  6]
 [ 6  7  8]
 [ 9 10 11]]
'''

num=np.concatenate((arr1,arr2),axis=1)
print(num)
'''
op:
[[ 1  2  3  6  7  8]
 [ 4  5  6  9 10 11]]
'''


'''
joining arrays using stack functions
stacking is same as concatenation,the only difference is that stacking is done along a new axis.
stack() method: we pass a sequence of arrays that we want to join to the along with axis,if axis is not explicitly passed it is taken as 0
'''

print("\nstack() method: \n")

nums=np.stack((arr1,arr2),axis=0)
print(f"with axis 0:\n {nums}")
'''
op:
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 6  7  8]
  [ 9 10 11]]]
'''
print()

nums=np.stack((arr1,arr2),axis=1)
print(f"with axis 1:\n {nums}")
print()
'''
op:
 [[[ 1  2  3]
  [ 6  7  8]]

 [[ 4  5  6]
  [ 9 10 11]]]
'''

nums=np.stack((arr1,arr2),axis=-1)
print(f"with axis -1:\n {nums}")
print()

'''
[[[ 1  6]
  [ 2  7]
  [ 3  8]]

 [[ 4  9]
  [ 5 10]
  [ 6 11]]]

'''

# stacking along the rows:
#numpy provides a helper function: "hstack()" (h stands for horizontal) to stack along rows: in it we pass a sequence of arrays

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

arr=np.hstack((arr1,arr2))
print(arr) #op: [1 2 3 4 5 6 7 8]

# stacking along columns: using numpy helper function vstack() (v stands for vertical)

arr=np.vstack((arr1,arr2))
print(arr)
'''
op:
[[1 2 3 4]
[5 6 7 8]]
'''

# stacking along height(depth): using numpy helper function dstack() (d stands for depth)

arr=np.dstack((arr1,arr2))
print(arr)
'''
op:
[[1 5]
[2 6]
[3 7]
[4 8]]
'''