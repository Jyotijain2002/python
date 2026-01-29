import numpy as np

'''
splitting is the reverse operation of joing

"array_split()" method is used for splitting arrays, in this method we pass the array we want to split and the number of splits
'''
arr=np.array([1,2,3,4,5,6,7,8])

new_arr=np.split(arr,4)
print(new_arr) # [[1 2] [3 4] [5 6] [7 8]]
print(new_arr[0]) # [1,2]


# if the array has less elements than required, it will adjust from the end accordingly
new_arr1=np.array_split(arr,5)
print(new_arr1) # op: [[1,2],[3,4],[5,6],[7],[8]]

'''
new_arr1=np.split(arr,5)
print(new_arr1)
use split() method in this case will give us error because arr have 8 element and we have to devide it in 5 equal divison array which we can not do 

so 'split()' function do not adjust the elements when elements are less in source array for splitting like 'array_split()' method
'''

# splitting 2D array:
arr=np.array([[1,2],[3,4],[5,6],[7,8]])
new_arr=np.array_split(arr,2)
print(new_arr)
'''
op:
[[[1,2],[3,4]],[[5,6],[7,8]]]


similarly we can splitting any multidimensional array
'''
'''
another types of numpy array splits:
horizontal split: 'hsplit() method'
vertical split: 'vsplit() method'
depth/height split: 'dsplit() method'
'''

