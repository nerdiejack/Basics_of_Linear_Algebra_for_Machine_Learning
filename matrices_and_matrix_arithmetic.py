# create matrix
from numpy import array
# A = array([[1, 2, 3],
#            [4, 5, 6]])
# print(A)
# B = array([[1, 2, 3],
#            [4, 5, 6]])
# print(B)
# C = A + B
# print(C)

# A = array([[1, 2, 3],
#            [4, 5, 6]])
# print(A)
# B = array([[0.5, 0.5, 0.5],
#            [0.5, 0.5, 0.5]])
# print(B)
# C = A - B
# print(C)

# matrix Hadamard product
# A = array([[1, 2, 3],
#            [4, 5, 6]])
# print(A)
# B = array([[1, 2, 3],
#            [4, 5, 6]])
# print(B)
# C = A * B
# print(C)

# A = array([[1, 2, 3],
#            [4, 5, 6]])
# print(A)
# B = array([[1, 2, 3],
#            [4, 5, 6]])
# print(B)
# C = A / B
# print(C)


# matrix dot product
# A = array([
#     [1, 2],
#     [3, 4],
#     [5, 6]])
# print(A, "\n")
# B = array([
#     [1, 2],
#     [3, 4]
# ])
# print(B, "\n")
# C = A.dot(B)
# print(C, "\n")
# D = A @ B
# print(D, "\n")

# matrix-vector multiplication
# A = array([
#     [1, 2],
#     [3, 4],
#     [5, 6]])
# print(A, "\n")
# B = array([0.5, 0.5])
# print(B, "\n")
# C = A.dot(B)
# print(C)

# matrix-scalar multiplication
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
b = 0.5
C = A * b
print(C)
