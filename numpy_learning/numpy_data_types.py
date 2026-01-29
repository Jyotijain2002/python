import numpy as np

arr=np.array(['true'])
print(arr.dtype) # output: U4 means unicode string with max_length 4

nums=np.array(['true','marshmello'])
print(nums.dtype) # op: u10 here 10 because of max_len=10

'''
datatypes in numpy and character used to represent them
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

# creating arrays with defined data types

arr1=np.array([1,2,3,4],dtype='i')
print(arr1)
print(arr1.dtype)

''''
arr2=np.array([1,2,3,4,'true'],dtype='i') 
# it will give "ValueError' because we have decide beforehand that the only values in arr2 are allowed must have datatype as integer/'i' as we have already defined the dtype as 'i'

 print(arr1)
 print(arr1.dtype)
 '''


# for i,u,f,S and U, we can define size as well

arr3=np.array(['hello','hi','world','loss'],dtype='S5')

''' here we have given dtype as S5 which means that only allowed datatype will be string and values in the array will be atmost 5 

but what if we try to insert a value with length>5 then only the string till len=5 will be added into the array 

eg when we add 'marshmello' into the array then only 'marsh' will be added into the array 
'''
print(arr3)

arr4=np.array(['hello','hi','world','loss','marshmello'],dtype='S5')
print(arr4) #op: [b'hello' b'hi' b'world' b'loss' b'marsh']


'''
how can we change the datatype of numpy array after we have alredy defined the dtype before:

using "astype()" method:
so for converting datatype this astype() function first make the copy of the array then change the datatype to a specified datatype
'''

nums1=np.array([1.0,2.3,4.8,5.0],dtype='f')
print(nums1)
print(nums1.dtype) # float32

new_nums1=nums1.astype('i')
print(new_nums1) # [1,2,3,4,5]
print(new_nums1.dtype) # int32

arr_int=np.array([-1,0,1])
arr_bool=arr_int.astype(bool)
print(arr_bool) # op: [True,False,True] , only 0 will be converted into false when datatype is converted from 'int' to 'bool'
print(arr_bool.dtype) # bool