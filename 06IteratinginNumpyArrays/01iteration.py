import numpy as np
a1 = np.arange(10)  #1D 
a2 = np.arange(12).reshape(3,4)  #2D
a3 = np.arange(27).reshape(3,3,3)  #3D
# for i in a1:
#     print(i)  #a1 ka har item print hoga
# for i in a2:  
#     print(i)  #a2 ka har row print hoga
# for i in a3:
#     print(i)  #a3 ka har 2D array print hoga 

#print all numbers of a3
for i in np.nditer(a3):  #nditer ki help se hum abhi elements print kra skte hai qki ye pehle sbhi types ke array ko 1D me convert krta hai fir har element ko print krta hai
    print(i)