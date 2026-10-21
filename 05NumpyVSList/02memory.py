#memory:
#list:
a = [i for i in range(10000000)]

import sys #sys means system is a module in which there is a function getsizeof() is used to calculate how much memory was occupied by variable or data
print(sys.getsizeof(a))  #give in bytes  (89095160 bytes)

#numpy
import numpy as np
b = np.arange(10000000, dtype=np.int32)
print(sys.getsizeof(b))  #80000112 bytes (almost similar to list) if use dtype=np.int32 : 40000112

#here list and numpy is almost equal but if we use dtype like int32, int16, int8 then we can reduce the size and work easily with data 
#so here numpy is best because its give flexibilty to reduce the size