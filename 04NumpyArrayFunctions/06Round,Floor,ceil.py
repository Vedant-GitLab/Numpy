import numpy as np
a = np.round(np.random.random((2,3))*100)  #round function is used to round-off the value into nearest integer (like float into integer value)
print(a)

print("-----------------------------------------------------------------------------")

b = np.floor(np.random.random((2,3))*100)  #floor function is used to get the previous integer value (like if we have "5.7" so then with the help of floor we get "5")
print(b)

print("-----------------------------------------------------------------------------")


c = np.ceil(np.random.random((2,3))*100)  #ceil function is used to get the next integer value (like if we have "5.7" so then with the help of ceil we get "6")
print(c)