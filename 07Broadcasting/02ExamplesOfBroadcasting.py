import numpy as np

#same shape
print("same")
a=np.arange(6).reshape(2,3)
b=np.arange(6,12).reshape(2,3)
print(a)
print(b)

print(a+b)

print("-------------------------------------------------------------------------")
#different shape
print("Different")
a=np.arange(6).reshape(2,3)
b=np.arange(3).reshape(1,3)
print(a)
print(b)

print(a+b)

#both are performing arithmetic operations and both have different shapes still they performs with the help of broadcasting.