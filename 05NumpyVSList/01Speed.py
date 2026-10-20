#the speed of numpy array is faster then the speed of list, let see:
#list :
a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c = []
import time
start = time.time()

for i in range(len(a)):
    c.append(a[i] + b[i])

print(time.time()-start) #1.6746668815612793


import numpy as np
a = np.arange(10000000)
b = np.arange(10000000,20000000)
start = time.time()
c = a+b
print(time.time()-start) #0.1346883773803711

print(1.5120859146118164/0.1346883773803711)