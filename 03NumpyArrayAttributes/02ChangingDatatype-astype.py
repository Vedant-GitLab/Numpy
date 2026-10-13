import numpy as np
a3=np.arange(8).reshape(2,2,2) #simple 3D array : tensor
print(a3)
print("------------------------------------------------------------")
print(a3.dtype)
print("------------------------------------------------------------")
print("Actually 64 is a very large bit if we have to store small data then we have to change it to small bit like 32 bit for example if we have to store the age of any person then the maximumm age will be 100 so why we use 64 bit for this type conditions we use astype attribute to decrese the size")
print("------------------------------------------------------------")
a3 = a3.astype(np.int32)
print(a3.dtype)