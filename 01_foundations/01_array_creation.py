import numpy as np


# np.array() - To create numpy arrays ---------------------------------------
# syntax: numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)

A = np.array([1, 2, 3, 4, 5])
print("Original Array:", A)

copy1_arr = np.array(A)
copy1_arr[0] = 10

print("Copy of original Array:", copy1_arr)
print("Original Array:", A)


# np.asarray() - To create numpy arrays too ---------------------------------

copy2_arr = np.asarray(A)
copy2_arr[0] = 10

print("Copy of Second Array:", copy2_arr)
print("Original Array:", A)

# np.array() always creates a brand-new copy in memory,
# while np.asarray() reuses existing memory if the input is already a NumPy array.


# 0D, 1D, 2D, 3D arrays -----------------------------------------------------

arr = np.array(42)  # 0D array
print("0D Array:", arr)

A = np.array([1, 2, 3, 4, 5])  # 1D array
print("1D Array:", A)

A = np.array([[1, 2],
              [3, 4]])  # 2D array
print("2D Array:\n", A)

A = np.array([[[1, 2, 3], [4, 5, 6]]])  # 3D array
print("3D Array:\n", A)


# np.zeros() - To create array of zeros only --------------------------------

A = np.zeros((3, 3, 3, 3))
print("Zeros:\n", A)


# np.ones() - returns array with elements 1 in it ---------------------------

A = np.ones((3, 3), dtype=float)
print("Ones:\n", A)


# np.empty() - returns array of new shape without setting values
# (not really empty, some leftover values will be there) --------------------

A = np.empty((3, 3))
print("Empty:\n", A)


# np.full() - fills array with desired element in desired shape -------------

A = np.full((3, 3), 9)
print("Full:\n", A)


# np.eye() - used to create identity matrix ---------------------------------

A = np.eye(4)
print("Eye 4:\n", A)

A = np.eye(6)
print("Eye 6:\n", A)

# np.eye() but for rectangular array
A = np.eye(3, 4)
print("Eye 3x4:\n", A)

A = np.eye(3, 4, k=1)  # shifts the diagonal one up
print("Eye 3x4, k=1:\n", A)

A = np.eye(3, 4, k=-1)  # shifts the diagonal one down
print("Eye 3x4, k=-1:\n", A)


# np.identity() - to create a square identity matrix (square only) ----------

print("Identity 3:\n", np.identity(3))
print("Identity 2 (int):\n", np.identity(2, dtype=int))

# np.identity() vs np.eye()
# np.identity() can only make strictly square matrices
# np.eye() is flexible for rows and columns (rectangular matrix) and shifting of diagonal as well (k)


# np.diag() - creates a matrix with custom diagonal, can also extract diagonal from a matrix

print("Diag with k=2:\n", np.diag([1, 2, 3, 4, 5], k=2))  # k shifts the diagonal

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("Extracted Diagonal:", np.diag(A))


# np.arange([start,] stop[, step,], dtype=None) - builds array of certain range

print("Arange:", np.arange(1, 20, 1))  # stops before the last one


# np.linspace() - generates evenly spaced numbers over a specified interval --

print("Linspace:", np.linspace(0, 10, 5))

# retstep=True returns BOTH the array and the step size
arr, step = np.linspace(0, 63.3, 10, retstep=True)

print("Array:", arr)
print("Step size:", step)