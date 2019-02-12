# sparse matrix
from numpy import array
from numpy import count_nonzero
from scipy.sparse import csr_matrix
# create a dense matrix
A = array([
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]
])
print(A)
# convert to sparse matrix
S = csr_matrix(A)
print(S)
# reconstruct dense matrix
B = S.todense()
print(B)

# calculate sparsity
sparsity = 1.0 - count_nonzero(A) / A.size
print(sparsity)
