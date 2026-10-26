import numpy as np
a = np.random.randint(1,100,15)
print(a)
print(np.sort(a))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
b = np.random.randint(1,100,24).reshape(6,4)
print(b)
print(np.sort(b))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
c = np.random.randint(1,100,8).reshape(2,2,2)
print(c)
print(np.sort(c))

