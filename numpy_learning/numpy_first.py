'''
numpy -> python library,used for working with arrays, short form of numerical python

NumPy aims to provide an array object that is 50x faster than the traditional python lists

the array object in pnumpy is called 'ndarray'

why ndarray are faster than lists?
beacuse ndarrays are stored at one continuous place in memory unlike lists,so processes can access and manipulate them very efficiently.
'''

# after installation of numpy importing numpy
import numpy as np

arr=np.array([1,2,3,4,5])
nums=np.array({1,2,4,5})
print(type(arr)) #<class 'numpy.ndarray'>
print(type(nums)) #<class 'numpy.ndarray'>

print(np.__version__)

