# vector L1 norm
from numpy import array
from numpy.linalg import norm
from math import inf
# a = array([1, 2, 3])
# print(a)
# l1 = norm(a, 1)
# print(l1)

#vector l2 norm
# a = array([1, 2, 3])
# print(a)
# l2 = norm(a)
# print(l2)

# vector max norm
a = array([1, 2, 3])
print(a)
maxnorm = norm(a, inf)
print(maxnorm)

