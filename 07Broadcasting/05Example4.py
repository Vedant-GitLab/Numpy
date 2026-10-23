import numpy as np

a = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4,1)

print(a)
print(b)
print(a+b)
'''This will also happens beacuse 1 is stretched to 4 and other 1 is stretched to 3 then (1,3) = (4,1) becomes (4,3)=(4,3)'''