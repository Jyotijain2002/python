import numpy as np

'''
Array v/s View

the main difference between the copy and view is 

copy method creates a new array and if any changes made in that new array will not affect the original array , the changes will only affect the new array and vice-versa

but view does not create a new array , view does not own data and any changes made to the view will affect the original array and any changes made to the original array will affect the view
'''

arr=np.array([1,2,3,4,5,6])

copy_arr=arr.copy()
print(copy_arr.dtype)
print(f'original array: {arr}')


copy_arr[0]=90
print(f"copy_arr: {copy_arr}")
arr[0]=123456
print(f'original array: {arr}')



# view

x=arr.view()
print(f'view array: {x}')

x[0]=1234 # any change made in view, will also reflect in original array
print(f'view array: {x}')

print(f'original array: {arr}')

'''
how to check if an array owns its data ??
we know that copies owns the data while views doesn't own the data but how to check?

so for that all numpy array have an attribute "base" that give 'None' if the array owns the data
'''

print(copy_arr.base) # op: None
print(x.base) # op: [1234    2    3    4    5    6]