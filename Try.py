import numpy as np
from itertools import combinations, permutations

a = ["1","2","3","4"]
b = np.array([4,5,6])
c = np.array([1,2,3])
cc = 'abcd'

print np.array(b)+np.array(c)
print np.dot(b[:2],c[:2])

print list(permutations([1, 2, 3], 2))
# print list(combinations([1, 2, 3], 2))
# print permutations([1, 2, 3], 2)
# print combinations([1, 2, 3], 2)
l = list(combinations([1,2,3,4],2))
for a,b in combinations([1,2,3,4],2):
    print a,b


# c = []
# c.append(b)
# c.append([float(a[1]),float(a[2]),float(a[3])])
# x = np.array(c)
# print x*10
# print x.ndim
# print len(c)
