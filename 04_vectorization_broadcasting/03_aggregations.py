import numpy as np

A = np.array([1,2,3,4,5,6,7,8,9,10])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])
#1.sum() - adds all the elements of the array

print(np.sum(A))
print(np.sum(B))

# mean() - Calculates average of the array

print(np.mean(A))
print(np.mean(B))

#std() - Calculates Standard deviation
print(np.std(A))

print(np.std(B))

# Think of it as a consistency score:
# Low standard deviation: Data points are tightly packed around the average (predictable and consistent).
# High standard deviation: Data points are scattered far and wide (high variability and chaotic).

# min() / max() - find smallest and largest value in an array

print(np.min(A))
print(np.max(A))

# argmax() - Returns the index of largest value

print(np.argmax(A))

# cumsum() - Calculates Cumulative Sum
# A cumulative sum (or running total) is a sequence where each item is calculated by 
# adding the current value to the sum of all previous values before it.

print(np.cumsum(A))

# prod() - Multiplies all element of the array

print(np.prod(A))

#axis = controls the direction of aggregation

print(B.sum(axis=0)) #Column

print(B.sum(axis=1)) #Row

# For a 3 × 3 matrix, calculate:

# column sums
# row sums
# column means
# row means

B = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(B.sum(axis = 0))
print(B.mean(axis = 0))

print(B.sum(axis = 1))
print(B.mean(axis = 1))

# keepdims=True -Keeps the reduced dimension instead of removing it.

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.mean(axis=0).shape)
print(a.mean(axis=0, keepdims=True).shape) 
# (3,)
# (1, 3) Kept the two dimenstion as it is only like from (3,) made (1,3)