import numpy as np
#indexing
a = np.arange(12).reshape(4,3)
print(a)
print(a[0,2])

#slicing
print(a[1:3,1:3])

#There are two very interesting types of indexing are:
#1: Fancy indexing
#2: Boolean indexing