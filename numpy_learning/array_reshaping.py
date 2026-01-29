import numpy as np

'''
numpy array reshaping:
means changing the shape of an array.
the shape of the array is the number of elements in each dimension.

by reshaping we can add or remove dimensions or change the number of elements in each dimension

'''
# reshape from 1D to 2D

arr=np.array([1,2,3,4,5,6])
print(f'arr without reshaping: {arr}')

new_arr=arr.reshape(2,3)
print(f'new_arr after reshaping the arr: {new_arr}') # op: [[1,2,3],[4,5,6]]

'''
reshaping ans array does not give us a copy of original array, it gives us views
beacuse 
new_arr.base #= None
so any changes made into new_arr will reflect in original arr
'''
print(new_arr.base) #[1,2,3,4,5,6]

new_arr[0,1]=99
print(f'new_arr: {new_arr}') #op: [[99,2,3],[4,5,6]]
print(f'original arr: {arr}') #op: [99,2,3,4,5,6]


# reshaping from 1D to 3D
new_arr1=arr.reshape(1,3,2)
print(f'new_arr1: {new_arr1}') # op: [[[99,2],[3,4],[5,6]]]



'''
can we reshape numpy array into any shape:
=> Yes, as long as the elements required for reshaping are equal in both shapes.

We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.
'''

'''
Unknown dimension:
you are allowed to have one 'unknown' dimension.
meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

pass -1 as the value ans numpy will calculate this number for you
'''

arr1=np.array([1,2,3,4,5,6,7,8])
new_arr_arr1=arr1.reshape(2,2,-1)
print(new_arr_arr1) # [[[1,2][3,4]] [[5,6][7,8]]]


'''
flattening the arrays: means converting a multidimensional array into a 1D array
for that we can use 'reshape(-1)'
'''

m_arr=np.array([[1,2,3],[3,4,5],[6,7,8]])
print(f"without flattening the m_arr: {m_arr}")

m_arr_flat=m_arr.reshape(-1)
print(f"without flattening the m_arr: {m_arr_flat}") #op: [1 2 3 3 4 5 6 7 8]
