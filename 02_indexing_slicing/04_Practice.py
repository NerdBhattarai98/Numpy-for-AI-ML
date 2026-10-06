import numpy as np

A = np.array([
    [12, 25, 8, 40],
    [5,  30, 15, 45],
    [20, 10, 35, 50],
    [3,  18, 28, 60]
])

# Select every value greater than 25.
print(A[A>25])

# Select values between 10 and 40, inclusive.

print(A[(A >= 10) & (A <= 40)])

# Select rows 0 and 2.
print(A[[0,2]])

# Select columns 1 and 3.
print(A[:,[1,3]])

# Select rows 1 and 3 with columns 0 and 2.

A[np.ix_([0, 2], [1, 3])]

# Select all values greater than 20 OR less than 10.

print(A[(A < 10) | (A > 40)])