# create array
from numpy import array
from numpy import empty
from numpy import zeros
from numpy import ones

# create array
l = [1.0, 2.0, 3.0]
a = array(l)
# display array
print(a)
# display array shape
print(a.shape)
# display array data type
print(a.dtype)
# create empty array
a = empty([3, 3])
print(a)
# create zero array
a = zeros([3, 5])
print(a)
# create one array
a = ones([5])
print(a)
