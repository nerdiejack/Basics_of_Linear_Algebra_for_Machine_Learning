# create tensor
from numpy import array
from numpy import tensordot
A = array([
    [[1, 2, 3],    [4, 5, 6],    [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]]
])

B = array([
    [[1, 2, 3],    [4, 5, 6],    [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]]
])

C = A / B
print(C)

C = array([1, 2, 3])
D = array([3, 4, 5])
E = tensordot(C, D, axes=0)
print(E)
