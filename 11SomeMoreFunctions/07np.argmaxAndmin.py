#The numpy.argmax() function returns indices of the max element of the array in a particular axis.
import numpy as np
a = np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a)
print(np.argmax(a))
print(a[np.argmax(a)])

print(np.argmin(a))
print(a[np.argmin(a)])