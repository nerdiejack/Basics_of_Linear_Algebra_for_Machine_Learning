from numpy import array
# define array
# a = array([1, 2, 3])
# print(a)
# define scalar
# b = 2
# print(b)
# broadcast
# c = a + b
# print(c)

# broadcast scalar to two-dimensional array
# A = array([[1, 2, 3],
#           [1, 2, 3]])
# define scalar
# b = 2
# print(b)
# C = A + b
# print(C)

# broadcast one-dimensional array to two-dimensional array
# A = array([[1, 2, 3],
#           [1, 2, 3]])
# print(A)
# b = array([1, 2, 3])
# print(b)
# C = A + b
# print(C)

# broadcasting error
A = array([[1, 2, 3],
          [1, 2, 3]])
print(A.shape)
b = array([1, 2])
print(b.shape)
C = A + b
print(C)
