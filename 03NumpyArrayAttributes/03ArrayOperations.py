#Array operations me 2 type ke operations hote hai Scalar And Vector

import numpy as np
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

#Scalar operation : Isme hum ek single numpy array ke upar ek scalar se operate krte hai. scalar means a single nnumber

#i) Arithmetic
'''print(a1)
a1=a1*2
print(a1)
a1=a1**2
print(a1)'''

#ii) Relational (<,>,<=,>=,==,!=)
'''print(a2)
# a2 = a2 > 5 #if number is greater than 5 print true otherwise false
# print(a2)
a2 = a2 == 15
print(a2)'''

#Vector operation : jab koi 2 numpy arrays ke upar koi operator apply krte ho jaise -->

#Arithmetic
print(a1)
print(a2)
a1 = a1+a2 #we can also use -,*,/,//,**
print(a1)