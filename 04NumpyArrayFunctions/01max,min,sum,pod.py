import numpy as np
a1=np.random.random((3,3))
# print(a1)
a1=np.round(a1*100)
print(a1)

print(np.max(a1)) #sbse bda item
print(np.min(a1)) #sbse chota item
print(np.sum(a1)) #sbse items ka sum
print(np.prod(a1)) #sbse items ka product 

#0->col, 1->row
print(np.max(a1, axis=1)) #har row ka sbse bda item
print(np.max(a1, axis=0)) #har col ka sbse bda item

#isi axis ko hum sbhi functions per perform kr skte hai kisi 1 row ke elements ko sum ya multiply ya fir minimum bhi nikal skte hai.