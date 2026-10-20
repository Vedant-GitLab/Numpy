#in slicing we can fetch multiple items at a time
import numpy as np
a1 = np.arange(10)  #1D 
a2 = np.arange(12).reshape(3,4)  #2D
a3 = np.arange(8).reshape(2,2,2)  #3D

#print number in 1D array
print(a1)
#print 234
print(a1[2:5])  #from index 2 to 5 (last index should not printed) and all concept are same as indexing 
print("----------------------------------------------------------------")



#2D array
print(a2)
#print only 1st row
print(a2[0,:])  #first row  (here we want all columns so we leave it empty)
print(a2[:,3]) #thied column (here we want all rows so we leave it empty)
#we want 5,6 and 9,10
print(a2[1:,1:3]) #row,row:column
#print 0,3 and 8,11
print(a2[::2,::3]) #took all rows and all columns with the gap of 2 and 3 respectively
#print 1,3 and 9,11
print(a2[::2, 1::2]) #(start:end:skip)-->row and (1:end:skip)-->col
#print 4 and 7
print(a2[1, ::3]) #(1:end:skip)-->row and (start:end:skip)-->col
#print 1,2,3 and 5,6,7
print(a2[:2, 1:])
print("----------------------------------------------------------------")



#3D array
a3 = np.arange(27).reshape(3,3,3)
print(a3)
#print 2nd 2D matrix
print(a3[1])
#print 1st and 3rd 2D matrix
print(a3[::2])
#print 2nd row of 1st 2D matrix
print(a3[0,1])
#print 2nd column of 2nd 2D matrix
print(a3[1, :, 1])
#print 22,23 and 25,26
print(a3[2,1:,1:])
#print 0,2 and 18,20
print(a3[::2,0,::2])