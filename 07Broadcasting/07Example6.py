import numpy as np
a=np.arange(12).reshape(3,4)
b=np.arange(12).reshape(4,3)
print(a)
print(b)
print(a+b)
'''Not Possible Because Both arrays have same dimesions so we cant do any change and (3,4) and (4,3) are not equal so its not happens'''