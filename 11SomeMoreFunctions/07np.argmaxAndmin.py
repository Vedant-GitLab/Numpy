#The numpy.argmax() function returns indices of the max element of the array in a particular axis.
import numpy as np
a = np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a)
print(np.argmax(a)) #indexes print krega
print(a[np.argmax(a)]) #values print krega

print(np.argmin(a)) #indexes print krega
print(a[np.argmin(a)]) #values print krega
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
b = np.arange(24).reshape(6,4)
print(b)
print(np.argmax(b,axis=0)) #indexes print krega (column wise)
print(np.argmax(b,axis=1)) #indexes print krega (row wise)
