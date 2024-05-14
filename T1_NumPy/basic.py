import numpy as np

# [1] Able to declare data type of an array
a = np.uint16(34)
b = np.complex128([3.2, 4.2+1.09j])
c = np.array([2334.432, 2.23], dtype=np.single)

# [2] Scalar of Numpy
a = np.int64(33)
print(a.flags)

# [3] Array and Matrix
A = np.array([[1, 2], [3, 4]]) # ndarray object
B = np.matrix([[1, 2], [3, 4]]) # matrix
print(A)
print(B)
'''
For example,
[ S = (HVH^T)^-1 ]

- ndarrary
> S = inv(H.dot(V.dot(H.T)))
> or S = inv(H @ V @ H.T)

- matrix
> S = inv(H * V * H.T)

=> Better to use ndarray
'''

# [4] Create ndarray
matA = [[3, 1, 9], [2, 5, 8], [4, 7, 6]] # Python Original
matB = np.array([[3, 1, 9], [2, 5, 8], [4, 7, 6]])
matC = np.array(((3, 1, 9), (2, 5, 8), (4, 7, 6))) 
'''
- Data is stored in a continuous space on the memory.
- Basically, all elements are of the same data type.
- The number of elements must be the same for each dimension.
- A specific operation may be performed at high speed on all elements or some elements in the array.
'''
print(np.zeros((2, 3)))
print(np.arange(10, 20, 2)) # arange([start,] stop[, step,][, dtype])
print(np.arange(0.1, 0.4, 0.1)) # include 0.4
print(np.arange(1, 4, 1)) # not include 4

# [5] Set Data Type
dt = np.dtype('float')
x = np.array([1.1, 2.1, 3.1], dtype=dt)
x = np.array([1.1, 2.1, 3.1], dtype='float')
x = np.array([1.1+2.2j, 2.1-3.4j], dtype='cfloat')

dt = np.dtype(np.int64)
dt = np.dtype('i8')
x = np.array([1.1+2.2j, 2.1-3.4j], dtype='complex64')
x = np.array([1.1+2.2j, 2.1-3.4j], dtype='c8')

# [6] Properties Examples
print(matB.shape)
print(matB.dtype)

# [7] Matrix Operations
# A = [[-2, 1], [1.5, -0.5]]
print(np.linalg.inv(A))
print(np.linalg.det(A))
print(np.linalg.matrix_rank(A))

a, b = np.array([2, -4, 1]), np.array([3, 1, -2])
print(np.inner(a, b))
print(np.cross(a, b))