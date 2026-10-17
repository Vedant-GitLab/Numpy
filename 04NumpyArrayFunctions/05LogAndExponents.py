#use to calculate log and exponential values of elements in numpy array
import numpy as np
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

print(a2)
print(np.log(a2)) #log ke liye

print(a3) 
print(np.exp(a2)) #exponent ke liye