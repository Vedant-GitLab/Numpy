import numpy as np
a1 = np.arange(12)
print(a1)

#reshape : used to reshape the array
a1 = np.arange(12).reshape(3,4)
print(a1)

#transpose : use to exchange the number of rows and columns  (3,4) <=> (4,3)
# a2 = np.transpose(a2)
a1 = a1.T #its a short form tanspose
print(a1)

#ravel : use to convert any array into 1D array
a3 = np.arange(27).reshape(3,3,3)  #3D
print(a3.ravel())
a2 = np.arange(12).reshape(3,4)  #2D
a2 = a2.ravel()
print(a2)