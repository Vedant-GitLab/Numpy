import numpy as np
a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1)

print(a)
print(b)

print(a+b)

'''Here we have (1,3) and (3,1) both arrays have 1 in their sizes so both 1's are stretched till both 3's then its become (3,3)=(3,3) So it gives Output'''