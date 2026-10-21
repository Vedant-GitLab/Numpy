#numpy is convinient than lists
a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c = []
import time

start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])
print(time.time()-start) 



#numpy
import numpy as np
c = np.arange(10000000)
d = np.arange(10000000,20000000)

start = time.time()
c = c+d
print(time.time()-start) 



#here we can see in lists we have to run the loop to add a and b but in numpy we simply add c and d, it shows numpy is easier or convinient than lists 