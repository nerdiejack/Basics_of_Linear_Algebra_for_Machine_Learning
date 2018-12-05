# create array
from numpy import array
from numpy import empty
from numpy import zeros
from numpy import ones
from numpy import vstack
from numpy import hstack

# # create array
# l = [1.0, 2.0, 3.0]
# a = array(l)
# # display array
# print(a)
# # display array shape
# print(a.shape)
# # display array data type
# print(a.dtype)
# # create empty array
# a = empty([3, 3])
# print(a)
# # create zero array
# a = zeros([3, 5])
# print(a)
# # create one array
# a = ones([5])
# print(a)
# # create array with vstack
# a1 = array([1, 2, 3])
# print(a1)
# a2 = array([4, 5, 6])
# print(a2)
# # vertical stack
# a3 = vstack((a1, a2))
# print(a3)
# print(a3.shape)
# # create array with hstack
# a3 = hstack((a1, a2))
# print(a3)
# print(a3.shape)
# slice a one-dimensional array
# data = array([11, 22, 33, 44, 55])
# print(data[:])
# print(data[0:1])
# print(data[-2:])
# split input and output data
# data = array([
#     [11, 22, 33],
#     [44, 55, 66],
#     [77, 88, 99]])
# # separate data
# X, y = data[:, :-1], data[:, -1]
# print(X)
# print(y)
# split train and test data
# data = array([
#     [11, 22, 33],
#     [44, 55, 66],
#     [77, 88, 99]])
# split = 2
# train, test = data[:split,:], data[split:,:]
# print(train)
# print(test)

