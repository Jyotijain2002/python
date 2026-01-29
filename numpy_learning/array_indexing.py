import numpy as np

'''
the indexing in numpy starts from 0 to size-1
'''
num=np.array([1,2,3,4,5,0])
print(num[0])

num1=np.array([1,2,3,4,'hi'],ndmin=5)
print(num1[0][0][0][0][4])
# or
print(num1[0,0,0,0,4])

print(num[1]+num[4])

num2=np.array([[1,2,3,8]])
print(num2[0,1])


'''
negative indexing: it is used to access an array from the end
eg:
'''
arr=np.array([[1,2,3,4],[5,6,7,8],[0,1,4,9]])
print(arr[-1]) # op: [0,1,4,9]
print(arr[-1,-1]) # op: 9
print(arr[-2]) # op: [5,6,7,8]