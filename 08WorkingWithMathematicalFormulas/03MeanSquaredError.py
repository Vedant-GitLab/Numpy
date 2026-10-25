#Mean square error : jb hum koi output predict krte hai lekin uska actual output kuch aur aata hai tb hum is situation ko MSE kehte hai. Aur predicted aur actual ke beech ke differnce ke square ko ERROR kehte hai. Aur fir MSE ki value nikalne ke liye total number of inputs se divide krte hai. formula : MSE = (actual - predicted)**2/n

import numpy as np
actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)
print(actual)
print(predicted)

def mse(actual, predicted):
    return np.mean((actual-predicted)**2 )
print(mse(actual,predicted))