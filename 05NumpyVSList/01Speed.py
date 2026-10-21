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

#numpy
import numpy as np
c = np.arange(10000000)
d = np.arange(10000000,20000000)
start = time.time()
c = c+d
print(time.time()-start) #0.1346883773803711

print(1.5120859146118164/0.1346883773803711) #11.22655082807599

#here it is shown the numpy is 11.22 times faster than list, but it is not accurate its just a calculated time on the basis of compiler speed