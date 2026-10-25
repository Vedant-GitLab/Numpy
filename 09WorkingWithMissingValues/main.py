#Missing Values ky hoti hai ? : Let suppose you make a form and send it to the other persons to fill it many of them doesn't fill the roll no. and g-mail so then these are the missing values

import numpy as np
a=np.array([1.,2.,3.,4.,np.nan,6.]) #nan (Not A Number) it means a missing value
print(a)

#If we have to simply check which number is missing we just use Boolean indexing
b=np.isnan(a) #it gives True to missing value
print(b)
print(a[np.isnan(a)])  #is used to give the missing value and remove others
print(a[~np.isnan(a)])  #(~)is used to just reverse the the whole situation means its just remove the missing value and give others 