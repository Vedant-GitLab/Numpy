import numpy as np
x = np.linspace(-10,10,100) #hum isko change krke 50 tk bhi kr skte hai
y = 1/(1+np.exp(-x))


import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show() #is used to show or execute the graph (like print)