#in indexing we can only fetch only 1 item at aa time it starts from 0 in +ve and in -ve from -1

import numpy as np
a1 = np.arange(10)  #1D 
a2 = np.arange(12).reshape(3,4)  #2D
a3 = np.arange(8).reshape(2,2,2)  #3D



#negative and positive indexing
print(a1) #print 1st digit of a1
print(a1[0])  #positive indexing = left to right
print(a1[-1]) #negative indexing = right to left

print("-------------------------------------------------------------------------------------")

#print the number in 2D array or matrix (it is a combination of 1D array)
print(a2)
#there are 3 rows (0,1,2) and 4 columns (0,1,2,3) if we have to print number "6" then first we have to check the row and then the column in which number is situated for example
print(a2[1,2]) #6  a2[row,column]
print(a2[2,3]) #11

print("-------------------------------------------------------------------------------------")


#print the number in 3D array or tensor (it is a combination of 2D array)
print(a3)
#in 3D array we have two 2D's array(0,1) so first we have to select a array and in it we have 2rows and 2columns(0,1) let suppose if we have to print 5 so first we have to select a array in which it is present, it is present in second array means in 1 and then the columns 1 and row is 0 so : 
print(a3[1,0,1]) #5
print(a3[0,0,0]) #0
print(a3[0,0,1]) #1
print(a3[1,1,0]) #6

#in same manner we can print a number of any 4D arrayy in which first we have to check 3D array then 2D array And then check its row and column