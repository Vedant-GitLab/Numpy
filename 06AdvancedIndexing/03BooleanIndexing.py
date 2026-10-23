import numpy as np
a=np.random.randint(1,100,24).reshape(6,4) #this randint function is use to select random numbers (from,to,how many)
print(a)

#find all numbers greater than 50
# a=a>50
# print(a) #answer in true or false

# a=a[a>50]
# print(a)


#find even numbers
# a=a[a%2==0]
# print(a)


#find all numbers greater than 50 and are even
# a=a[(a>50) & (a%2==0)] #numpy me "&" use hota h normal python me "and", because "and" is a logical-and but "ampercent(&)" is bitwise-and we use it because we works on boolean values
# print(a)

#find all numbers greater than 50 or are even
# a=a[(a>50) | (a%2==0)] 
# print(a)

#find all the numbers which are not divisible bby 7
# a=a%7!=0
print(a[a%7!=0])