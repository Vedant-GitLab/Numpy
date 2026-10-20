#splittiong functions are used to divide a array into given equal parts. And it is reverse of stacking (h=v,v=h)
import numpy as np
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

#HORIZONTAL SPLITTING
print(a1)
a1=np.hsplit(a1,2) #(array, parts)
print(a1)

#VERTICAL SPLITTING
print(a2)
a2=np.vsplit(a2,3) #(array, parts), isko humlog even parts me divide nhi kr skte qki isme odd rows hai
print(a2)