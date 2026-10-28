#With the help of Numpy.expand_dims() method, we can get the expanded dimensions of an array
#with the use of this library we can convert a 1D array into 2D array
import numpy as np
a=np.array([1,2,3,4,5,6,7])
print(a)
print(np.expand_dims(a, axis=0)) #row vector 
print(a.shape)

print(np.expand_dims(a, axis=1)) #column vector
print(a.shape)
