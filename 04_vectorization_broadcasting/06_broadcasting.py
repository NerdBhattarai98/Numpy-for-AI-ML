import numpy as np

#NumPy automatically expands smaller arrays so that arrays with compatible shapes can operate together.

a = np.ones((3, 1))
b = np.ones((1, 4))

print(a + b) #(3,1) and (1,4) like eutai shape ma rakhdiyo

# a → (3, 1) → (3, 4)

# [1 1 1 1]
# [1 1 1 1]
# [1 1 1 1]

# b → (1, 4) → (3, 4)

# [1 1 1 1]
# [1 1 1 1]
# [1 1 1 1]

# Compare shapes from RIGHT → LEFT. Each dimension must either be equal or one of them must be 1.

# a = np.ones((2, 3))
# b = np.ones((3,))

# print((a + b).shape)

# a = np.ones((3, 2))
# b = np.ones((3,))

# a + b
#The rightmost number is compared so below the rightmost is 3 and the above is 2 so now

a = np.ones((4, 1))
b = np.ones((1, 5))

print((a + b).shape)

a = np.array([[1],
              [2],
              [3]])

b = np.array([10, 20, 30])

print(a + b)

v = np.array([1, 2, 3, 4])

print(v[:, np.newaxis].shape)
print(v[np.newaxis, :].shape)

a = np.ones((2, 3))
b = np.ones((2, 1))

print((a + b).shape)