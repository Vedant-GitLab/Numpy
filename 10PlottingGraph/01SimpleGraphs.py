#plotting is a technique to make a graph. In which we use matplot library. (hum iske baare me baad me pdhenge)
#2D graphs : 

import numpy as np
x = np.linspace(-10,10,100) #here we just take 100 random numbers from -10 to 10

#it is same like x (its a graph of straight line at 45' from x to y)
# y = x 

#its a graph of parabola
# y = x**2 

#its a graph like a wave called sinewave
# y = np.sin(x) #isi tarike se hum cos, tan, exponent, etc ka bhi nikal skte hai
# y = np.exp(x) #exponent

#it is a graph of smooth, continuous curve
y = x*np.log(x)



import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show() #is used to show or execute the graph (like print)