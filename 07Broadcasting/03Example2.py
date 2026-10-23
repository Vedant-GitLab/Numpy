import numpy as np
a=np.arange(12).reshape(3,4) #2D
b=np.arange(3) #1D
print(a) 
print(b)
print(a+b) #it gives error because operands could not be broadcast together with shapes (3,4) (3,) 

'''Okay let suppose we have (3,4) and (3) acc. to rule-1 first we add 1 on the head of the array to make them same dimension and then acc. to rule-2 stretced 1 till its not equal to the head of other array (1 is stretched till 3) and then if they are not equal it gives error like here (3,4) != (1,3)'''