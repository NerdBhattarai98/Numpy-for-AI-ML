INDEXING
arr[0]
arr[-1]
A[0, 1]

SLICING
arr[start:stop:step]

2D SLICING
A[rows, columns]
A[0:2, 1:3]
A[:, 1]
A[1, :]

BOOLEAN INDEXING
A[A > 5]
A[(A > 5) & (A < 10)]

FANCY INDEXING
A[[0, 2, 4]]

VIEW vs COPY
B = A[1:4]          # view
B = A[1:4].copy()   # copy