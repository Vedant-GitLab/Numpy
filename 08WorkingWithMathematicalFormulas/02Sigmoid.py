#Sigmoid : A sigmoid function is a mathematical function having a characteristic "S"-shaped curve or sigmoid curve. The logistic curve.  formula S(x) = 1 / 1+e^-x {S(x)=sigmoid of x and e=eulers number}

#ye koi built-in function nhi hai isko humein manually banana pdega

import numpy as np
def sigmoid(array):
    return 1/(1 + np.exp(array))


a=np.arange(10)
print(sigmoid(a))