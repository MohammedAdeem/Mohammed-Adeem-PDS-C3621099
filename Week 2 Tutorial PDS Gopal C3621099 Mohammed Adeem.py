
import numpy as np

#Task 1

a = np.array([2, 3, 4])
print(a)
print(a.dtype)

b = np.array([1.2, 3.5, 5.1])
print(b.dtype)

# Why can’t NumPy mix integers and floats freely?
# Numpy can accept both but standard Numpy accepts one standard data type.

# Task 2
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
print(c.shape)
print(c.dtype)

# ndarray is NumPy's array object, which can hold data in one or more dimensions.

# shape tells you the size of each dimension. (2, 2) means two rows and two columns.

#  type tells you the type of values stored. Complex means NumPy stores complex numbers,
#  so values will appear in a form such as 1.+0.j.

# Task 3
zeros = np.zeros((3, 4))
ones = np.ones((2, 3), dtype=np.int16)
empty = np.empty((2, 3))

print(zeros)
print(ones)
print(empty)
# Why is empty() dangerous?
# Because the contents are not predictable until they have assigned values.

# Task 4
import numpy as np

print(np.arange(10, 30, 5))
print(np.linspace(0, 2, 9))

# What is floating-point precision?
# Computers cannot represent every decimal exactly in binary. This can produce tiny rounding errors.
# For example, calculations involving 0.1 may not produce the exact mathematical decimal you expect.
# What is linespace?
# linespace is better when you need a specific number and want a specific endpoint.

# mini excercise
from numpy import pi

x = np.linspace(0, 2 * pi, 100)
y = np.sin(x)

print(x)
print(y)

# Task 5

a = np.array([20, 30, 40, 50])
b = np.arange(4)

print(a - b)
print(b ** 2)
print(10 * np.sin(a))
# Why doesn't * mean matrix multiplication?
# * normally multiplies corresponding elements of arrays.

# Task 6

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print(A * B)
print(A @ B)

# Task 7

b = np.arange(12).reshape(3, 4)

print(b)
print(b.sum(axis=0))
print(b.min(axis=1))
print(b.cumsum(axis=1))

# Task 8
a = np.arange(10) ** 3

print(a)
print(a[2])
print(a[2:5])
print(a[:6:2])
print(a[::-1])
print(a[a > 100])

# Task 9

def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)

print(b)
print(b[:, 1])
print(b[1:3, :])

# Task 10
a = np.floor(10 * np.random.random((3, 4)))

print(a)
print(a.shape)
print(a.ravel())
print(a.reshape(6, 2))
print(a.T)

#  View versus copy

# A view shares underlying data with another array. A copy has independent data.
# Changing a view can affect the original array, while changing a copy does not.
# Some operations, such as reshape, may return a view or a copy depending on the array's memory layout.

# Reshape with -1
# tells NumPy to calculate that dimension automatically from the total number of elements.

# Task 11

print(np.vstack((a, a)))
print(np.hstack((a, a)))
print(np.hsplit(a, 2))





