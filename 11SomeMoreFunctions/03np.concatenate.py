#numpy.concatenate() function concatenate a sequence of arrays along an existing axis.
import numpy as np
a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)
#we can use concatenate on the place of stacking because it ca also done as vertical and horizontal.
# print(a)
# print(b)
ans1 = np.concatenate((a,b), axis=0) #axis=0 row by row concatenate krne ke liye use hota hai. agar axix 1 ya 0 kuch bhi na rkhe to bhi row by row hi hoga.
print(ans1) 

ans2 = np.concatenate((a,b), axis=1) #axis=1 column by column concatenate krne ke liye use hota hai.
print(ans2) 
