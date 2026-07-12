import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.zeros(5, dtype=int)
c = np.ones((2, 3), dtype=int)


print(a)
print(a * 2)
print(a + 100)
print(a + a)
print(a.shape)
print(a.dtype)

print(b)
print(b.shape)
print(b.dtype)

print(complex)
print(c.shape)
print(c.dtype)


# print result
#
# [10 20 30 40]
# [20 40 60 80]
# [110 120 130 140]
# [20 40 60 80]
# (4,)
# int64
# [0 0 0 0 0]
# (5,)
# int64
# [[1 1 1]
#  [1 1 1]]
# (2, 3)
# int64

# 2 part

print(a[0])
print(a[1:4])
print(a[-1])

m = np.array([[1, 2, 3], [4, 5, 6]])
print(m[0, 2])
print(m[:, 1])
print(m[1, :])


arr = np.array([5, 10, 15, 20, 25, 30])
print(arr[0])
print(arr[-1])
print(arr[0:3])
print(arr[-2:])
print(arr[1:4])

mtrx = np.arange(12).reshape(3, 4)
print(mtrx)
print(mtrx[1, :])
print(mtrx[:, 2])
print(mtrx[1, 2])

# print
#
# 5
# 30
# [ 5 10 15]
# [25 30]
# [10 15 20]
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# [4 5 6 7]
# [ 2  6 10]
# 6


# part 3


A = np.arange(12).reshape(3, 4)
row = np.array([100, 200, 300, 400])
print(A + row)

col = np.array([[10], [20], [30]])
col_shape = col.shape

print(col_shape)
print(A + col)

# print(A + np.array([1, 2, 3]))

# print
#
# [[100 201 302 403]
#  [104 205 306 407]
#  [108 209 310 411]]
# (3, 1)
# [[10 11 12 13]
#  [24 25 26 27]
#  [38 39 40 41]]
# Traceback (most recent call last):
#   File "/Users/martyn/development/MLLearning/ML Learning/code/phase-0/03_numpy.py", line 90, in <module>
#     print(A + np.array([1, 2, 3]))
#           ~~^~~~~~~~~~~~~~~~~~~~~
# ValueError: operands could not be broadcast together with shapes (3,4) (3,)


# part 4
print("part 4")

# dataset = np.random.randint(0, 99, 15).reshape(5, 3)
#
dataset = np.random.randint(0, 99, size=(5, 3))

print(dataset.shape)
print(dataset.dtype)
print(dataset.mean(axis=1).shape)

mean_per_col = dataset.mean(axis=0)
std_per_col = dataset.std(axis=0)

print(mean_per_col)
print(std_per_col)

print(mean_per_col.shape)
print(std_per_col.shape)
print(dataset.shape)


z = (dataset - mean_per_col) / std_per_col
print(z)
print(z.mean(axis=0))
print(z.std(axis=0))
