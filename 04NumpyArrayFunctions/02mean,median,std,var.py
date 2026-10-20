import numpy as np
a1=np.random.random((3,3))
# print(a1)
a1=np.round(a1*100)
print(a1)

print(np.mean(a1), " ---> mean") #poore matrix ka mean dega
print(np.mean(a1,axis=1), " ---> mean") #har row ka mean dega

print(np.median(a1), " ---> median") #poore matrix ko sort krke beech wala item nikal kr dega

print(np.std(a1), " ---> standard deviation") #standard deviation

print(np.var(a1), " ---> variance") #variance