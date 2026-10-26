#The numpy.append() appends values along the mentioned axis at the end of the array
import numpy as np
a = np.random.randint(1,100,15)
print(a)
print(np.append(a,200))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

b = np.random.randint(1,100,24).reshape(6,4)
print(b)
print(np.append(b,np.ones((b.shape[0],1)), axis=1)) #1 appends after last column
print(np.append(b,np.random.random((b.shape[0],1)), axis=1)) #random numbers after last column