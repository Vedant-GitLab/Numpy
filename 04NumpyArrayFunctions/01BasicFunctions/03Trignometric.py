#Trignometric functions are like sin, cos, tan, etc.
import numpy as np
a1=np.random.random((3,3))
a1=np.round(a1*100)
print(a1)

a1=np.sin(a1)  #calculates sin of every value in matrix
print(a1)

a1=np.cos(a1) #calculates cos of every value in matrix
print(a1)

a1=np.tan(a1) #calculates tan of every value in matrix
print(a1)