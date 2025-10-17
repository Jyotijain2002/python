import numpy as np

# creating an array
arr=np.array([1,3,4,'True'])
print(arr)
print(type(arr)) #<class 'numpy.ndarray'>

# numpy array are similar to list but faster
# to create a numpy array we can pass a list, tuple or any array like object into the array() method, it will convert that into ndarray

# dimensions in array

#0-D array: or scalers, are the elements in an array. each value in an array is 0-D array
zero_arr=np.array(23)
print(zero_arr)

# 1-D array: most common and basic arrays,an array that have 0-D arrays as its element
one_arr=np.array([1,2,3,4])
print(one_arr)

# 2-D array: array that has 1-D array as its element or matrix
two_arr=np.array([[1,2,3],['hello','hi','bye']])
print(two_arr)

# 3-D array: has 2-D arrays as its element
three_arr=np.array([[[1,32],['true',89.89],[1+3j,'hey']]]) 
print(three_arr)


# how to check the dimensions of numpy array? -> using "ndim"" attribute

print(zero_arr.ndim) #0
print(one_arr.ndim) #1
print(two_arr.ndim) #2
print(three_arr.ndim) #3


'''
higher dimensional array: a array can have any number od dimensions,when the array is created, you can define the number of dimensions by using ndmin argument
'''
num=np.array([1,2,3,4],ndmin=5)
print(num)
print(f'number of dimensions {num.ndim}')