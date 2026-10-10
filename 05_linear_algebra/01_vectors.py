# A vector is an ordered list of numbers. In NumPy, it’s a 1D array.

import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a.shape)
print(a.ndim)

# Add and subtract

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

#  Addition and Subtraction
print(a + b)
print(a - b) #Element-Wise Component
# If the lengths differ, there’s nothing to pair up {1,2} and {1,2,3} cannot

#Scalar * Vector and Vector * Vector

v  = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(v * 5)
print(v * v2)

#Divsion
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(b / a)

#Difference Between Python List and Array
print([1, 2, 3] * 2)
print(np.array([1, 2, 3]) * 2)

# Practice
a = np.array([2,4,6])
b = np.array([1,2,3])
c = np.array([1,2])

print(a+b)
print(a-b)
print(a * 3)
print(a*b)
print(a/b)

# print(a+c)Wont work as 3 element and 2 element

mul = a * b
print(mul.shape)
print(a.reshape(3, 1))

# 7. Is a * b the same kind of operation as a * 3? Explain in one or two sentences.
# Nope not same in a*b correspofing elements are multiplied where as in a*3 each element is multiplied by 3

w = np.array([[0.2, 0.5, -1.0]])
g = np.array([[1.0, -2.0, 4.0]])
print(w - 0.1 * g)