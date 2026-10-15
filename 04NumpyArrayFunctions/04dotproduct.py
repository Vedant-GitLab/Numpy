import numpy as np
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)
# print(a2)
# print(a3)

#DotProduct : It is used to calculate the dot product of two matrix, And dpt product tbhi hi possible hai jb pehli matrix ke row dusre matrix ke column se equal ho.

a2 =np.dot(a2,a3)
print(a2)