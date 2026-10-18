#in slicing we can fetch multiple items at a time
import numpy as np
a1 = np.arange(10)  #1D 
a2 = np.arange(12).reshape(3,4)  #2D
a3 = np.arange(8).reshape(2,2,2)  #3D

print(a1)
#print number in 1D array
#print 234
print(a1[2:5])