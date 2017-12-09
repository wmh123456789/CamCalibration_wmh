import numpy as np

a = ["1","2","3","4"]
b = [4,5,6]
cc = 'abcd'

c = []
c.append(b)
c.append([float(a[1]),float(a[2]),float(a[3])])
x = np.array(c)
print x*10
print x.ndim
print len(c)
