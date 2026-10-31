#numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis. 
#mtlb one by one numbers ko add krega simultaneously agar yeh function na hota to ye kaam hum loop ki help se krte.

import numpy as np
a = np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a)
print(np.cumsum(a)) # ((((i + i1) + i2) + i3) + i4)
print(np.cumprod(a)) # ((((i * i1) * i2) * i3) * i4)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
b = np.arange(24).reshape(6,4)
print(b)
print(np.cumsum(b)) #1D me convert krke sum krega
print(np.cumsum(b, axis=0)) #column
print(np.cumsum(b, axis=1)) #row