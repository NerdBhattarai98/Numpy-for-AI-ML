# The dot product multiplies matching positions, then adds everything up. The result is one number.

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a * b)
print((a * b).sum()) #Sum of the products
print(a @ b) #@ is used for matrix multiplication but here it is fine
print(np.dot(a, b)) #gives dot product between a and b

x = np.array([3, 2, 1500])        # bedrooms, bathrooms, sqft
w = np.array([10000, 5000, 100])  # value of each feature
b = 5000

print(x @ w + b)