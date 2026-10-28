#The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.
import numpy
a = numpy.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a)

# find all indices with value greater than 50
print(numpy.where(a>50))

#replace all the value > 50 with 0
#np.where(condition,True,False)
print(numpy.where(a>50,0,a))


#replace all even numbers with 0
print(numpy.where(a%2==0,0,a))
