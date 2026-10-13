import numpy as np
a1=np.arange(10, dtype=np.int32)  #simple 1D array : vector
a2=np.arange(12, dtype=float).reshape(3,4) #simple 2D array : matrix
a3=np.arange(8).reshape(2,2,2) #simple 3D array : tensor

#ndim : used to check the no. of dimentions of any array, its a 1D, 2D or 3D
# print(a1.ndim)
# print(a2.ndim)
# print(a3.ndim)


#shape : It tells us how many items in one dimention
# print(a1.shape) #10 rows, 0 columns
# print(a2.shape) #3 rows, r columns


#size : it tell us the number of items
# print(a1.size)
# print(a2.size)
# print(a3.size)


#item size : it tells how much size was occupied by each item
# print(a1.itemsize) #8 bytes 
# print(a2.itemsize) #8 bytes by default 64 bit hota hai isliye 8 answer hai agar 32 kr do toh 4 hoga
# print(a3.itemsize) #8 bytes, 8 bits = 1 byte


#dtype : it tell us which type of type of data is
# print(a1.dtype)
# print(a2.dtype)
# print(a3.dtype)