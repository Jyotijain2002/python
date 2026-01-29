import numpy as np

'''
shape of an array: is the number of elements in each dimension.

NumPy arrays have an attribute called 'shape' that returns a tuple with each index having the number of corresponding elements.
'''
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.shape) # (3,3)

arr1=np.array([1,2,3,4])
print(arr1.shape) # (4,)

arr2=np.array(23) 
print(arr2.shape) # ()

arr3=np.array([[1,2],[3,4],[5,6]])
print(arr3.shape) # (3,2) 

arr4=np.array([[[[1,2,3,4,5,6]]]])
print(arr4.shape) #(1,1,1,6)

arr5=np.array([1,2,3,4],ndmin=5)
print(arr5.shape) #(1,1,1,1,4)

'''
what does the shape tuple present?
integers at every index tells about the number of elements the corresponding dimension has

In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.
'''